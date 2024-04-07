[//]: # ([//]: # &#40;[//]: # &#40;<h1 align="center">Image Style Transfer with Streamlit</h1>&#41;&#41;)
[//]: # ([//]: # &#40;&#41;)
[//]: # ([//]: # &#40;[//]: # &#40;<p align="center">&#41;&#41;)
[//]: # ([//]: # &#40;&#41;)
[//]: # ([//]: # &#40;[//]: # &#40;  <img src="images/banner.png" alt="Image Style Transfer Banner" width="600">&#41;&#41;)
[//]: # ([//]: # &#40;&#41;)
[//]: # ([//]: # &#40;[//]: # &#40;</p>&#41;&#41;)
[//]: # ([//]: # &#40;&#41;)
[//]: # ([//]: # &#40;[//]: # &#40;&#41;&#41;)
[//]: # ([//]: # &#40;[//]: # &#40;Overview&#41;&#41;)
[//]: # ([//]: # &#40;&#41;)
[//]: # ([//]: # &#40;[//]: # &#40;&#41;&#41;)
[//]: # ([//]: # &#40;[//]: # &#40;The Image Style Transfer application is an interactive tool that allows users to transfer the style of one image onto another using the VGG-19 model. Users can upload images, provide text prompts, and generate stunning artistic creations effortlessly.&#41;&#41;)
[//]: # ([//]: # &#40;&#41;)
[//]: # ([//]: # &#40;[//]: # &#40;&#41;&#41;)
[//]: # ([//]: # &#40;[//]: # &#40;Key Features&#41;&#41;)
[//]: # ([//]: # &#40;&#41;)
[//]: # ([//]: # &#40;<!DOCTYPE html>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;<html lang="en">&#41;)
[//]: # ()
[//]: # ([//]: # &#40;<head>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;  <meta charset="UTF-8">&#41;)
[//]: # ()
[//]: # ([//]: # &#40;  <meta name="viewport" content="width=device-width, initial-scale=1.0">&#41;)
[//]: # ()
[//]: # ([//]: # &#40;  <title>Image Style Transfer with Streamlit</title>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;</head>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;<body>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;  <h1 style="text-align: center;">Image Style Transfer with Streamlit</h1>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;&#41;)
[//]: # ([//]: # &#40;  <p style="text-align: center;">&#41;)
[//]: # ()
[//]: # ([//]: # &#40;&#41;)
[//]: # ([//]: # &#40;[//]: # &#40;    <img src="images/banner.png" alt="Image Style Transfer Banner" width="600">&#41;&#41;)
[//]: # ([//]: # &#40;<img src="MARK 5/1.png" alt="Image Style Transfer Banner" width="600">&#41;)
[//]: # ()
[//]: # ([//]: # &#40;  </p>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;&#41;)
[//]: # ([//]: # &#40;  <h2>Overview</h2>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;&#41;)
[//]: # ([//]: # &#40;  <p>The Image Style Transfer application is an interactive tool that allows users to transfer the style of one image onto another using the VGG-19 model. Users can upload images, provide text prompts, and generate stunning artistic creations effortlessly.</p>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;&#41;)
[//]: # ([//]: # &#40;  <h2>Key Features</h2>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;&#41;)
[//]: # ([//]: # &#40;  <ul>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;    <li><strong>Upload Images:</strong> Easily upload your content and style images for style transfer.</li>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;    <li><strong>Text-to-Image:</strong> Generate images from text prompts using the integrated ClipDrop API.</li>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;    <li><strong>VGG-19 Model:</strong> Leverage the power of the VGG-19 model for high-quality style transfer.</li>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;    <li><strong>Streamlit Interface:</strong> Enjoy a simple and intuitive user interface powered by Streamlit.</li>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;    <li><strong>Customization:</strong> Fine-tune style transfer parameters such as epochs and image dimensions.</li>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;  </ul>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;&#41;)
[//]: # ([//]: # &#40;  <h2>Installation</h2>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;&#41;)
[//]: # ([//]: # &#40;  <ol>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;    <li><strong>Clone Repository:</strong></li>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;    <pre><code>git clone https://github.com/SDE-Ashik/stylen.git</code></pre>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;    <li><strong>Install Dependencies:</strong></li>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;    <pre><code>pip install -r requirements.txt</code></pre>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;    <li><strong>Set API Key:</strong></li>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;    <ul>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;      <li>Obtain an API key from ClipDrop and replace 'your_api_key_here' in the code with your actual API key.</li>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;    </ul>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;    <li><strong>Configure .env File:</strong></li>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;    <ul>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;      <li>Create a .env file in the root directory of the project.</li>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;      <li>Add your API key to the .env file using the following format:</li>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;      <pre><code>API_KEY=your_api_key_here</code></pre>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;    </ul>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;  </ol>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;&#41;)
[//]: # ([//]: # &#40;  <h2>Usage</h2>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;&#41;)
[//]: # ([//]: # &#40;  <ol>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;    <li><strong>Run Streamlit App:</strong></li>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;    <pre><code> streamlit run main_program.py&#41;)
[//]: # ()
[//]: # ([//]: # &#40;</code></pre>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;    <li><strong>Access App:</strong></li>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;    <ul>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;      <li>Open the provided URL in your web browser to access the application.</li>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;    </ul>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;    <li><strong>Generate Images:</strong></li>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;    <ul>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;      <li>Upload images or provide text prompts to initiate style transfer and generate images.</li>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;    </ul>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;  </ol>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;&#41;)
[//]: # ([//]: # &#40;  <h2>Screenshots</h2>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;&#41;)
[//]: # ([//]: # &#40;  <p style="text-align: center;">&#41;)
[//]: # ()
[//]: # ([//]: # &#40;    <img src="MARK 5/3.png" alt="Uploaded Photos" width="800">&#41;)
[//]: # ()
[//]: # ([//]: # &#40;  </p>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;&#41;)
[//]: # ([//]: # &#40;  <p style="text-align: center;">&#41;)
[//]: # ()
[//]: # ([//]: # &#40;    <img src="MARK 5/8.png" alt="Text Prompts" width="800">&#41;)
[//]: # ()
[//]: # ([//]: # &#40;  </p>&#41;)
[//]: # ()
[//]: # ([//]: # &#40; <p style="text-align: center;">&#41;)
[//]: # ()
[//]: # ([//]: # &#40;    <img src="MARK 5/5.png" alt="Text Prompts" width="800">&#41;)
[//]: # ()
[//]: # ([//]: # &#40;  </p>&#41;)
[//]: # ()
[//]: # ([//]: # &#40; <p style="text-align: center;">&#41;)
[//]: # ()
[//]: # ([//]: # &#40;    <img src="MARK 5/6.png" alt="Text Prompts" width="800">&#41;)
[//]: # ()
[//]: # ([//]: # &#40;  </p>&#41;)
[//]: # ()
[//]: # ([//]: # &#40; <p style="text-align: center;">&#41;)
[//]: # ()
[//]: # ([//]: # &#40;    <img src="MARK 5/7.png" alt="Text Prompts" width="800">&#41;)
[//]: # ()
[//]: # ([//]: # &#40;  </p>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;&#41;)
[//]: # ([//]: # &#40;  <h2>Contributing</h2>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;&#41;)
[//]: # ([//]: # &#40;  <p>Contributions to improve the project are welcome. Please fork the repository and submit pull requests with your changes.</p>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;&#41;)
[//]: # ([//]: # &#40;  <h2>License</h2>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;&#41;)
[//]: # ([//]: # &#40;  <p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;</body>&#41;)
[//]: # ()
[//]: # ([//]: # &#40;</html>&#41;)
[//]: # (<!DOCTYPE html>)

[//]: # (<html lang="en">)

[//]: # (<head>)

[//]: # (  <meta charset="UTF-8">)

[//]: # (  <meta name="viewport" content="width=device-width, initial-scale=1.0">)

[//]: # (  <title>Image Style Transfer with Streamlit</title>)

[//]: # (  <style>)

[//]: # (    body {)

[//]: # (      background-color: black;)

[//]: # (      color: white;)

[//]: # (      font-family: Arial, sans-serif;)

[//]: # (      padding: 20px;)

[//]: # (    })

[//]: # (    h1, h2, h3, h4, h5, h6 {)

[//]: # (      color: white;)

[//]: # (    })

[//]: # (    img {)

[//]: # (      display: block;)

[//]: # (      margin: 0 auto;)

[//]: # (    })

[//]: # (    pre {)

[//]: # (      background-color: #333;)

[//]: # (      color: white;)

[//]: # (      padding: 10px;)

[//]: # (      border-radius: 5px;)

[//]: # (      overflow-x: auto;)

[//]: # (    })

[//]: # (    code {)

[//]: # (      color: white;)

[//]: # (    })

[//]: # (  </style>)

[//]: # (</head>)

[//]: # (<body>)

[//]: # (  <h1 style="text-align: center;">Image Style Transfer with Streamlit</h1>)

[//]: # ()
[//]: # (  <p style="text-align: center;">)

[//]: # (    <img src="MARK 5/1.png" alt="Image Style Transfer Banner" width="600">)

[//]: # (  </p>)

[//]: # ()
[//]: # (  <h2>Overview</h2>)

[//]: # ()
[//]: # (  <p>The Image Style Transfer application is an interactive tool that allows users to transfer the style of one image onto another using the VGG-19 model. Users can upload images, provide text prompts, and generate stunning artistic creations effortlessly.</p>)

[//]: # ()
[//]: # (  <h2>Key Features</h2>)

[//]: # ()
[//]: # (  <ul>)

[//]: # (    <li><strong>Upload Images:</strong> Easily upload your content and style images for style transfer.</li>)

[//]: # (    <li><strong>Text-to-Image:</strong> Generate images from text prompts using the integrated ClipDrop API.</li>)

[//]: # (    <li><strong>VGG-19 Model:</strong> Leverage the power of the VGG-19 model for high-quality style transfer.</li>)

[//]: # (    <li><strong>Streamlit Interface:</strong> Enjoy a simple and intuitive user interface powered by Streamlit.</li>)

[//]: # (    <li><strong>Customization:</strong> Fine-tune style transfer parameters such as epochs and image dimensions.</li>)

[//]: # (  </ul>)

[//]: # ()
[//]: # (  <h2>Installation</h2>)

[//]: # ()
[//]: # (  <ol>)

[//]: # (    <li><strong>Clone Repository:</strong></li>)

[//]: # (    <pre><code>git clone https://github.com/SDE-Ashik/stylen.git</code></pre>)

[//]: # (    <li><strong>Install Dependencies:</strong></li>)

[//]: # (    <pre><code>pip install -r requirements.txt</code></pre>)

[//]: # (    <li><strong>Set API Key:</strong></li>)

[//]: # (    <ul>)

[//]: # (      <li>Obtain an API key from ClipDrop and replace 'your_api_key_here' in the code with your actual API key.</li>)

[//]: # (    </ul>)

[//]: # (    <li><strong>Configure .env File:</strong></li>)

[//]: # (    <ul>)

[//]: # (      <li>Create a .env file in the root directory of the project.</li>)

[//]: # (      <li>Add your API key to the .env file using the following format:</li>)

[//]: # (      <pre><code>API_KEY=your_api_key_here</code></pre>)

[//]: # (    </ul>)

[//]: # (  </ol>)

[//]: # ()
[//]: # (  <h2>Usage</h2>)

[//]: # ()
[//]: # (  <ol>)

[//]: # (    <li><strong>Run Streamlit App:</strong></li>)

[//]: # (    <pre><code> streamlit run main_program.py)

[//]: # (</code></pre>)

[//]: # (    <li><strong>Access App:</strong></li>)

[//]: # (    <ul>)

[//]: # (      <li>Open the provided URL in your web browser to access the application.</li>)

[//]: # (    </ul>)

[//]: # (    <li><strong>Generate Images:</strong></li>)

[//]: # (    <ul>)

[//]: # (      <li>Upload images or provide text prompts to initiate style transfer and generate images.</li>)

[//]: # (    </ul>)

[//]: # (  </ol>)

[//]: # ()
[//]: # (  <h2>Screenshots</h2>)

[//]: # ()
[//]: # (  <p style="text-align: center;">)

[//]: # (    <img src="MARK 5/3.png" alt="Uploaded Photos" width="800">)

[//]: # (  </p>)

[//]: # ()
[//]: # (  <p style="text-align: center;">)

[//]: # (    <img src="MARK 5/8.png" alt="Text Prompts" width="800">)

[//]: # (  </p>)

[//]: # ( <p style="text-align: center;">)

[//]: # (    <img src="MARK 5/5.png" alt="Text Prompts" width="800">)

[//]: # (  </p>)

[//]: # ( <p style="text-align: center;">)

[//]: # (    <img src="MARK 5/6.png" alt="Text Prompts" width="800">)

[//]: # (  </p>)

[//]: # ( <p style="text-align: center;">)

[//]: # (    <img src="MARK 5/7.png" alt="Text Prompts" width="800">)

[//]: # (  </p>)

[//]: # ()
[//]: # (  <h2>Contributing</h2>)

[//]: # ()
[//]: # (  <p>Contributions to improve the project are welcome. Please fork the repository and submit pull requests with your changes.</p>)

[//]: # ()
[//]: # (  <h2>License</h2>)

[//]: # ()
[//]: # (  <p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>)

[//]: # (</body>)

[//]: # (</html>)
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Image Style Transfer with Streamlit</title>
  <style>
    body {
      background-color: #1a1a1a;
      color: white;
      font-family: Arial, sans-serif;
      padding: 20px;
      line-height: 1.6;
    }
    h1 {
      text-align: center;
      font-size: 32px;
      margin-bottom: 20px;
    }
    h2 {
      font-size: 24px;
      margin-bottom: 15px;
    }
    p {
      margin-bottom: 15px;
    }
    ul {
      margin-bottom: 15px;
      padding-left: 20px;
    }
    pre {
      background-color: #333;
      color: white;
      padding: 10px;
      border-radius: 5px;
      overflow-x: auto;
    }
    code {
      color: white;
    }
    img {
      display: block;
      margin: 0 auto;
      max-width: 100%;
      height: auto;
      margin-bottom: 20px;
    }
  </style>
</head>
<body>
  <h1>Image Style Transfer with Streamlit</h1>

  <img src="MARK 5/1.png" alt="Image Style Transfer Banner">

  <h2>Overview</h2>

  <p>The Image Style Transfer application is an interactive tool that allows users to transfer the style of one image onto another using the VGG-19 model. Users can upload images, provide text prompts, and generate stunning artistic creations effortlessly.</p>

  <h2>Key Features</h2>

  <ul>
    <li><strong>Upload Images:</strong> Easily upload your content and style images for style transfer.</li>
    <li><strong>Text-to-Image:</strong> Generate images from text prompts using the integrated ClipDrop API.</li>
    <li><strong>VGG-19 Model:</strong> Leverage the power of the VGG-19 model for high-quality style transfer.</li>
    <li><strong>Streamlit Interface:</strong> Enjoy a simple and intuitive user interface powered by Streamlit.</li>
    <li><strong>Customization:</strong> Fine-tune style transfer parameters such as epochs and image dimensions.</li>
  </ul>

  <h2>Installation</h2>

  <ol>
    <li><strong>Clone Repository:</strong></li>
    <pre><code>git clone https://github.com/SDE-Ashik/stylen.git</code></pre>
    <li><strong>Install Dependencies:</strong></li>
    <pre><code>pip install -r requirements.txt</code></pre>
    <li><strong>Set API Key:</strong></li>
    <ul>
      <li>Obtain an API key from ClipDrop and replace 'your_api_key_here' in the code with your actual API key.</li>
    </ul>
    <li><strong>Configure .env File:</strong></li>
    <ul>
      <li>Create a .env file in the root directory of the project.</li>
      <li>Add your API key to the .env file using the following format:</li>
      <pre><code>API_KEY=your_api_key_here</code></pre>
    </ul>
  </ol>

  <h2>Usage</h2>

  <ol>
    <li><strong>Run Streamlit App:</strong></li>
    <pre><code> streamlit run main_program.py
</code></pre>
    <li><strong>Access App:</strong></li>
    <ul>
      <li>Open the provided URL in your web browser to access the application.</li>
    </ul>
    <li><strong>Generate Images:</strong></li>
    <ul>
      <li>Upload images or provide text prompts to initiate style transfer and generate images.</li>
    </ul>
  </ol>

  <h2>Screenshots</h2>

  <img src="MARK 5/3.png" alt="Uploaded Photos">
  <img src="MARK 5/8.png" alt="Text Prompts">
  <img src="MARK 5/5.png" alt="Text Prompts">
  <img src="MARK 5/6.png" alt="Text Prompts">
  <img src="MARK 5/7.png" alt="Text Prompts">

  <h2>Contributing</h2>

  <p>Contributions to improve the project are welcome. Please fork the repository and submit pull requests with your changes.</p>

  <h2>License</h2>

  <p>This project is licensed under the <a href="LICENSE" style="color: #4caf50; text-decoration: underline;">MIT License</a>.</p>
</body>
</html>
