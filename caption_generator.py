from online_module import * 
from apikey import apikey
from PIL import Image
from transformers import pipeline
import streamlit as st

st.markdown('<p class="title">Caption Generator</p>', unsafe_allow_html=True)

st.markdown(
    """
    <style>
        /* Style for title */
        .title {
            text-align: center !important;
            padding-bottom: 20px;
            color: white;
            font-size: 60px;
            font-weight: bold;
    </style>
    """,
    unsafe_allow_html=True
)

@st.cache_resource()
def load_model_pipeline(task, model_path, device="cuda"):
    model = pipeline(task, model=model_path, device=device)
    return model
 

model_path = ("/home/computervision/Desktop/siddhant/my_work/ai_4_every_1/caption_generator/models--Salesforce--blip-image-captioning-large/snapshots/2227ac38c9f16105cb0412e7cab4759978a8fd90")
 
model = load_model_pipeline('image-to-text', model_path)
client = setup_openai(apikey)
# File uploader with the unique key from session state
uploaded_image = st.file_uploader("Choose a photo", type=["jpg", "jpeg", "png"])
 
if st.button("Generate Captions"):
    with st.spinner('Generating Captions...'):
        col1, col2 = st.columns(2)
        with col1:
            st.image(uploaded_image, width=300)
        with col2:
            pil_image = Image.open(uploaded_image)
            semantics = model(images=pil_image)[0]['generated_text']
            # st.subheader("Semantics")
            # st.write(semantics)
            st.header("Captions")
            text_area_placeholder = st.empty()
 
            prompt = "Based on the image description, generate 3 captions for instagram" \
                     "Add Emojis and hashtags atleast 3 " \
                     "Here is the description " + semantics
 
            generate_text_openai_streamlit(client, prompt, text_area_placeholder,html=True)