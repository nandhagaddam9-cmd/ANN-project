from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)

model = joblib.load("model.pkl")

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    capacitance = float(data["capacitance"])
    voltage = float(data["voltage"])
    current_density = float(data["currentDensity"])
    surface_area = float(data["surfaceArea"])

    # Example feature array
    features = np.array([[
        capacitance,
        voltage,
        current_density,
        surface_area
    ]])

    prediction = model.predict(features)

    efficiency = round(float(prediction[0]), 2)

    return jsonify({
        "efficiency": f"{efficiency}%",
        "energy_density": f"{round(efficiency * 0.4, 2)} Wh/kg",
        "power_density": f"{round(efficiency * 0.15, 2)} kW/kg",
        "cycle_stability": int(efficiency * 120)
    })

if __name__ == "__main__":
    app.run(debug=True)