from flask import Flask, request, render_template
from src.predict import predict_sentiment

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    sentiment = None

    if request.method == "POST":
        review = request.form.get("review", "").strip()
        print("REVIEW RECEIVED:", review)

        if review:
            try:
                sentiment = predict_sentiment(review)
                print("PREDICTION:", sentiment)
            except Exception as e:
                print("ERROR DURING PREDICTION:", e)
                sentiment = "Error analyzing sentiment"

    return render_template("index.html", sentiment=sentiment)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)



