import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import joblib

# GENERATE SYNTHETIC DATA

rows = []

for _ in range(1000):

    capacitance = np.random.randint(150, 400)

    voltage = round(np.random.uniform(1.5, 3.5), 2)

    currentDensity = round(np.random.uniform(1, 10), 2)

    surfaceArea = np.random.randint(500, 2000)

    # FAKE SCIENTIFIC RELATION

    efficiency = (
        capacitance * 0.12
        + voltage * 12
        - currentDensity * 1.5
        + surfaceArea * 0.015
    )

    rows.append([
        capacitance,
        voltage,
        currentDensity,
        surfaceArea,
        efficiency
    ])

df = pd.DataFrame(rows, columns=[
    "capacitance",
    "voltage",
    "currentDensity",
    "surfaceArea",
    "efficiency"
])

# FEATURES

X = df[[
    "capacitance",
    "voltage",
    "currentDensity",
    "surfaceArea"
]]

# TARGET

y = df["efficiency"]

# MODEL

model = RandomForestRegressor()

model.fit(X, y)

# SAVE

joblib.dump(model, "model.pkl")

print("Pretrained model ready!")