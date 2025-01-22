import streamlit as st
import pytesseract
from PIL import Image
import os

# Set Tesseract executable path if required (uncomment and specify the path if needed)
# pytesseract.pytesseract.tesseract_cmd = r'/path/to/tesseract'

st.title('Upload your document')

# File uploader for JPG files
uploaded_file = st.file_uploader("Choose a file", type=['jpg'])

if uploaded_file is not None:
    # Save the uploaded image as image.jpg
    with open("image.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.success("File uploaded successfully and saved as image.jpg.")
    
    # Open the saved image
    image = Image.open("image.jpg")
    
    # Define custom Tesseract configuration
    myconfig = r"--oem 3 --psm 3"
    
    # Perform OCR using pytesseract
    text = pytesseract.image_to_string(image, config=myconfig)
    
    # Display the extracted text
    st.text_area("Extracted Text", text)

    # Optional: Show the uploaded image
    st.image(image, caption="Uploaded Image", use_container_width=True)
