import pickle
import sys

with open('models/language_detection_model.pkl', 'rb') as f:
    model = pickle.load(f)

text = sys.argv[1]

prediction = model.predict([text])
print(f'The predicted language is: {prediction[0]}')
