import streamlit as st
import cv2 #for image processing
import numpy as np #to store image
import imageio #to read image stored at particular path
import sys
import matplotlib.pyplot as plt
import os
from PIL import Image

    
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
        
        opt = st.sidebar.selectbox('Which cartoon filters would you like to apply?',
    ('Pencil Sketch', 'Detail Enhancement'))
        
        cartoon = cartoonify(image,opt)
        st.image(cartoon, use_column_width=True)
           
            
def cartoonify(ImagePath, option):
    
    originalmage = cv2.cvtColor(ImagePath, cv2.COLOR_BGR2RGB)

    if option == 'Pencil Sketch':     
        value = st.sidebar.slider('Tune the brightness of your sketch (the higher the value, the brighter your sketch)', 0.0, 300.0, 250.0)
        kernel = st.sidebar.slider('Tune the boldness of the edges of your sketch (the higher the value, the bolder the edges)', 1, 99, 25, step=2)
        gray_blur = cv2.GaussianBlur(originalmage, (kernel, kernel), 0)
        cartoon = cv2.divide(originalmage, gray_blur, scale=value)
        
    elif option == 'Detail Enhancement': 
        smooth = st.sidebar.slider('Tune the smoothness level of the image (the higher the value, the smoother the image)', 3, 99, 5, step=2)
        kernel = st.sidebar.slider('Tune the sharpness of the image (the lower the value, the sharper it is)', 1, 21, 3, step =2)
        edge_preserve = st.sidebar.slider('Tune the color averaging effects (low: only similar colors will be smoothed, high: dissimilar color will be smoothed)', 0.0, 1.0, 0.5)
    
        gray = cv2.medianBlur(originalmage, kernel) 
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9) 
    
        color = cv2.detailEnhance(originalmage, sigma_s=smooth, sigma_r=edge_preserve)
        cartoon = cv2.bitwise_and(color, color, mask=edges) 
        
        
    return cartoon


if __name__=='__main__':
    main()
