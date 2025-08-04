import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import pickle

df = pd.read_csv('data/Language Detection.csv')

X = df['Text']
y = df['Language']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('nb', MultinomialNB())
])

model.fit(X_train, y_train)

print(f'Model accuracy: {model.score(X_test, y_test)}')

with open('models/language_detection_model.pkl', 'wb') as f:
    pickle.dump(model, f)
