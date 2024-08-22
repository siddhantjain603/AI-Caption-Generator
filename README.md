# AI-Caption-Generator

Overview
This project is a web application that generates Instagram captions for uploaded images using OpenAI's GPT-3.5-turbo model and a BLIP image captioning model. Built with Streamlit, this app allows users to upload images, generates captions based on image content, and enhances these captions with emojis and hashtags.

Files
apikey.py: Contains the API key for OpenAI. Note: The provided key is a placeholder and should be replaced with a valid key.

caption_generator.py: The main script that integrates the image captioning model and OpenAI API. It handles image uploads and displays generated captions.

online_module.py: Contains utility functions for setting up the OpenAI client and generating text with the OpenAI API.

requirements.txt: Lists the dependencies required for the project.

Setup
Clone the Repository

bash
Copy code
git clone https://github.com/yourusername/caption-generator.git
cd caption-generator
Install Dependencies

Ensure you have pip installed and run the following command to install the required packages:

bash
Copy code
pip install -r requirements.txt
Configure API Key

Open apikey.py and replace the placeholder API key with your actual OpenAI API key.
Run the Application

Use Streamlit to run the application:

bash
Copy code
streamlit run caption_generator.py
Usage
Upload an Image

Click on the "Choose a photo" button to upload an image file (supported formats: JPG, JPEG, PNG).

Generate Captions

Click the "Generate Captions" button. The application will process the image and display the generated captions, including emojis and hashtags, on the right side of the page.

Components
caption_generator.py: Main script for handling user interactions and generating captions.
online_module.py: Includes functions to set up OpenAI and generate text based on image descriptions.
requirements.txt: Dependency list for the project.
Dependencies
streamlit
transformers
Pillow
openai
