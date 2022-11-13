import streamlit as st
import cv2 #for image processing
import numpy as np #to store image
import imageio #to read image stored at particular path
import sys
import matplotlib.pyplot as plt
import os
from PIL import Image

def cartoonify(ImagePath):
   
    originalmage = cv2.cvtColor(ImagePath, cv2.COLOR_BGR2RGB)

    if option == 'Pencil Sketch':     
        value = st.sidebar.slider('Tune the brightness of your sketch (the higher the value, the brighter your sketch)', 0.0, 300.0, 250.0)
        kernel = st.sidebar.slider('Tune the boldness of the edges of your sketch (the higher the value, the bolder the edges)', 1, 99, 25, step=2)
        gray_blur = cv2.GaussianBlur(originalmage, (kernel, kernel), 0)
        cartoon = cv2.divide(originalmage, gray_blur, scale=value)
            
    return cartoon

    
def main():
    st.title("Cartoonify Your Image!")
    html_temp = """
    <div style="background-color:teal ;padding:10px">
    <h2 style="color:white;text-align:center;">Iris Classification</h2>
    </div>
    """
    
    file = st.file_uploader("Upload a PNG/JPG image file:", type=["jpg", "png"])
    
    if file is None:
        st.text("You haven't uploaded a valid image file yet.")
    
    else:
        IMG = Image.open(file)
        image = np.array(IMG)        
        C = cartoonify(image)
        st.image(C, use_column_width=True)
           
         


if __name__=='__main__':
    main()
