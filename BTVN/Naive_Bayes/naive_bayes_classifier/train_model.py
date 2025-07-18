import os
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from utils.text_processor import preprocess_text

# Set paths
current_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(current_dir, 'data', 'Education.csv')
models_dir = os.path.join(current_dir, 'models')

# Create models directory if it doesn't exist
if not os.path.exists(models_dir):
    os.makedirs(models_dir)

# Load the dataset
df = pd.read_csv(data_path)

# Preprocess the text
df['Processed_Text'] = df['Text'].apply(lambda x: ' '.join(preprocess_text(x)))

# Create features and target
X = df['Processed_Text']
y = df['Label']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the CountVectorizer
count_vectorizer = CountVectorizer()
X_train_counts = count_vectorizer.fit_transform(X_train)

# Train the Naive Bayes model
nb_model = MultinomialNB()
nb_model.fit(X_train_counts, y_train)

# Save the model and vectorizer
model_path = os.path.join(models_dir, 'naive_bayes_model.pkl')
vectorizer_path = os.path.join(models_dir, 'count_vectorizer.pkl')

with open(model_path, 'wb') as file:
    pickle.dump(nb_model, file)

with open(vectorizer_path, 'wb') as file:
    pickle.dump(count_vectorizer, file)

print(f"Model saved to {model_path}")
print(f"Vectorizer saved to {vectorizer_path}")

# Evaluate the model
X_test_counts = count_vectorizer.transform(X_test)
accuracy = nb_model.score(X_test_counts, y_test)
print(f"Model accuracy: {accuracy:.2f}")
