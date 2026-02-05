import pickle

def load_vectorizer(path: str):
    with open(path, "rb") as f:
        return pickle.load(f)

def transform_text(vectorizer, text_list):
    return vectorizer.transform(text_list)
