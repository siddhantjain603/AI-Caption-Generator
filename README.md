# AI-Caption-Generator

## Overview

AI-Caption-Generator is a web application designed to generate Instagram-style captions for uploaded images. It leverages advanced machine learning models to:
- Analyze image content and generate descriptive captions.
- Enhance the captions with emojis and hashtags using OpenAI's GPT-3.5-turbo model.

## Files

- **`apikey.py`**: Contains the API key for OpenAI. Note: Replace the placeholder with your actual API key.
- **`caption_generator.py`**: Main script that integrates the image captioning model and OpenAI API. Handles image uploads and displays generated captions.
- **`online_module.py`**: Contains utility functions for setting up the OpenAI client and generating text.
- **`requirements.txt`**: Lists the Python dependencies required for the project.

## Setup

### 1. Clone the Repository

- git clone https://github.com/siddhantjain603/AI-Caption-Generator.git
- cd AI-Caption-Generator

### 2. Install Dependencies

- pip install -r requirements.txt

### 3. Configure API Key

- Open apikey.py.
- Replace the placeholder API key with your actual OpenAI API key.

### 4. Run the Application

- streamlit run caption_generator.py


## Usage

### 1. Upload an Image

- Click the "Choose a photo" button.
- Select an image file (supported formats: JPG, JPEG, PNG).

### 2. Generate Captions

- Click the "Generate Captions" button.
- The application will process the image and display the generated captions with emojis and hashtags.
