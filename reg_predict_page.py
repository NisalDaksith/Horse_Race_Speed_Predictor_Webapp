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