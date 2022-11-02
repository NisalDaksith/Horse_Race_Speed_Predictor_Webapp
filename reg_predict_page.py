import streamlit as st 
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

def load_model():
    
    with open('speed_predictor.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

linearReg = data["model"]
htype = data["horse_type"]
config = data["config"]

def show_predict_page():
    st.title("Horse Speed Predictor")
    st.sidebar.write("""### First we need some information about your horse and the Track""")
    
    horse_type = ("Gelding","Brown","Horse","Mare","Colt","Steed","Mount")
    track_config = ("A","B","B+2","C","C+3")
    horse_age = ([2,3,4,5,6,7,8])
    surface = ([0,1])
    
    horse_type = st.sidebar.selectbox("Type of your Horse ",horse_type)
    track_config = st.sidebar.selectbox("Configuration of the Track ",track_config)
    horse_age = st.sidebar.selectbox("Age of the Horse ",horse_age)
    surface = st.sidebar.selectbox("Type of the Surface( 0 = Dirt , 1 = Turf ) ",surface)
    horse_weight = st.sidebar.slider("Weight of the Horse ",0,1200)                #Could be problematic 
    rider_weight = st.sidebar.slider("Weight of the Rider ",0,150)                 #Could be problematic
    
    
    ######################################################################################################
    ok = st.sidebar.button("Predict Speed")
    if ok:
        X = np.array([[horse_type,track_config,horse_age,horse_weight,rider_weight,surface]])
        X[:,0] = htype.transform(X[:,0])
        X[:,1] = config.transform(X[:,1])
    
        X = X.astype(float)
    #######################################################################################################    
        horse_speed = linearReg.predict(X)
        st.sidebar.subheader(f"The Horse will run at {horse_speed[0]:.4f} meters per second.")
    