from flask import Flask, request, jsonify
import json
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Load intents
with open('intents.json') as file:
    data = json.load(file)

sentences = []
labels = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        sentences.append(pattern)
        labels.append(intent['tag'])

# Train model
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(sentences)

model = LogisticRegression()
model.fit(X, labels)

app = Flask(__name__)

@app.route("/")
def home():
    return "Chatbot API is running 🚀"

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]

    X_test = vectorizer.transform([user_input])
    predicted_tag = model.predict(X_test)[0]

    for intent in data['intents']:
        if intent['tag'] == predicted_tag:
            return jsonify({
                "response": random.choice(intent['responses'])
            })

    return jsonify({"response": "I don't understand"})

if __name__ == "__main__":
    app.run(debug=True)