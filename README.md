📚 Student Performance Prediction Using Multiple Linear Regression
🎯 Project Overview

This project uses a Multiple Linear Regression (MLR) model to predict a student's performance score based on various academic and lifestyle factors.

The model is trained using machine learning techniques and saved as a Pickle file (mlr_test.pkl) for deployment in web applications such as Flask.

🚀 Features

✅ Predict student performance accurately

✅ Uses Multiple Linear Regression Algorithm

✅ Trained and saved using Pickle

✅ Easy integration with Flask Web Application

✅ User-friendly prediction system

📊 Input Features

The model uses the following independent variables:

Feature	Description
Hours Studied	Number of study hours
Previous Scores	Previous examination scores
Sleep Hours	Average sleeping hours
Sample Question Papers Practiced	Number of sample papers solved
Target Variable

Performance Index / Student Score

🧠 Machine Learning Algorithm
Multiple Linear Regression

Multiple Linear Regression predicts a dependent variable using multiple independent variables.

The mathematical equation is:

Y=b
0
	​

+b
1
	​

X
1
	​

+b
2
	​

X
2
	​

+b
3
	​

X
3
	​

+b
4
	​

X
4
	​


Where:

Y = Predicted Performance Score
b₀ = Intercept
b₁,b₂,b₃,b₄ = Feature Coefficients
X₁,X₂,X₃,X₄ = Input Features
📈 Model Information
Features Used
Hours Studied
Previous Scores
Sleep Hours
Sample Question Papers Practiced
Learned Coefficients
Hours Studied                     : 2.8562
Previous Scores                   : 1.0189
Sleep Hours                       : 0.4744
Sample Question Papers Practiced  : 0.1971
Intercept
-33.7902
📂 Project Structure
Student-Performance-Prediction/
│
├── app.py
├── templates/
│   └── index.html
│
├── mlr_test.pkl
├── requirements.txt
├── Procfile
└── README.md
⚙️ Installation
Clone the Repository
git clone https://github.com/your-username/student-performance-prediction.git
Navigate to Project Folder
cd student-performance-prediction
Install Required Libraries
pip install -r requirements.txt
▶️ Run the Application
Local Machine
python app.py

Open:

http://127.0.0.1:5000/

in your browser.

💻 Example Input
Feature	Value
Hours Studied	8
Previous Scores	85
Sleep Hours	7
Sample Papers Practiced	5
Predicted Output
Predicted Student Performance Score

(The output will vary according to the model.)

🛠 Technologies Used
Python
NumPy
Pandas
Scikit-Learn
Flask
HTML/CSS
Pickle
📦 Requirements
Flask
numpy
pandas
scikit-learn
gunicorn

Install using:

pip install Flask numpy pandas scikit-learn gunicorn
🌐 Deployment

This project can be deployed on:

Render
Heroku
Railway

Typical deployment files:

Procfile
requirements.txt
app.py
mlr_test.pkl
📖 Workflow
Collect Dataset
        ↓
Data Preprocessing
        ↓
Train MLR Model
        ↓
Evaluate Performance
        ↓
Save Model as Pickle
        ↓
Build Flask Application
        ↓
Deploy to Cloud
🎓 Learning Outcomes

Through this project you will learn:

Multiple Linear Regression
Data Preprocessing
Model Training
Model Persistence using Pickle
Flask Integration
Machine Learning Deployment
GitHub Project Management

deployment on renfer.com
**https://mlr-studentperformace.onrender.com**

👩‍💻 Author

Bharathi Vennela

Machine Learning | Data Science | Python Developer
