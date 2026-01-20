from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load FULL pipeline
model = joblib.load("spam_model.pkl")

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    spam_level = None
    message = ""

    if request.method == "POST":
        message = request.form["message"]

        # Predict
        pred = model.predict([message])[0]
        prob = model.predict_proba([message])[0]

        spam_prob = prob[1]

        if spam_prob > 0.7:
            spam_level = "HIGH"
        elif spam_prob > 0.4:
            spam_level = "MEDIUM"
        else:
            spam_level = "LOW"

        prediction = "SPAM 🚫" if pred == 1 else "HAM ✅"

    return render_template(
        "index.html",
        prediction=prediction,
        spam_level=spam_level,
        message=message
    )

if __name__ == "__main__":
    app.run(debug=True)
