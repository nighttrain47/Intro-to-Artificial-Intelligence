import streamlit as st
import pandas as pd
import pickle
import os
import sys

# Add the parent directory to the path so we can import utils
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)
from utils.text_processor import preprocess_text

# Set paths using absolute paths
models_dir = os.path.join(parent_dir, 'models')
model_path = os.path.join(models_dir, 'naive_bayes_model.pkl')
vectorizer_path = os.path.join(models_dir, 'count_vectorizer.pkl')

# Check if model files exist, if not, suggest running the training script
if not os.path.exists(model_path) or not os.path.exists(vectorizer_path):
    st.error("Model files not found. Please run the training script first:")
    st.code("python train_model.py")
    st.stop()

# Load the trained Naive Bayes model
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

# Load the CountVectorizer used for transforming input text
with open(vectorizer_path, 'rb') as vectorizer_file:
    count_vectorizer = pickle.load(vectorizer_file)

# Streamlit application title
st.title("Naive Bayes Text Classification")

# User input for text classification
user_input = st.text_area("Enter text for classification:")

if st.button("Classify"):
    if user_input:
        # Preprocess the input text
        processed_text = ' '.join(preprocess_text(user_input))
        
        # Transform the input text using the loaded CountVectorizer
        input_data = count_vectorizer.transform([processed_text])
        
        # Make prediction using the loaded model
        prediction = model.predict(input_data)
        
        # Display the classification result
        st.write("Classification Result:", prediction[0])
    else:
        st.write("Please enter some text for classification.")