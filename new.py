import streamlit as st
import pytesseract
from PIL import Image
import os


st.title('Upload your document')


uploaded_file = st.file_uploader("Choose a file", type=['jpg'])

if uploaded_file is not None:
    # Save the uploaded image as image.jpg
    with open("image.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.success("File uploaded successfully and saved as image.jpg.")
    

    image = Image.open("image.jpg")
    
    
    myconfig = r"--oem 3 --psm 3"

    text = pytesseract.image_to_string(image, config=myconfig)
    
    
    st.text_area("Extracted Text", text)


    st.image(image, caption="Uploaded Image", use_container_width=True)
