# Language Detection Project

This project is a machine learning model that can identify the language of a given piece of text. It is built using Python and the scikit-learn library. The model is trained on a dataset of text samples from 17 different languages.

## Features

- Detects 17 different languages: English, Malayalam, Hindi, Tamil, Portugeese, French, Spanish, Dutch, Sweedish, Italian, Russian, anish, anish, Turkish, German, Arabic, and Kannada.
- Achieves ~98% accuracy on the test set.
- Simple and easy-to-use command-line interface for training and prediction.
- Includes a web application built with Flask to provide a user-friendly interface.

## Dataset

The model is trained on the "Language Detection" dataset from Kaggle. You can find the dataset [here](https://www.kaggle.com/datasets/basilb2s/language-detection). It contains a single CSV file with two columns: "Text" and "Language".

## Technologies Used

- Python
- scikit-learn
- pandas
- NumPy
- Jupyter
- Matplotlib
- Seaborn
- Flask

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/LEGBEDJE/Language-Detection
    cd language-detection
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Training the Model

To train the model, run the following command in your terminal:

```bash
python src/train.py
```

This will train a Naive Bayes classifier on the dataset and save the trained model as `models/language_detection_model.pkl`.

### Making Predictions (Command Line)

You can use the trained model to predict the language of a given text directly from the command line:

```bash
python src/predict.py "Your text here"
```

For example:

```bash
python src/predict.py "Bonjour, comment ça va?"
```

The script will output the predicted language.

### Web Application

This project also includes a modern and responsive web application built with Flask that allows you to use the language detection model through a web browser.

**Screenshot:**

*Replace this with a screenshot of the web application.*

1.  **Run the Flask app:**
    ```bash
    python app.py
    ```

2.  **Open your web browser** and navigate to `http://127.0.0.1:5000`.

You will see a stylish web page with a text area where you can enter text. The predicted language will be displayed below.

## Future Improvements

- **Use a more advanced model:** Experiment with more sophisticated models like LSTMs or Transformers for potentially higher accuracy.
- **Support more languages:** Train the model on a larger dataset that includes a wider variety of languages.
- **Deploy to the cloud:** Deploy the Flask application to a cloud platform like Heroku or AWS so that it's publicly accessible.
