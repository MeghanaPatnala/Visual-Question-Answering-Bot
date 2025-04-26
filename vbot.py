import streamlit as st
from PIL import Image
import requests
from transformers import BlipProcessor, BlipForQuestionAnswering
import torch

# Load the processor and model
.............
# Streamlit app
st.title("Visual Question Answering")

# Image upload
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.write("")

    # Question input
    question = st.text_input("Ask a question about the image:")

    # Number of answers input
    num_answers = st.number_input("Number of answers to generate:", min_value=1, max_value=10, value=1)

    # Submit button
    if st.button("Submit"):
        if question:
            with st.spinner("Analyzing..."):
                device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
                inputs = processor(image, question, return_tensors="pt").to(device)
                out = model.generate(
                    **inputs,
                    num_return_sequences=num_answers,
                    num_beams=num_answers
                )
                answers = [processor.decode(output, skip_special_tokens=True) for output in out]
            st.success(f"Answers: {answers}")
        else:
            st.error("Please enter a question.")
