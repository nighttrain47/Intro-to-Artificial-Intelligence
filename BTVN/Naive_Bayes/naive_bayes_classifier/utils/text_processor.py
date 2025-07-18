import re
import string

def clean_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    text = text.strip()  # Remove leading and trailing whitespace
    return text

def tokenize(text):
    return text.split()  # Simple whitespace tokenization

def preprocess_text(text):
    cleaned_text = clean_text(text)
    tokens = tokenize(cleaned_text)
    return tokens