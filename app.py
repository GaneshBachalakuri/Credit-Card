from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load model and scaler
with open("credit_card.pkl", "rb") as f:
    model = pickle.load(f)

with open("standard_scalar.pkl", "rb") as f:
    scaler = pickle.load(f)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        try:
            # Collect form inputs
            features = [
                float(request.form["Age"]),
                float(request.form["NumberOfOpenCreditLinesAndLoans"]),
                float(request.form["NumberRealEstateLoansOrLines"]),
                float(request.form["MonthlyIncome_replaced"]),
                float(request.form["Gender_Male"]),
                float(request.form["Region_East"]),
                float(request.form["Region_North"]),
                float(request.form["Region_South"]),
                float(request.form["Region_West"]),
                float(request.form["Rented_OwnHouse_con"]),
                float(request.form["Occupation_con"]),
                float(request.form["Education_con"])
            ]

            features_array = np.array([features])
            features_scaled = scaler.transform(features_array)

            prediction = model.predict(features_scaled)[0]
            prediction = "Good Customer" if prediction == 1 else "Bad Customer"

        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
