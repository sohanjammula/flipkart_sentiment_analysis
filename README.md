# Flipkart Sentiment Analysis using Machine Learning & NLP

This project performs **sentiment analysis on Flipkart product reviews** using Natural Language Processing (NLP) and multiple Machine Learning models.  
The goal is to classify customer reviews as **Positive** or **Negative** and deploy the best-performing model using a **Flask web application**.

---

## 📌 Project Objectives
- Clean and preprocess real-world customer reviews
- Convert text data into numerical features using **TF-IDF**
- Train and compare multiple ML models
- Select the best model based on **Macro F1-score**
- Deploy the final model using **Flask**

---

## 🧠 Models Used
The following models were trained and evaluated:

- Logistic Regression
- Naive Bayes
- Linear Support Vector Machine (SVM)
- Random Forest
- XGBoost
- CatBoost
- Linear Regression (baseline with thresholding)

📌 **Model Selection Metric:**  
**Macro F1-score** was used to ensure balanced performance for both positive and negative classes.

➡ **Final Selected Model:** Linear SVM  
(Provided the best balance between positive and negative sentiment prediction)

---

## 🛠️ Tech Stack
- **Programming Language:** Python
- **Libraries:**  
  - pandas, numpy  
  - scikit-learn  
  - nltk  
  - xgboost, catboost  
  - flask  
  - matplotlib, seaborn
- **Frontend:** HTML (Flask templates)
- **Backend:** Flask

---

---

## 🔄 Project Workflow
1. **Data Cleaning & Preprocessing**
   - Removal of null values
   - Text normalization (lowercasing, punctuation removal)
   - Stopword removal and lemmatization

2. **Feature Extraction**
   - TF-IDF Vectorization with max 5000 features

3. **Model Training & Evaluation**
   - Train-test split with stratification
   - Class imbalance handled using class weights
   - Evaluation using Precision, Recall, F1-score

4. **Model Selection**
   - Best model selected based on **Macro F1-score**

5. **Deployment**
   - Flask-based web interface for real-time prediction

---

## 🚀 How to Run the Project

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
### run the app.py
python app/app.py

