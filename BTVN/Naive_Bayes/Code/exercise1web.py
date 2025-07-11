import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, auc

# Set page title and description
st.set_page_config(page_title="Naive Bayes Text Classification", layout="wide")
st.title("Naive Bayes Text Classification")
st.markdown("This app demonstrates text classification using Naive Bayes algorithms.")

# Function to split data into train and test sets
@st.cache_data
def split_train_test(data, ratio_test, random_seed=0):
    np.random.seed(random_seed)
    index_permu = np.random.permutation(len(data))
    data_permu = data.iloc[index_permu]
    test_size = int(len(data_permu)*ratio_test)
    train_set = data_permu.iloc[:-test_size]
    test_set = data_permu.iloc[-test_size:]
    return train_set, test_set

# Function to train model and evaluate
def train_and_evaluate(X_train, y_train, X_test, y_test, model_type="bernoulli", binary=True):
    # Ensure text data is properly formatted
    # Convert to string and replace NaN values with empty string
    X_train = X_train.astype(str).replace('nan', '')
    X_test = X_test.astype(str).replace('nan', '')
    
    # Check if there's valid text data to process
    if X_train.str.strip().eq('').all():
        st.error("Error: Text column contains only empty strings.")
        return None
    
    # Create vectorizer
    count_vect = CountVectorizer(binary=binary, stop_words='english')
    
    try:
        # Fit and transform training data
        X_train_transformed = count_vect.fit_transform(X_train)
        # Transform test data
        X_test_transformed = count_vect.transform(X_test)
        
        # Check if any features were extracted
        if X_train_transformed.shape[1] == 0:
            st.error("No features were extracted from the text. Check your data.")
            return None
        
        # Train model
        if model_type == "bernoulli":
            model = BernoulliNB()
        else:
            model = MultinomialNB()
        
        model.fit(X_train_transformed, y_train)
        
        # Predictions
        y_pred = model.predict(X_test_transformed)
        y_pred_proba = model.predict_proba(X_test_transformed)
        
        # Identify positive and negative classes
        # Check various common formats for positive/negative labels
        positive_class = None
        negative_class = None
        
        # Check if labels are already numeric (0, 1)
        if pd.api.types.is_numeric_dtype(y_train):
            unique_values = sorted(y_train.unique())
            # Assuming binary classification with higher value = positive
            if len(unique_values) == 2:
                negative_class, positive_class = unique_values
        # Check if labels are strings like 'positive'/'negative'
        elif all(label.lower() in ['positive', 'negative', 'pos', 'neg'] for label in y_train.astype(str).unique()):
            # Map variations of positive labels
            pos_variations = ['positive', 'pos']
            neg_variations = ['negative', 'neg']
            for label in y_train.astype(str).unique():
                if label.lower() in pos_variations:
                    positive_class = label
                elif label.lower() in neg_variations:
                    negative_class = label
        
        # If positive/negative classes were identified
        if positive_class is not None and negative_class is not None:
            # Create a mapping of model's numeric classes to labels
            class_mapping = {
                0 if model.classes_[0] == negative_class else 1: "negative",
                1 if model.classes_[1] == positive_class else 0: "positive"
            }
            # Convert predictions to labels
            y_pred_labels = np.array([class_mapping[p] for p in y_pred])
        else:
            # Just use the raw predictions if not a standard positive/negative classification
            y_pred_labels = y_pred
        
        # Extract most important features for each class
        feature_names = count_vect.get_feature_names_out()
        # Get feature importance scores (log probabilities) for each class
        feature_importance = {}
        
        # Only extract if we have a binary classification
        if len(model.classes_) == 2:
            # For each class, get top features
            for i, class_label in enumerate(model.classes_):
                # Get feature log probabilities for this class
                log_probs = model.feature_log_prob_[i]
                # Sort by importance (highest log probability)
                sorted_idx = np.argsort(log_probs)[::-1]
                # Get top 10 features and their scores
                top_features = [(feature_names[idx], log_probs[idx]) for idx in sorted_idx[:10]]
                feature_importance[f"class_{i}"] = top_features
        
        return {
            "model": model,
            "vectorizer": count_vect,
            "predictions": y_pred,
            "prediction_labels": y_pred_labels,
            "probabilities": y_pred_proba,
            "features": feature_names,
            "positive_class": positive_class,
            "negative_class": negative_class,
            "top_features": feature_importance,
            "class_mapping": model.classes_
        }
    except Exception as e:
        st.error(f"Error during text processing: {str(e)}")
        return None

def calculate_metrics(y_true, y_pred):
    # Confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    
    # Basic metrics
    if len(cm) == 2:  # Binary classification
        TN, FP, FN, TP = cm.ravel()
        accuracy = (TP + TN) / (TP + TN + FP + FN)
        precision = TP / (TP + FP) if (TP + FP) > 0 else 0
        recall = TP / (TP + FN) if (TP + FN) > 0 else 0
        f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    else:
        # For multiclass, use macro average from classification report
        report = classification_report(y_true, y_pred, output_dict=True)
        accuracy = report['accuracy']
        precision = report['macro avg']['precision']
        recall = report['macro avg']['recall']
        f1 = report['macro avg']['f1-score']
        
    return {
        "confusion_matrix": cm,
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1
    }

def plot_roc_curve(y_test, y_pred_proba, pos_label='positive'):
    # Check if probabilities are provided for binary classification
    if y_pred_proba.shape[1] == 2:
        fpr, tpr, _ = roc_curve(y_test, y_pred_proba[:, 1], pos_label=pos_label)
        roc_auc = auc(fpr, tpr)
        
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.plot(fpr, tpr, color='blue', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
        ax.plot([0, 1], [0, 1], color='gray', linestyle='--')
        ax.set_xlim([0.0, 1.0])
        ax.set_ylim([0.0, 1.05])
        ax.set_xlabel('False Positive Rate')
        ax.set_ylabel('True Positive Rate')
        ax.set_title('Receiver Operating Characteristic')
        ax.legend(loc="lower right")
        
        return fig, roc_auc
    else:
        return None, None

# Main app
def main():
    # Sidebar controls
    st.sidebar.header("Settings")
    
    try:
        # Load data
        with st.sidebar.expander("Data Options", expanded=True):
            uploaded_file = st.file_uploader("Upload your CSV file (or use default)", type=["csv"])
            
            if uploaded_file is not None:
                data = pd.read_csv(uploaded_file)
                st.success("Custom dataset loaded!")
            else:
                try:
                    data = pd.read_csv('Education.csv')
                    st.info("Using default 'Education.csv' dataset")
                except FileNotFoundError:
                    st.error("Default dataset 'Education.csv' not found. Please upload a file.")
                    return
            
            # Display data sample
            if st.checkbox("Show raw data sample"):
                st.write(data.head())
            
            # Column selection
            text_col = st.selectbox("Select text column:", data.columns)
            label_col = st.selectbox("Select label column:", data.columns)
            
        # Model parameters - update to add dual model comparison option
        with st.sidebar.expander("Model Parameters", expanded=True):
            test_ratio = st.slider("Test set ratio:", 0.1, 0.5, 0.2, 0.05)
            random_seed = st.number_input("Random seed:", 0, 100, 0)
            
            # Add a checkbox for dual model comparison
            dual_model = st.checkbox("Enable dual model comparison", value=True, 
                                    help="Train both Bernoulli and Multinomial models for comparison")
            
            # If not dual model, show model type selector
            if not dual_model:
                model_type = st.selectbox("Naive Bayes model type:", ["bernoulli", "multinomial"])
                binary_features = st.checkbox("Use binary features", value=True if model_type=="bernoulli" else False)
            else:
                # For dual model, just show binary features option for Bernoulli
                st.write("Both models will be trained for comparison")
                binary_features = st.checkbox("Use binary features for Bernoulli", value=True)
            
            if st.sidebar.button("Train Model"):
                with st.spinner("Training model..."):
                    # Split data
                    train_set, test_set = split_train_test(data, test_ratio, random_seed)
                    train_set.reset_index(drop=True, inplace=True)
                    test_set.reset_index(drop=True, inplace=True)
                    
                    # Store train and test sets in session state so they're available later
                    st.session_state.train_set = train_set
                    st.session_state.test_set = test_set
                    
                    # Prepare data
                    X_train, y_train = train_set[text_col], train_set[label_col]
                    X_test, y_test = test_set[text_col], test_set[label_col]
                    
                    # Display dataset stats before training
                    st.info(f"Training set: {len(X_train)} samples, Test set: {len(X_test)} samples")
                    
                    # Check for missing values
                    train_missing = X_train.isna().sum()
                    test_missing = X_test.isna().sum()
                    
                    if train_missing > 0 or test_missing > 0:
                        st.warning(f"Found {train_missing} missing values in training text and {test_missing} in test text. These will be treated as empty strings.")
                    
                    # Check if labels are already encoded
                    if y_train.dtype == 'object' and set(y_train.unique()) == {'positive', 'negative'}:
                        y_train = y_train.map({"positive": 1, "negative": 0})
                    
                    # Train models
                    if dual_model:
                        # Train both models
                        bernoulli_results = train_and_evaluate(X_train, y_train, X_test, y_test, "bernoulli", True)
                        multinomial_results = train_and_evaluate(X_train, y_train, X_test, y_test, "multinomial", False)
                        
                        if bernoulli_results and multinomial_results:
                            # Calculate metrics for both models
                            bernoulli_metrics = calculate_metrics(y_test, bernoulli_results["prediction_labels"])
                            multinomial_metrics = calculate_metrics(y_test, multinomial_results["prediction_labels"])
                            
                            # Store in session state
                            st.session_state.bernoulli_results = bernoulli_results
                            st.session_state.bernoulli_metrics = bernoulli_metrics
                            st.session_state.multinomial_results = multinomial_results
                            st.session_state.multinomial_metrics = multinomial_metrics
                            st.session_state.y_test = y_test
                            st.session_state.test_set = test_set
                            st.session_state.dual_model_trained = True
                            st.success("Both models trained successfully!")
                        else:
                            st.error("Model training failed. Please check your data and try again.")
                    else:
                        # Train single model (original code)
                        results = train_and_evaluate(X_train, y_train, X_test, y_test, model_type, binary_features)
                        
                        if results:
                            metrics = calculate_metrics(y_test, results["prediction_labels"])
                            st.session_state.results = results
                            st.session_state.metrics = metrics
                            st.session_state.y_test = y_test
                            st.session_state.test_set = test_set
                            st.session_state.model_trained = True
                            st.success("Model training completed successfully!")
                        else:
                            st.error("Model training failed. Please check your data and try again.")

        # Show results for dual model comparison
        if 'dual_model_trained' in st.session_state and st.session_state.dual_model_trained:
            st.header("Model Comparison Results")
            
            # Dataset info
            st.subheader("Dataset Information")
            col1, col2 = st.columns(2)
            with col1:
                # Use session state to access train_set and test_set
                st.write(f"Training set size: {len(st.session_state.train_set)}")
                st.write(f"Test set size: {len(st.session_state.test_set)}")
                
                # Class distribution
                st.subheader("Class Distribution")
                train_dist = pd.DataFrame(st.session_state.train_set[label_col].value_counts()).transpose()
                test_dist = pd.DataFrame(st.session_state.test_set[label_col].value_counts()).transpose()
                st.write("Training set:", train_dist)
                st.write("Test set:", test_dist)
            
            # Metrics comparison
            st.header("Performance Metrics Comparison")
            
            # Create a dataframe to compare metrics
            comparison_data = {
                "Metric": ["Accuracy", "Precision", "Recall", "F1 Score"],
                "Bernoulli NB": [
                    f"{st.session_state.bernoulli_metrics['accuracy']:.4f}",
                    f"{st.session_state.bernoulli_metrics['precision']:.4f}",
                    f"{st.session_state.bernoulli_metrics['recall']:.4f}",
                    f"{st.session_state.bernoulli_metrics['f1']:.4f}"
                ],
                "Multinomial NB": [
                    f"{st.session_state.multinomial_metrics['accuracy']:.4f}",
                    f"{st.session_state.multinomial_metrics['precision']:.4f}",
                    f"{st.session_state.multinomial_metrics['recall']:.4f}",
                    f"{st.session_state.multinomial_metrics['f1']:.4f}"
                ]
            }
            comparison_df = pd.DataFrame(comparison_data)
            st.table(comparison_df)
            
            # Confusion Matrices
            st.subheader("Confusion Matrices")
            col1, col2 = st.columns(2)
            with col1:
                st.write("Bernoulli NB")
                st.write(st.session_state.bernoulli_metrics['confusion_matrix'])
            
            with col2:
                st.write("Multinomial NB")
                st.write(st.session_state.multinomial_metrics['confusion_matrix'])
            
            # Custom text prediction for both models
            st.header("Test Your Own Text")
            st.write("""
            **Examples of negative phrases based on the dataset:**
            - "Standardized tests fail to capture students' abilities and create unnecessary stress."
            - "Budget cuts in education lead to larger class sizes and fewer resources."
            - "Privatization and charter schools drain resources from public education."
            """)
            
            user_text = st.text_area("Enter text to classify:")
            if st.button("Classify") and user_text:
                col1, col2 = st.columns(2)
                
                # Bernoulli prediction
                with col1:
                    st.subheader("Bernoulli NB Prediction")
                    # Vectorize and predict
                    user_vector = st.session_state.bernoulli_results['vectorizer'].transform([user_text])
                    user_pred_bernoulli = st.session_state.bernoulli_results['model'].predict(user_vector)[0]
                    user_proba_bernoulli = st.session_state.bernoulli_results['model'].predict_proba(user_vector)[0]
                    
                    # Display result with clearer confidence thresholds
                    if user_pred_bernoulli == 0:
                        bernoulli_pred_label = "Negative"
                        pred_prob = f"{user_proba_bernoulli[0]:.2%}"
                        # Use color intensity based on confidence
                        confidence = user_proba_bernoulli[0]
                        if confidence < 0.6:
                            pred_color = "#ffcccc"  # Light red for low confidence
                            confidence_message = "⚠️ Low confidence prediction"
                        else:
                            pred_color = "red"
                            confidence_message = "✓ High confidence prediction"
                    else:
                        bernoulli_pred_label = "Positive"
                        pred_prob = f"{user_proba_bernoulli[1]:.2%}"
                        # Use color intensity based on confidence
                        confidence = user_proba_bernoulli[1]
                        if confidence < 0.6:
                            pred_color = "#ccffcc"  # Light green for low confidence
                            confidence_message = "⚠️ Low confidence prediction"
                        else:
                            pred_color = "green"
                            confidence_message = "✓ High confidence prediction"
                    
                    # Store the prediction label for comparison
                    st.session_state.bernoulli_pred_label = bernoulli_pred_label
                    
                    # Display prediction with color and confidence indicator
                    st.markdown(f"<h3 style='color:{pred_color}'>Prediction: {bernoulli_pred_label}</h3>", unsafe_allow_html=True)
                    st.write(f"Confidence: {pred_prob}")
                    st.write(confidence_message)
                    
                    # Show probabilities as bar chart
                    probs_df = pd.DataFrame({
                        'Class': ['Negative', 'Positive'],
                        'Probability': [user_proba_bernoulli[0], user_proba_bernoulli[1]]
                    })
                    st.bar_chart(probs_df.set_index('Class'))
                
                # Multinomial prediction - Similar changes
                with col2:
                    st.subheader("Multinomial NB Prediction")
                    # Vectorize and predict
                    user_vector = st.session_state.multinomial_results['vectorizer'].transform([user_text])
                    user_pred_multinomial = st.session_state.multinomial_results['model'].predict(user_vector)[0]
                    user_proba_multinomial = st.session_state.multinomial_results['model'].predict_proba(user_vector)[0]
                    
                    # Display result with clearer confidence thresholds
                    if user_pred_multinomial == 0:
                        multinomial_pred_label = "Negative"
                        pred_prob = f"{user_proba_multinomial[0]:.2%}"
                        # Use color intensity based on confidence
                        confidence = user_proba_multinomial[0]
                        if confidence < 0.6:
                            pred_color = "#ffcccc"  # Light red for low confidence
                            confidence_message = "⚠️ Low confidence prediction"
                        else:
                            pred_color = "red"
                            confidence_message = "✓ High confidence prediction"
                    else:
                        multinomial_pred_label = "Positive"
                        pred_prob = f"{user_proba_multinomial[1]:.2%}"
                        # Use color intensity based on confidence
                        confidence = user_proba_multinomial[1]
                        if confidence < 0.6:
                            pred_color = "#ccffcc"  # Light green for low confidence
                            confidence_message = "⚠️ Low confidence prediction"
                        else:
                            pred_color = "green"
                            confidence_message = "✓ High confidence prediction"
                    
                    # Store the prediction label for comparison
                    st.session_state.multinomial_pred_label = multinomial_pred_label
                    
                    # Display prediction with color and confidence indicator
                    st.markdown(f"<h3 style='color:{pred_color}'>Prediction: {multinomial_pred_label}</h3>", unsafe_allow_html=True)
                    st.write(f"Confidence: {pred_prob}")
                    st.write(confidence_message)
                    
                    # Show probabilities as bar chart
                    probs_df = pd.DataFrame({
                        'Class': ['Negative', 'Positive'],
                        'Probability': [user_proba_multinomial[0], user_proba_multinomial[1]]
                    })
                    st.bar_chart(probs_df.set_index('Class'))
                
                # Add a section comparing the results - ENHANCED VERSION
                st.subheader("Comparison Summary")
                
                # Use the already determined prediction labels and add confidence info
                if st.session_state.bernoulli_pred_label == st.session_state.multinomial_pred_label:
                    agreement = f"Both models agree: The text is {st.session_state.bernoulli_pred_label}"
                    if user_proba_bernoulli.max() < 0.6 and user_proba_multinomial.max() < 0.6:
                        st.warning(f"{agreement}, but both have low confidence")
                    else:
                        st.success(agreement)
                else:
                    st.warning(f"Models disagree: Bernoulli predicts {st.session_state.bernoulli_pred_label}, while Multinomial predicts {st.session_state.multinomial_pred_label}")
                
                # Add enhanced word analysis
                st.subheader("Word Analysis")
                
                # Split the text into words and show which are significant
                import re
                from collections import Counter
                
                # Get all words from input text
                words = re.findall(r'\b\w+\b', user_text.lower())
                word_count = Counter(words)
                
                # Extract key negative and positive words from the models
                bern_neg_idx = 0 if st.session_state.bernoulli_results['model'].classes_[0] == 0 else 1
                bern_pos_idx = 1 - bern_neg_idx
                
                # Extract top words with their probabilities for each class
                bern_neg_words = {}
                bern_pos_words = {}
                
                if f"class_{bern_neg_idx}" in st.session_state.bernoulli_results['top_features']:
                    for word, score in st.session_state.bernoulli_results['top_features'][f"class_{bern_neg_idx}"]:
                        bern_neg_words[word.lower()] = score
                
                if f"class_{bern_pos_idx}" in st.session_state.bernoulli_results['top_features']:
                    for word, score in st.session_state.bernoulli_results['top_features'][f"class_{bern_pos_idx}"]:
                        bern_pos_words[word.lower()] = score
                
                # Find matching words in input text with their impact on classification
                word_impacts = []
                for word in word_count:
                    # Calculate impact scores (negative means pushes toward negative class)
                    neg_impact = bern_neg_words.get(word, 0)
                    pos_impact = bern_pos_words.get(word, 0)
                    net_impact = pos_impact - neg_impact
                    
                    if word in bern_neg_words or word in bern_pos_words:
                        word_impacts.append({
                            "Word": word,
                            "Count in Text": word_count[word],
                            "Positive Impact": f"{pos_impact:.4f}",
                            "Negative Impact": f"{neg_impact:.4f}",
                            "Net Impact": f"{net_impact:.4f}",
                            "Classification Tendency": "Positive" if net_impact > 0 else "Negative"
                        })
                
                # Sort by absolute impact value
                word_impacts.sort(key=lambda x: abs(float(x["Net Impact"])), reverse=True)
                
                if word_impacts:
                    st.write("### Words in your text that influenced the models' predictions:")
                    st.dataframe(pd.DataFrame(word_impacts))
                    
                    # Show overall impact analysis
                    total_positive = sum(float(w["Positive Impact"]) for w in word_impacts if w["Positive Impact"] != "0.0000")
                    total_negative = sum(float(w["Negative Impact"]) for w in word_impacts if w["Negative Impact"] != "0.0000")
                    st.write(f"**Overall text sentiment impact**: Positive: {total_positive:.4f}, Negative: {total_negative:.4f}")
                    
                    # Suggestion for stronger negative text
                    if st.session_state.bernoulli_pred_label == "Positive" and st.session_state.multinomial_pred_label == "Positive":
                        st.info("**Suggestion:** To get a negative classification, try including more strong negative words like: 'fail', 'limit', 'undermine', 'inequality', 'cuts', 'drain', 'privatization', 'standardized testing'")
                else:
                    st.info("None of the words in your text appear in the models' vocabulary or have significant impact.")

                # Add debugging information in an expander
                with st.expander("Debug Information"):
                    st.write("Bernoulli Raw Prediction:", user_pred_bernoulli)
                    st.write("Multinomial Raw Prediction:", user_pred_multinomial)
                    st.write("Bernoulli Classes:", st.session_state.bernoulli_results['model'].classes_)
                    st.write("Multinomial Classes:", st.session_state.multinomial_results['model'].classes_)
                    if 'positive_class' in st.session_state.bernoulli_results:
                        st.write("Bernoulli Positive Class:", st.session_state.bernoulli_results['positive_class'])
                    if 'negative_class' in st.session_state.bernoulli_results:
                        st.write("Bernoulli Negative Class:", st.session_state.bernoulli_results['negative_class'])
                    if 'positive_class' in st.session_state.multinomial_results:
                        st.write("Multinomial Positive Class:", st.session_state.multinomial_results['positive_class'])
                    if 'negative_class' in st.session_state.multinomial_results:
                        st.write("Multinomial Negative Class:", st.session_state.multinomial_results['negative_class'])

            # Word analysis
            st.subheader("Word Analysis")
            
            # Split the text into words and show which are significant
            import re
            from collections import Counter
            
            # Get all words from input text
            words = re.findall(r'\b\w+\b', user_text.lower())
            word_count = Counter(words)
            
            # Get feature names from both models
            bernoulli_features = set(st.session_state.bernoulli_results['vectorizer'].get_feature_names_out())
            multinomial_features = set(st.session_state.multinomial_results['vectorizer'].get_feature_names_out())
            
            # Find words that appear in the models' vocabularies
            matching_words = []
            for word in word_count:
                in_bernoulli = word in bernoulli_features
                in_multinomial = word in multinomial_features
                if in_bernoulli or in_multinomial:
                    matching_words.append({
                        "Word": word,
                        "Count": word_count[word],
                        "In Bernoulli": "Yes" if in_bernoulli else "No",
                        "In Multinomial": "Yes" if in_multinomial else "No"
                    })
            
            if matching_words:
                st.write("Words from your text that influenced the models' predictions:")
                st.table(pd.DataFrame(matching_words))
            else:
                st.info("None of the words in your text appear in the models' vocabularies.")

        # Original code for single model results
        elif 'model_trained' in st.session_state and st.session_state.model_trained:
            st.header("Model Results")
            
            # Dataset info
            col1, col2 = st.columns(2)
            with col1:
                # Use session state to access train_set and test_set here too
                st.write(f"Training set size: {len(st.session_state.train_set)}")
                st.write(f"Test set size: {len(st.session_state.test_set)}")
                
                # Class distribution
                st.subheader("Class Distribution")
                train_dist = pd.DataFrame(st.session_state.train_set[label_col].value_counts()).transpose()
                test_dist = pd.DataFrame(st.session_state.test_set[label_col].value_counts()).transpose()
                st.write("Training set:", train_dist)
                st.write("Test set:", test_dist)
            
            with col2:
                st.subheader("Feature Information")
                st.write(f"Number of features: {len(st.session_state.results['features'])}")
                if st.checkbox("Show feature names"):
                    st.write(st.session_state.results['features'])
            
            # Metrics
            st.header("Performance Metrics")
            metrics = st.session_state.metrics
            
            # Metrics in columns
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Accuracy", f"{metrics['accuracy']:.2f}")
            col2.metric("Precision", f"{metrics['precision']:.2f}")
            col3.metric("Recall", f"{metrics['recall']:.2f}")
            col4.metric("F1 Score", f"{metrics['f1']:.2f}")
            
            # Confusion Matrix
            st.subheader("Confusion Matrix")
            st.write(metrics['confusion_matrix'])
            
            # Predictions
            st.subheader("Predictions")
            if st.checkbox("Show predictions"):
                predictions_df = pd.DataFrame({
                    'Text': st.session_state.test_set[text_col],
                    'True Label': st.session_state.y_test,
                    'Predicted Label': st.session_state.results['prediction_labels']
                })
                st.write(predictions_df)
            
            # ROC Curve for binary classification
            if len(np.unique(st.session_state.y_test)) == 2:
                st.subheader("ROC Curve")
                pos_label = 'positive' if st.session_state.y_test.dtype == 'object' else 1
                fig, roc_auc = plot_roc_curve(st.session_state.y_test, 
                                             st.session_state.results['probabilities'], 
                                             pos_label)
                if fig:
                    st.pyplot(fig)
                    st.write(f"Area Under Curve (AUC): {roc_auc:.4f}")
            
            # Custom text prediction
            st.header("Test Your Own Text")
            user_text = st.text_area("Enter text to classify:")
            
            if st.button("Classify") and user_text:
                # Vectorize and predict
                user_vector = st.session_state.results['vectorizer'].transform([user_text])
                user_pred = st.session_state.results['model'].predict(user_vector)[0]
                user_proba = st.session_state.results['model'].predict_proba(user_vector)[0]
                
                # Display result
                st.write("### Prediction Results")
                
                # Check if we have positive/negative classification
                if 'positive_class' in st.session_state.results and st.session_state.results['positive_class'] is not None:
                    # Get index of positive class
                    pos_idx = np.where(st.session_state.results['class_mapping'] == st.session_state.results['positive_class'])[0][0]
                    neg_idx = 1 - pos_idx  # Since we have binary classification
                    
                    # Format prediction result
                    if user_pred == st.session_state.results['positive_class']:
                        pred_label = "Positive"
                        pred_prob = f"{user_proba[pos_idx]:.2%}"
                        pred_color = "green"
                    else:
                        pred_label = "Negative"
                        pred_prob = f"{user_proba[neg_idx]:.2%}"
                        pred_color = "red"
                    
                    # Display prediction with color
                    st.markdown(f"<h3 style='color:{pred_color}'>Prediction: {pred_label} with confidence {pred_prob}</h3>", unsafe_allow_html=True)
                    
                    # Show probabilities as bar chart
                    probs_df = pd.DataFrame({
                        'Class': ['Negative', 'Positive'],
                        'Probability': [user_proba[neg_idx], user_proba[pos_idx]]
                    })
                    st.bar_chart(probs_df.set_index('Class'))
                    
                    # Word analysis - highlight positive/negative words
                    if 'top_features' in st.session_state.results:
                        st.subheader("Word Analysis")
                        
                        # Create two columns for positive and negative words
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            st.write("### Top Positive Words")
                            if f"class_{pos_idx}" in st.session_state.results['top_features']:
                                pos_features = st.session_state.results['top_features'][f"class_{pos_idx}"]
                                pos_df = pd.DataFrame(pos_features, columns=['Word', 'Score'])
                                st.dataframe(pos_df, width=300)
                        
                        with col2:
                            st.write("### Top Negative Words")
                            if f"class_{neg_idx}" in st.session_state.results['top_features']:
                                neg_features = st.session_state.results['top_features'][f"class_{neg_idx}"]
                                neg_df = pd.DataFrame(neg_features, columns=['Word', 'Score'])
                                st.dataframe(neg_df, width=300)
                        
                        # Highlight matching words in input text
                        st.subheader("Word Highlighting")
                        
                        # Get all words from the input text
                        import re
                        words = re.findall(r'\b\w+\b', user_text.lower())
                        
                        # Extract top words from both classes
                        top_pos_words = [word.lower() for word, _ in pos_features]
                        top_neg_words = [word.lower() for word, _ in neg_features]
                        
                        # Create HTML with highlighted words
                        html_parts = []
                        for word in words:
                            if word in top_pos_words:
                                html_parts.append(f'<span style="background-color:#a1f5a1">{word}</span>')
                            elif word in top_neg_words:
                                html_parts.append(f'<span style="background-color:#f5a1a1">{word}</span>')
                            else:
                                html_parts.append(word)
                        
                        highlighted_text = ' '.join(html_parts)
                        st.markdown(f"<p>{highlighted_text}</p>", unsafe_allow_html=True)
                        
                        # Legend
                        st.markdown("""
                        **Legend:**
                        - <span style="background-color:#a1f5a1">Green</span>: Words associated with positive sentiment
                        - <span style="background-color:#f5a1a1">Red</span>: Words associated with negative sentiment
                        """, unsafe_allow_html=True)
                else:
                    # Regular display for non-binary or non-standard classification
                    st.write(f"Prediction: **{user_pred}**")
                    st.write("Probabilities:")
                    st.write(user_proba)

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.exception(e)

# Run the app
if __name__ == "__main__":
    main()
