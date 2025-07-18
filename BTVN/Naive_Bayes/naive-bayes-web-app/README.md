# Naive Bayes Web Application

This project is a Streamlit web application that implements a Naive Bayes classification model to predict drug prescriptions based on user input features. The application allows users to input their data and receive predictions based on the trained model.

## Project Structure

```
naive-bayes-web-app
├── app.py                # Main entry point of the Streamlit application
├── data
│   └── drug200.csv      # Dataset used for training the Naive Bayes model
├── models
│   └── model.py         # Implementation of the Naive Bayes classification model
├── utils
│   └── preprocessing.py  # Utility functions for data preprocessing
├── requirements.txt      # List of dependencies for the project
└── README.md             # Documentation for the project
```

## Installation

To run this application, you need to have Python installed on your machine. Follow these steps to set up the project:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd naive-bayes-web-app
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To start the Streamlit web application, run the following command in your terminal:
```
streamlit run app.py
```

This will launch the application in your default web browser.

## Usage

1. Input the required features such as Age, Sex, BP, Cholesterol, and Na_to_K in the provided fields.
2. Click on the "Submit" button to get the predicted drug prescription.
3. The results will be displayed on the screen.

## Features

- User-friendly interface for inputting data.
- Real-time predictions based on the Naive Bayes classification model.
- Visualization of results.

## Acknowledgments

This project utilizes the Naive Bayes algorithm for classification tasks and is built using Streamlit for creating interactive web applications.