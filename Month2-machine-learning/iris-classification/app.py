import streamlit as st
import numpy as np
import pickle

with open(r"C:\Users\Prakash\Desktop\Ai_learning_journey\Month2-machine-learning\iris-classification\iris.pkl", "rb") as f:
    model = pickle.load(f)


st.title("Iris Flower Classification")

speal_length = st.slider("Sepal Length", 4.0, 7.0, 5.0)
speal_width = st.slider("Sepal Width", 2.0, 4.0, 3.0)
petal_length = st.slider("Petal Length", 1.0, 6.0, 2.0)
petal_width = st.slider("Petal Width", 0.0, 2.0, 1.0)

if st.button("Predict"):
    prediction = model.predict([[speal_length, speal_width, petal_length, petal_width]])
    Species = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
    st.success(f"The predicted species is: {Species[prediction[0]]}")