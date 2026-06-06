from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open("mlr_test.pkl", "rb") as file:
    model = pickle.load(file)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        hours_studied = float(request.form['hours_studied'])
        previous_scores = float(request.form['previous_scores'])
        sleep_hours = float(request.form['sleep_hours'])
        sample_papers = float(request.form['sample_papers'])

        features = np.array(
            [[hours_studied, previous_scores, sleep_hours, sample_papers]]
        )

        prediction = model.predict(features)[0]

        return render_template(
            'index.html',
            prediction_text=f'Predicted Performance Index: {prediction:.2f}'
        )

    except Exception as e:
        return render_template(
            'index.html',
            prediction_text=f'Error: {str(e)}'
        )


if __name__ == "__main__":
    app.run(debug=True)