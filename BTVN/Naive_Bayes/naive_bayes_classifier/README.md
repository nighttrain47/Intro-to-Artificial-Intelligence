# Naive Bayes Classifier

This project implements a Naive Bayes classification model using a dataset of educational text samples. The model is trained to classify text as either positive or negative based on the content.

## Project Structure

```
naive_bayes_classifier
├── app
│   └── exercise1web.py        # Streamlit web application for text classification
├── data
│   └── Education.csv          # Dataset used for training the model
├── models
│   └── naive_bayes_model.pkl   # Serialized Naive Bayes model
├── utils
│   ├── __init__.py            # Initialization file for utils package
│   └── text_processor.py       # Utility functions for text processing
├── requirements.txt            # List of dependencies
└── README.md                   # Project documentation
```

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd naive_bayes_classifier
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the Streamlit web application, execute the following command in your terminal:

1.	First, run the training script to create the model files:
```
python train_model.py
```

2.	Then, run the Streamlit app:
```
streamlit run app/exercise1web.py
```

This will start the Streamlit server and open the application in your default web browser.

## Usage

1. Enter the text you want to classify in the input box.
2. Click the "Submit" button to see the classification result.
3. The application will display whether the input text is classified as "positive" or "negative".

## Model Training

The model is trained using the dataset located in the `data/Education.csv` file. The trained model is saved as a serialized object in `models/naive_bayes_model.pkl`.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.