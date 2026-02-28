# Spam Email Classifier

A Machine Learning powered web application that detects whether a message is **Spam** or **Not Spam**, built using Python, Scikit-learn, and Flask.

## Features

- Text preprocessing pipeline (lowercasing, stopword removal, stemming)
- TF-IDF vectorization
- Naive Bayes classifier (tuned for improved recall)
- Logistic Regression model comparison
- Hyperparameter tuning (alpha optimization)
- Model confidence score display
- Flask web interface
- Modern responsive UI
- Model serialization using pickle

## Machine Learning Details

### Dataset
- SMS Spam Collection Dataset
- ~5,500 labeled messages (spam / ham)

### Preprocessing Steps
- Lowercasing
- Punctuation removal
- Stopword removal
- Stemming (Porter Stemmer)

### Models Trained
- Multinomial Naive Bayes
- Logistic Regression

### Final Model Performance (Naive Bayes, alpha=0.5)

- Accuracy: ~97.6%
- Precision: 1.00
- Recall: ~83%
- F1 Score: ~0.90

The model prioritizes high precision while maintaining strong recall.

## Execution
To run the application type in terminal
```
python app.py
```
