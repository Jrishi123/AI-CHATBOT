import json
import random
import nltk
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

nltk.download('punkt')

stemmer = PorterStemmer()

# Load intents
with open('intents.json') as file:
    data = json.load(file)

sentences = []
labels = []
tags = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        sentences.append(pattern)
        labels.append(intent['tag'])
    tags.append(intent['tag'])

# Convert text → numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(sentences)

# Train model
model = LogisticRegression()
model.fit(X, labels)

# Chat loop
def chat():
    print("🤖 Chatbot is running (type 'quit' to stop)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "quit":
            print("Bot: Goodbye! 👋")
            break

        X_test = vectorizer.transform([user_input])
        predicted_tag = model.predict(X_test)[0]

        for intent in data['intents']:
            if intent['tag'] == predicted_tag:
                print("Bot:", random.choice(intent['responses']))

# Run chatbot
chat()