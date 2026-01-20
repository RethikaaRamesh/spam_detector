📩 Spam Detection System using Machine Learning

This project is a Machine Learning–based Spam Detection System that classifies messages as SPAM or HAM and displays the Spam Intensity Level (High / Medium / Low) instead of raw percentages.

🚀 Features

✅ Uses your custom dataset

🤖 Naive Bayes classification

📊 Displays Spam Level (High / Medium / Low)

🌐 Flask-based web interface

⚡ Real-time message prediction

🛠️ Tech Stack

Python 3.10

Scikit-learn

Pandas

Flask

HTML & CSS
📁 Project Structure
```text 
spam_detector/
│
├── dataset/
│ ├── SMSSpamCollection
│ └── spam.csv
│
├── templates/
│ └── index.html
│
├── app.py
├── train_model.py
├── download_dataset.py
├── spam_model.pkl
├── vectorizer.pkl
├── requirements.txt
└── README.md

▶️ How to Run the Project
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Train the model
python train_model.py

3️⃣ Run the Flask app
python app.py

4️⃣ Open in browser
http://127.0.0.1:5000/

📌 Example Output
Prediction: SPAM 🚨
Spam Level: HIGH

📊 Spam Level Logic
Spam Probability	Spam Level
≥ 70%	HIGH 🔴
40% – 69%	MEDIUM 🟠
< 40%	LOW 🟢
🎯 Use Cases

📧 Email filtering

📩 SMS spam detection

🔐 Cybersecurity awareness

📄 requirements.txt (Very Important)
flask
pandas
scikit-learn
numpy

👩‍💻 Author

Rethikaa Ramesh
🔗 GitHub: https://github.com/RethikaaRamesh




