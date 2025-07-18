from sklearn.naive_bayes import GaussianNB
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler

class NaiveBayesModel:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)
        self.model = GaussianNB()
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

    def preprocess_data(self):
        X = self.data.drop(['Drug'], axis=1)
        y = self.data['Drug']
        
        # One-hot encoding for categorical variables
        encoder = OneHotEncoder(sparse=False)
        X_encoded = encoder.fit_transform(X[['Sex', 'BP', 'Cholesterol']])
        
        # Scaling numerical features
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X[['Age', 'Na_to_K']])
        
        # Combine processed features
        X_processed = pd.concat([pd.DataFrame(X_encoded), pd.DataFrame(X_scaled)], axis=1)
        
        # Split the data into training and testing sets
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X_processed, y, test_size=0.3, random_state=0)

    def train_model(self):
        self.model.fit(self.X_train, self.y_train)

    def predict(self, input_data):
        return self.model.predict(input_data)