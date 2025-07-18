import streamlit as st
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

# Load the dataset
data = pd.read_csv('data/drug200.csv')

# Preprocessing
X = data.drop(['Drug'], axis=1)
y = data['Drug']

# One-hot encoding for categorical variables
categorical_features = ['Sex', 'BP', 'Cholesterol']
numeric_features = ['Age', 'Na_to_K']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', 'passthrough', numeric_features),
        ('cat', OneHotEncoder(), categorical_features)
    ])

# Create a pipeline for the model
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', GaussianNB())
])

# Train the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'models/naive_bayes_model.pkl')

# Streamlit app
st.title('Naive Bayes Drug Classification')

# User input
age = st.number_input('Age', min_value=0, max_value=120, value=25)
sex = st.selectbox('Sex', options=['F', 'M'])
bp = st.selectbox('Blood Pressure', options=['LOW', 'NORMAL', 'HIGH'])
cholesterol = st.selectbox('Cholesterol', options=['NORMAL', 'HIGH'])
na_to_k = st.number_input('Na_to_K', value=15.0)

# Create a DataFrame for the input
input_data = pd.DataFrame({
    'Age': [age],
    'Sex': [sex],
    'BP': [bp],
    'Cholesterol': [cholesterol],
    'Na_to_K': [na_to_k]
})

# Make prediction
if st.button('Predict'):
    prediction = model.predict(input_data)
    st.write(f'The predicted drug is: {prediction[0]}')