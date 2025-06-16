import joblib
import pandas as pd

model = joblib.load("aircraft_classifier.pkl")

# Example input for prediction
new_aircraft = pd.DataFrame(
    [
        {
            "Speed (km/h)": 2120,
            "Weight (kg)": 18400,
            "Operational Range (km)": 3000,
        }
    ]
)

type = model.predict(new_aircraft)
print(f"The aircraft type is: {type[0]}")
