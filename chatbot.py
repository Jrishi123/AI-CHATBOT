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

# Vectorize
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(sentences)

# Train model
model = LogisticRegression()
model.fit(X, labels)

# Chat function
def chat():
    print("Chatbot is running (type 'quit' to stop)")
    while True:
        inp = input("You: ")
        if inp.lower() == "quit":
            break

        X_test = vectorizer.transform([inp])
        pred = model.predict(X_test)[0]

        for intent in data['intents']:
            if intent['tag'] == pred:
                print("Bot:", random.choice(intent['responses']))

chat()