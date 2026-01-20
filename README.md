# 📩 Spam Detection System using Machine Learning

This project is a machine learning–based **Spam Detection System**
that classifies messages as **SPAM** or **HAM** and shows spam intensity
(High / Medium / Low).

## 🚀 Features
- Uses **your custom dataset**
- Naive Bayes classification
- Shows **Spam Level** instead of percentage
- Flask-based web interface
- Real-time prediction

## 🛠️ Tech Stack
- Python 3.10
- Scikit-learn
- Pandas
- Flask
- HTML & CSS

## 📁 Project Structure
spam_detector/
├── app.py
├── train_model.py
├── spam_model.pkl
├── vectorizer.pkl
├── templates/
│ └── index.html
├── static/
├── requirements.txt
└── README.md



## ▶️ How to Run the Project
```bash
pip install -r requirements.txt
python train_model.py
python app.py
Open in browser:

http://127.0.0.1:5000/

📌 Example Output
Prediction: SPAM 🚨
Spam Level: HIGH

📊 Spam Level Logic
HIGH → Spam Probability ≥ 70%

MEDIUM → 40% – 69%

LOW → < 40%

🎯 Use Case
Email filtering

SMS spam detection

Cybersecurity awareness

👩‍💻 Author
Rethikaa Ramesh

## 📄 requirements.txt (Very Important)

```txt
flask
pandas
scikit-learn
numpy
