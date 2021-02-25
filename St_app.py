import streamlit as ST
import pickle
import numpy as np
from PIL import Image

ST.sidebar.title("Diabetes Predictor")
image=Image.open("Application_Logo.png")
ST.image(image,use_column_width=True)


filename = 'diabetes-prediction-rfc-model.pkl'
classifier = pickle.load(open(filename, 'rb'))




preg=ST.number_input("Number of Pregnancies: eg. 0",min_value=0,value=0,step=1,format="%d")
glucose=ST.number_input("Glucose (mg/DL): eg. 80",min_value=0,value=0,step=1,format="%d")
bp=ST.number_input("Blood Pressure (mmHg): eg. 80",min_value=0,value=0,step=1,format="%d")
st=ST.number_input("Skin Thickness (mm): eg. 20",min_value=0,value=0,step=1,format="%d")
insulin=ST.number_input("Insulin Level (IU/mL): eg. 80",min_value=0,value=0,step=1,format="%d")
bmi=ST.number_input("Body Mass Index (kg/m²): eg. 24.1")
dpf=ST.number_input("Diabetes Pedigree Function: eg. 0.52")
age=ST.number_input("Age (years): eg. 40",min_value=0,value=0,step=1,format="%d")




data = np.array([[preg, glucose, bp, st, insulin, bmi, dpf, age]])
my_prediction = classifier.predict(data)
if ST.button("Predict"):
    if my_prediction==1:
        ST.info("OOPS! you have diabetes")
        image=Image.open("Diabetes_Sad.png")
        ST.image(image,use_column_width=True)
        
    else:
        ST.info("Great! you don't have diabetes")
        image=Image.open("No_Diabetes_Happy.png")
        ST.image(image,use_column_width=True)


