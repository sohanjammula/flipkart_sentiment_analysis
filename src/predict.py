import os
import pickle
from src.preprocess import clean_text
from src.features import load_vectorizer, transform_text

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "model", "sentiment_model.pkl")
VECTORIZER_PATH = os.path.join(BASE_DIR, "model", "tfidf_vectorizer.pkl")

model = pickle.load(open(MODEL_PATH, "rb"))
vectorizer = pickle.load(open(VECTORIZER_PATH, "rb"))

def predict_sentiment(review: str) -> str:
    cleaned = clean_text(review)
    vectorized = transform_text(vectorizer, [cleaned])
    prediction = model.predict(vectorized)[0]

    return "Positive 😊" if prediction == 1 else "Negative 😞"

