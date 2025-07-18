import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler

def preprocess_data(input_data):
    # Convert input data to DataFrame
    df = pd.DataFrame(input_data, index=[0])
    
    # One-hot encode categorical variables
    encoder = OneHotEncoder(sparse=False, drop='first')
    categorical_cols = ['Sex', 'BP', 'Cholesterol']
    encoded_cats = encoder.fit_transform(df[categorical_cols])
    
    # Create a DataFrame for the encoded categorical variables
    encoded_df = pd.DataFrame(encoded_cats, columns=encoder.get_feature_names_out(categorical_cols))
    
    # Drop original categorical columns and concatenate with encoded columns
    df = df.drop(categorical_cols, axis=1)
    df = pd.concat([df.reset_index(drop=True), encoded_df.reset_index(drop=True)], axis=1)
    
    # Scale numerical features
    scaler = StandardScaler()
    numerical_cols = ['Age', 'Na_to_K']
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])
    
    return df