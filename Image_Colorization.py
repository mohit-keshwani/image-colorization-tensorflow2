# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 12:19:31 2020

@author: KIIT
"""

import tensorflow as tf
import keras 
import numpy as np
import os
import streamlit as st
import PIL
from PIL import Image 
import cv2
import time 
from keras.models import load_model
import tensorflow.keras.backend as K


st.markdown("<h1 style='test-align:center;'>Image Colorization</h1>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align:center;'> Built with Tensorflow2 and Keras</h3>", unsafe_allow_html=True)

st.text('2. Click  the nutton below to colorize your selected image')


gray=np.load('C:\\Users\\KIIT\\Downloads\\gray_scale.npy')

st.sidebar.title('1. Choose from 300 images')

i = st.sidebar.number_input(label = 'Énter a value:', min_value = 1 , value=1 , step=1)

def batch_prep(gray_img , batch_size = 100):
    img = np.zeros((batch_size , 224 , 224 , 3))
    for i in range(0,3):
        img[:batch_size, : , :,1] = gray_img[:batch_size]
    return img

img_in = batch_prep(gray, batch_size = 300)

st.sidebar.image(gray[i])

start_analyze_file = st.button('Colorize')
if start_analyze_file == True:
    
    with st.spinner(text = 'Colorizing...'):
        time.sleep(1)
        
    st.cache(allow_output_mutation = True)
    model = tf.keras.models.load_model('C:\\Users\\KIIT\\Downloads\\modelfinal.h5')
    prediction = model.predict(img_in)
    st.success('Done!')
    st.image(prediction[i].astype('uint8'), clamp = True)

del img_in

