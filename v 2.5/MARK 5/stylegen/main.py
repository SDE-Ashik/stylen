import streamlit as st
import os
import tempfile
from streamlit_lottie import st_lottie
import json
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.applications import vgg19
import base64
from PIL import Image
import plotly.graph_objects as go
import openai
from craiyon import Craiyon, craiyon_utils
from PIL import Image
from io import BytesIO


class Output:

    def __init__(self,img,epch,lsd):
        self.image =  img
        self.e = epch
        self.l = lsd

    def output_display(self):

        st.balloons()
        st.write("""""")
        st.write("""""")
        st.write("""""")
        st.title("🖌️ StyleGen")
        st.markdown("""
        ## Image Style Transfer using VGG - 19
        ### Here is the output!!!
        """)
        #st.image(self.image)
        """
        # Convert image to bytes
        image_bytes = self.image.tobytes()

        # Define function to create a download link
        def get_image_download_link(img_bytes):
            b64 = base64.b64encode(img_bytes).decode()
            href = f'data:application/octet-stream;base64,{b64}'
            return href
        """
        # Convert numpy array to PIL Image
        img = Image.fromarray(self.image)

        # Save image as "output.png"
        img.save("output.png")

        # Show image and download button
        st.image(self.image, caption="Output Image")
        button = st.download_button(
            label="Download image",
            data= open("output.png", "rb").read(),
            file_name="output_image.jpg",
            mime = "image/png"
        )

        # Define the data
        epochs_range = np.array([x for x in range(100, self.e + 1, 100)])
        loss_data = np.array(self.l)

        # Create a plotly figure
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=epochs_range, y=loss_data, mode='lines', name='Loss'))
        fig.update_layout(
            xaxis_title='Iterations',
            yaxis_title='Total Loss rate',
            title='Total Loss Graph',
            showlegend=True
        )

        # Display the chart in Streamlit
        st.plotly_chart(fig)



class json_file:

    def __init__(self):
        pass

    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)

class Load(json_file):

    def __init__(self):
        #self.progress = st.progress(0)
        self.progress = None
    def load_display(self):
        st.write("""""")
        st.write("""""")
        st.write("""""")
        st.title("⚙ Image Style Transferring")
        file = json_file.load_lottiefile("load.json")
        print(file)

        st_lottie(
            file,
            speed=1,
            reverse=False,
            loop=True,
            quality="high",  # medium ; high
            height=300,
            width=None,
            key=None,
        )
        self.progress = st.progress(0,text="Loading model... Please wait... Takes time...")
        """
        progress_label = "Loading model..."
        for i in range(100):
            time.sleep(0.1)
            progress_text = f"{progress_label} {i+1}/100"
            self.progress.progress(i + 1,text=progress_text)
        """
class Core(Load):

    def __init__(self,img_path,style_path,epch):

        self.loss_data=[]
        self.param = []

        Load.__init__(self)
        self.base_image_path = img_path
        self.style_reference_image_path = style_path
        self.epoch = epch
        self.result_prefix = "generated"

        # Weights of the different loss components
        self.total_variation_weight = 1e-6
        self.style_weight = 1e-6
        self.content_weight = 2.5e-8

        # Dimensions of the generated picture.
        self.width, self.height = keras.preprocessing.image.load_img(self.base_image_path).size
        self.img_nrows = 400
        self.img_ncols = int(self.width * self.img_nrows / self.height)

        """
        print("Source Image")
        display(Image(base_image_path))
        """

        # HIDE OUTPUT
        # Build a VGG19 model loaded with pre-trained ImageNet weights
        self.model = vgg19.VGG19(weights="imagenet", include_top=False)

        # Get the symbolic outputs of each "key" layer (we gave them unique names).
        self.outputs_dict = dict([(layer.name, layer.output) for layer in self.model.layers])

        # Set up a model that returns the activation values for every layer in
        # VGG19 (as a dict).
        self.feature_extractor = keras.Model(inputs=self.model.inputs, outputs=self.outputs_dict)

        # List of layers to use for the style loss.
        self.style_layer_names = [
            "block1_conv1",
            "block2_conv1",
            "block3_conv1",
            "block4_conv1",
            "block5_conv1",
        ]
        # The layer to use for the content loss.
        self.content_layer_name = "block5_conv2"

    def preprocess_image(self,image_path):
        # Util function to open, resize and format
        # pictures into appropriate tensors
        img = keras.preprocessing.image.load_img(
            image_path, target_size=(self.img_nrows, self.img_ncols)
        )
        img = keras.preprocessing.image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img = vgg19.preprocess_input(img)
        return tf.convert_to_tensor(img)

    def deprocess_image(self,x):
        # Util function to convert a tensor into a valid image
        x = x.reshape((self.img_nrows, self.img_ncols, 3))
        # Remove zero-center by mean pixel
        x[:, :, 0] += 103.939
        x[:, :, 1] += 116.779
        x[:, :, 2] += 123.68
        # 'BGR'->'RGB'
        x = x[:, :, ::-1]
        x = np.clip(x, 0, 255).astype("uint8")
        return x

    # The gram matrix of an image tensor (feature-wise outer product)
    def gram_matrix(self,x):
        x = tf.transpose(x, (2, 0, 1))
        features = tf.reshape(x, (tf.shape(x)[0], -1))
        gram = tf.matmul(features, tf.transpose(features))
        return gram

    # The "style loss" is designed to maintain
    # the style of the reference image in the generated image.
    # It is based on the gram matrices (which capture style) of
    # feature maps from the style reference image
    # and from the generated image
    def style_loss(self, style, combination):
        S = self.gram_matrix(style)
        C = self.gram_matrix(combination)
        channels = 3
        size = self.img_nrows * self.img_ncols
        return tf.reduce_sum(tf.square(S - C)) / (4.0 * (channels ** 2) * (size ** 2))

    # An auxiliary loss function
    # designed to maintain the "content" of the
    # base image in the generated image
    def content_loss(self, base, combination):
        return tf.reduce_sum(tf.square(combination - base))

    # The 3rd loss function, total variation loss,
    # designed to keep the generated image locally coherent
    def total_variation_loss(self,x):
        a = tf.square(
            x[:, : self.img_nrows - 1, : self.img_ncols - 1, :] \
            - x[:, 1:, : self.img_ncols - 1, :]
        )
        b = tf.square(
            x[:, : self.img_nrows - 1, : self.img_ncols - 1, :] \
            - x[:, : self.img_nrows - 1, 1:, :]
        )
        return tf.reduce_sum(tf.pow(a + b, 1.25))

    def compute_loss(self, combination_image, base_image, style_reference_image):
        input_tensor = tf.concat(
            [base_image, style_reference_image, combination_image], axis=0
        )
        features = self.feature_extractor(input_tensor)

        # Initialize the loss
        loss = tf.zeros(shape=())

        # Add content loss
        layer_features = features[self.content_layer_name]
        base_image_features = layer_features[0, :, :, :]
        combination_features = layer_features[2, :, :, :]
        loss = loss + self.content_weight * self.content_loss(
            base_image_features, combination_features
        )
        # Add style loss
        for layer_name in self.style_layer_names:
            layer_features = features[layer_name]
            style_reference_features = layer_features[1, :, :, :]
            combination_features = layer_features[2, :, :, :]
            sl = self.style_loss(style_reference_features, combination_features)
            loss += (self.style_weight / len(self.style_layer_names)) * sl

        # Add total variation loss
        loss += self.total_variation_weight * \
                self.total_variation_loss(combination_image)
        return loss

    @tf.function
    def compute_loss_and_grads(self,combination_image,base_image, style_reference_image):
        with tf.GradientTape() as tape:
            loss = self.compute_loss(combination_image,base_image, style_reference_image)
        grads = tape.gradient(loss, combination_image)
        return loss, grads

    def image_style_processing(self):

        self.load_display()
        progress_label = "Image Processing..."
        optimizer = keras.optimizers.SGD(
            keras.optimizers.schedules.ExponentialDecay(
            initial_learning_rate=100.0, decay_steps=100, decay_rate=0.96
            )
        )

        base_image = self.preprocess_image(self.base_image_path)
        style_reference_image = self.preprocess_image(self.style_reference_image_path)
        combination_image = tf.Variable(self.preprocess_image(self.base_image_path))
        for i in range(1,self.epoch+ 1):
            loss, grads = self.compute_loss_and_grads(
                combination_image, base_image, style_reference_image
            )
            optimizer.apply_gradients([(grads, combination_image)])
            if(i%100 == 0):
                self.loss_data.append(loss)
            progress_scale = i/self.epoch
            img = self.deprocess_image(combination_image.numpy())
            #fname = self.result_prefix + "_at_iteration_%d.png" % i
            #keras.preprocessing.image.save_img(fname, img)
            progress_text = f"{progress_label} {i}/{self.epoch} and Loss = {loss:.2f}"
            self.progress.progress(progress_scale, text=progress_text)
            """
            partition = (100//(self.epoch/100))/100

            if i % 100 == 0:
                #print("Iteration %d: loss=%.2f" % (i, loss))
                img = self.deprocess_image(combination_image.numpy())
                fname = self.result_prefix + "_at_iteration_%d.png" % i
                #keras.preprocessing.image.save_img(fname, img)
                progress_text = f"{progress_label} {i}/{self.epoch} and Loss = {loss:.2f}"
                self.progress.progress(partition * count, text=progress_text)
                count+=1
                #print(partition,count,partition*count)
            """
        

        out = Output(img,self.epoch,self.loss_data)
        st.session_state.current_page = out
        out.output_display()



class Main:

    def __init__(self):
        self.photo_upload = None
        self.style_upload = None
        self.generate_photo_input = ''
        self.generate_style_input = ''
        self.generate_photo = None
        self.generate_style = None
        self.epoch = 200
        self.params = []
        self.generator = Craiyon()
        self.A = None
        self.B = None
        self.C = None
        self.D = None
        self.A_comp = None
        self.B_comp = None
        self.C_comp = None
        self.D_comp = None
        self.photo_file_path = None
        self.style_file_path = None

    def main_parameters_return(self):

        with tempfile.NamedTemporaryFile(delete=False) as photo_temp_file:
            if self.photo_upload is not None:
                photo_temp_file.write(self.photo_upload.read())
            else:
                with open('generated_photo.jpg', 'rb') as generated_photo_file:
                    photo_temp_file.write(generated_photo_file.read())
                os.remove('generated_photo.jpg')
            self.photo_file_path = photo_temp_file.name

        with tempfile.NamedTemporaryFile(delete=False) as style_temp_file:
            if self.style_upload is not None:
                style_temp_file.write(self.style_upload.read())
            else:
                with open('generated_style.jpg', 'rb') as generated_style_file:
                    style_temp_file.write(generated_style_file.read())
                os.remove('generated_style.jpg')
            self.style_file_path = style_temp_file.name

        self.params.append(self.photo_file_path)
        self.params.append(self.style_file_path)
        self.params.append(self.epoch)

        return self.params

    def call_core(self):

        p = self.main_parameters_return()
        c = Core(p[0], p[1], p[2])
        c.image_style_processing()
    
    def generation_from_text(self,txt,filename):
        result = self.generator.generate(txt)
        images = craiyon_utils.encode_base64(result.images)
        for i in images:
            image = Image.open(BytesIO(base64.decodebytes(i)))
            resized_image = image.resize((512, 512))
            image_path = filename+".jpg" 
            resized_image.save(image_path)
    
    def callback(self):
            st.session_state.button_clicked = True

    def main_display(self):

        st.title("🖌️ StyleGen")
        st.subheader("Image Style Transfer using VGG-19")
        self.photo_upload = st.file_uploader(label="Photo Upload", type=['jpeg', 'jpg', 'png'], accept_multiple_files=False,
                                            key="photo_upload")
        self.style_upload = st.file_uploader(label="Style Upload", type=['jpeg', 'jpg', 'png'], accept_multiple_files=False,
                                            key="style_upload")

        self.generate_photo_input = st.text_input("Generate Image with Text")
        self.generate_style_input = st.text_input("Generate Style Image with Text")


        self.epoch = st.slider(label="Number of Epochs", min_value=200, max_value=4000, step=100, format="%d",
                            key="epoch")

        
        if "button_clicked" not in st.session_state:
            st.session_state.button_clicked = False
        

        if (st.button("SUBMIT", on_click = self.callback) or st.session_state.button_clicked):
            self.A_comp = self.photo_upload is None
            self.B_comp = self.style_upload is None
            self.C_comp = self.generate_photo_input == ''
            self.D_comp = self.generate_style_input == ''

            if self.A_comp:
                self.A = False
            if self.B_comp:
                self.B = False

            if self.A_comp is False:
                self.A = self.photo_upload.type == "image/jpeg" or self.photo_upload.type == "image/jpg" or self.photo_upload.type == "image/png"
            if self.B_comp is False:
                self.B = self.style_upload.type == "image/jpeg" or self.style_upload.type == "image/jpg" or self.style_upload.type == "image/png"
                
            self.C = self.generate_photo_input != ''
            self.D = self.generate_style_input != ''


            y = (self.A or self.C) and (self.B or self.D) and (self.B_comp or self.D_comp) and (self.A_comp or self.C_comp)

            print(self.A,self.B,self.C,self.D)
            print(self.A_comp,self.B_comp,self.C_comp,self.D_comp)
            print(y)
            if y:
                if self.C:
                    self.generation_from_text(self.generate_photo_input, 'generated_photo')
                if self.D:
                    self.generation_from_text(self.generate_style_input, 'generated_style')
                
                st.title("🖼️ Given Input:")
                col1, col2 = st.columns(2)

                if self.A:
                    with col1:
                        st.image(self.photo_upload, use_column_width=True)
                        st.caption("Photo Reference")

                if self.B:
                    with col2:
                        st.image(self.style_upload, use_column_width=True)
                        st.caption("Style Reference")
                
                if self.C:
                    with col1:
                        st.image("generated_photo.jpg", use_column_width=True)
                        st.caption("Generated Photo Reference")

                if self.D:
                    with col2:
                        st.image("generated_style.jpg", use_column_width=True)
                        st.caption("Generated Style Reference")
                
                    
                if st.button("Confirm"):
                    self.call_core()

            else:
                st.error("Invalid input Combination!!! Enter either text or upload not both or upload required inputs")
            















