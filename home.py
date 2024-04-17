import streamlit as st
from PIL import Image
import cv2

def app():
    st.markdown("<h1 style='color: blue;'>Welcome to the Home</h1>", unsafe_allow_html=True)
    st.write("In this site, you'll find the rate of the text.")
    st.write("Like!!!!!......")
    
   
    img_pil = Image.open("display.png")

    
    

    
    st.image(img_pil, caption="(for your understanding)", use_column_width=True)

    
   


