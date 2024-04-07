<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
<!--     <title>Image Style Transfer with Streamlit</title>
    <style>
        body {
            background-color: black;
            color: white;
            font-family: Arial, sans-serif;
            padding: 20px;
        }
        h1, h2, h3, h4, h5, h6 {
            color: white;
            text-align: center;
        }
        img {
            display: block;
            margin: 0 auto;
            max-width: 100%;
            height: auto;
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
        ul {
            list-style-type: none;
        }
        li::before {
            content: "•";
            color: white;
            display: inline-block;
            width: 1em;
            margin-left: -1em;
        }
        ol {
            padding-left: 20px;
        }
        pre {
            white-space: pre-wrap;
        }
    </style> -->
</head>
<body>
<h1 style="text-align: center;">Image Style Transfer with Streamlit</h1>

<p style="text-align: center;">
    <img src="https://raw.githubusercontent.com/SDE-Ashik/stylen/master/v%202.5/MARK%205/1.png" alt="Image Style Transfer Banner" width="600">
</p>

<h2>Overview</h2>

<p style="text-align: left;">The Image Style Transfer application is an interactive tool that allows users to transfer the style of one image onto
    another using the VGG-19 model. Users can upload images, provide text prompts, and generate stunning artistic
    creations effortlessly.</p>

<h2>Key Features</h2>

<ul style="text-align: left;">
    <li>Upload Images: Easily upload your content and style images for style transfer.</li>
    <li>Text-to-Image: Generate images from text prompts using the integrated ClipDrop API.</li>
    <li>VGG-19 Model: Leverage the power of the VGG-19 model for high-quality style transfer.</li>
    <li>Streamlit Interface: Enjoy a simple and intuitive user interface powered by Streamlit.</li>
    <li>Customization: Fine-tune style transfer parameters such as epochs and image dimensions.</li>
</ul>

<h2>Installation</h2>

<ol style="text-align: left;">
    <li>Clone Repository:</li>
    <pre><code>git clone https://github.com/SDE-Ashik/stylen.git</code></pre>
    <li>Install Dependencies:</li>
    <pre><code>pip install -r requirements.txt</code></pre>
    <li>Set API Key:</li>
    <ul style="text-align: left;">
        <li>Obtain an API key from ClipDrop and replace 'your_api_key_here' in the code with your actual API key.</li>
    </ul>
    <li>Configure .env File:</li>
    <ul style="text-align: left;">
        <li>Create a .env file in the root directory of the project.</li>
        <li>Add your API key to the .env file using the following format:</li>
        <pre><code>API_KEY=your_api_key_here</code></pre>
    </ul>
</ol>

<h2>Usage</h2>

<ol style="text-align: left;">
    <li>Run Streamlit App:</li>
    <pre><code> streamlit run main_program.py
</code></pre>
    <li>Access App:</li>
    <ul style="text-align: left;">
        <li>Open the provided URL in your web browser to access the application.</li>
    </ul>
    <li>Generate Images:</li>
    <ul style="text-align: left;">
        <li>Upload images or provide text prompts to initiate style transfer and generate images.</li>
    </ul>
</ol>

<h2>Screenshots</h2>

<p style="text-align: center;">
    <img src="https://raw.githubusercontent.com/SDE-Ashik/stylen/master/v%202.5/MARK%205/3.png" alt="Uploaded Photos" width="800">
</p>

<p style="text-align: center;">
    <img src="https://raw.githubusercontent.com/SDE-Ashik/stylen/master/v%202.5/MARK%205/8.png" alt="Text Prompts" width="800">
</p>
<p style="text-align: center;">
    <img src="https://raw.githubusercontent.com/SDE-Ashik/stylen/master/v%202.5/MARK%205/5.png" alt="Text Prompts" width="800">
</p>
<p style="text-align: center;">
    <img src="https://raw.githubusercontent.com/SDE-Ashik/stylen/master/v%202.5/MARK%205/6.png" alt="Text Prompts" width="800">
</p>
<p style="text-align: center;">
    <img src="https://raw.githubusercontent.com/SDE-Ashik/stylen/master/v%202.5/MARK%205/7.png" alt="Text Prompts" width="800">
</p>

<h2>Contributing</h2>

<p style="text-align: left;">Contributions to improve the project are welcome. Please fork the repository and submit pull requests with your
    changes.</p>

<h2>License</h2>

<p style="text-align: left;">This project is licensed under the <a href="LICENSE">MIT License</a>.</p>
</body>
</html>
