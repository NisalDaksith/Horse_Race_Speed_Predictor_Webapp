import streamlit as st 
import pickle
import numpy as np

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
    st.write("""### First we need some information about your horse and the Track""")
    
    horse_type = ("Gelding","Brown","Horse","Mare","Colt","Steed","Mount")
    config = ("A","B","B+2","C","C+3")
    horse_age = ("2","3","4","5","6","7","8")

    horse_type = st.selectbox("Type of your Horse: ",horse_type)
    config = st.selectbox("Configuration of the Track: ",config)
    horse_age = st.selectbox("Age of the Horse: ",)
