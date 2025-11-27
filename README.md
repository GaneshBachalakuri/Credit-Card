📌 Credit Card Customer Classification – README
⭐ Project Overview

This project is a complete Machine Learning-based Credit Card Customer Classification System built using:

Python (Flask Framework) – Backend API & model inference

HTML/CSS – Frontend user interface

Machine Learning (Scikit-learn + SMOTE) – Data preprocessing, feature engineering & model training

Pickle (.pkl) – Saving trained model & scaler

Procfile – Deployment configuration for platforms like Heroku/Railway

The system predicts whether a credit card customer is a Good Customer or a Bad Customer based on multiple financial and demographic features.

🚀 Features

✔ Machine learning pipeline with:

Missing value handling

Variable transformation

Outlier trimming

Feature selection

Categorical to numerical conversion

Data balancing using SMOTE

Model training and saving

✔ User-friendly web interface built using HTML (templates folder)

✔ Real-time prediction using Flask (app.py)

✔ Ready for cloud deployment using Procfile

🗂️ Project Structure
├── app.py                    # Flask application for prediction
├── main.py                   # Complete ML pipeline (training workflow)
├── balancing_data.py         # SMOTE balancing + scaling
├── credit_card.pkl           # Trained ML model
├── standard_scalar.pkl       # StandardScaler object
├── templates/
│   └── index.html            # Frontend UI
├── Procfile                  # Deployment configuration
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation

🧠 Machine Learning Pipeline Summary
1. Data Loading

Handled in main.py using the CREDIT_CARD_INFO class.

2. Preprocessing Steps

Missing value imputation

Yeo-Johnson transformation

Outlier handling

Feature selection

Encoding categorical variables

Data balancing via SMOTE

3. Scaling & Model Training

Performed in balancing_data.py

StandardScaler saved → standard_scalar.pkl

Logistic Regression model saved → credit_card.pkl

4. Prediction

app.py loads:

credit_card.pkl
standard_scalar.pkl


and generates a prediction:

Good Customer

Bad Customer

🖥️ How to Run Locally
1. Clone the Repository
git clone https:(https://github.com/GaneshBachalakuri/Credit-Card/edit/main/README.md)
cd your-repo-name

2. Create Virtual Environment
python -m venv venv

3. Activate Virtual Environment

Windows

venv\Scripts\activate


Linux/Mac

source venv/bin/activate

4. Install Dependencies
pip install -r requirements.txt

5. Run Flask App
python app.py


☁️ Deployment (Heroku / Railway)
Procfile Content
web: gunicorn app:app



 Deploy
git add .
git commit -m "Initial Deployment"
git push heroku main

🧪 Training the Model

To retrain the model with new data:

Replace your dataset in the project folder

Update dataset path in main.py

Run:

python main.py


This will regenerate:

credit_card.pkl

standard_scalar.pkl

📄 Technologies Used
Backend

Python

Flask

Gunicorn

Machine Learning

Scikit-learn

Pandas

NumPy

SMOTE (Imbalanced-learn)

Frontend

HTML

CSS

Deployment



Procfile

🤝 Contributing

Contributions are welcome!
You can fork the repository and create a pull request.

📝 License

This project is open-source and available under the MIT License.
