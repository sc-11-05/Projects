from flask import Flask, render_template, request
import pickle
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

app = Flask(__name__)

with open("model/spam_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("model/vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

ps = PorterStemmer()

def clean_text(text):
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    words = text.split()
    words = [word for word in words if word not in stopwords.words('english')]
    words = [ps.stem(word) for word in words]
    return " ".join(words)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    message = request.form["message"]
    cleaned = clean_text(message)
    vectorized = vectorizer.transform([cleaned])

    prediction = model.predict(vectorized)[0]
    probabilities = model.predict_proba(vectorized)[0]

    spam_prob = probabilities[1]
    ham_prob = probabilities[0]

    if prediction == 1:
        result = f"Spam ❌ (Confidence: {spam_prob * 100:.2f}%)"
    else:
        result = f"Not Spam ✅ (Confidence: {ham_prob * 100:.2f}%)"

    return render_template("index.html", prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)