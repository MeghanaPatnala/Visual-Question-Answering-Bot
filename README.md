# Visual Question Answering (VQA) Bot

🚀 Introduction

This project is a Visual Question Answering (VQA) Bot built using Streamlit and Hugging Face's BLIP model. The bot allows users to upload an image, ask a question about it, and receive an AI-generated answer.

📌 Features

✅ Upload an image (.jpg, .jpeg, .png)
✅ Ask a question about the image
✅ Generate multiple answers
✅ Simple & interactive UI using Streamlit

📂 Project Structure

🛠️ Step-by-Step Guide

1️⃣ Install Required Libraries

Ensure Python is installed on your system. Then, install the necessary dependencies:

2️⃣ Set Up the Streamlit App

Create a new Python file (vbot.py).

Import essential libraries: Streamlit, PIL, Transformers, Torch.

Load the BLIP VQA model for image-based question answering.

3️⃣ Build the User Interface (UI)

Use Streamlit to create a web-based interface.

Add an image uploader so users can upload an image.

Provide a text box where users can enter a question.

Include a number input to specify how many answers they want.

4️⃣ Process the Image and Question

Convert the uploaded image to a format that the model can process.

Send the image and question to the BLIP model.

Generate one or more possible answers.

5️⃣ Display the Results

Show the uploaded image to the user.

Display the generated answer(s) in a readable format.

6️⃣ Run the App Locally

Open a terminal, navigate to the project folder, and run:

Run the following command:

# streamlit run vbot.py

The app will open in a web browser, allowing users to interact with it.


# after uploading app will be look like below:
![image](https://github.com/user-attachments/assets/b0591627-61a1-4c6e-9116-1b72bfbaa972)
![image](https://github.com/user-attachments/assets/2dbc388a-495f-41c5-b27a-d6228507a510)


