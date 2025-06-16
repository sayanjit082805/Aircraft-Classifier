# Aircraft-Classifier

A machine learning model which classifies the type of an aircraft (Fighter, Bomber, Recon) based on technical specifications like speed, weight, and operational ranges.

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)

# Overview

This project implements a classification system that can identify and categorize military aircraft into three main categories:

- **Fighter Aircraft**: High-speed, agile aircraft designed for air-to-air combat
- **Bomber Aircraft**: Heavy aircraft designed for strategic bombing missions
- **Reconnaissance Aircraft**: Aircraft specialized for surveillance and intelligence gathering

The classifier uses aircraft specifications such as maximum speed, weight, and operational range to make accurate predictions about aircraft type.

# Features

- **Input Parameters**: Speed (in km/hr), Weight (in kg) and Operational range (in km).
- **Model**: Random Forest
- **Multi-class Classification**: Categorizes aircraft into Fighter, Bomber, or Reconnaissance types

# Dataset

The dataset used has been taken from [Kaggle](https://www.kaggle.com/datasets/hosseinbahrami/aircraft-types/data).

- `Aircraft Name`: The name/designation of the aircraft.
- `Manufacturer Country`: The country where the aircraft was developed or manufactured.
- `Weight`: The aircraft’s weight in kilograms (kg).
- `Speed`: The aircraft’s top speed in kilometers per hour (km/h).
- `Operational Range`: The maximum distance the aircraft can operate without refueling, in kilometers (km).
- `Payload`: The primary weapons or armaments equipped on the aircraft.
- `Payload2`: Additional weapons or equipment used on the aircraft.
- `Type`: The class of aircraft — either Fighter, Bomber, or Reconnaissance.

# Installation

1. Clone the repository:

```bash
git clone https://github.com/sayanjit082805/Aircraft-Classifier.git
cd Aircraft-Classifier
```

2. Create a virtual environment (recommended):

```bash
python -m venv aircraft_classifier_env
source aircraft_classifier_env/bin/activate  # On Windows: aircraft_classifier_env\Scripts\activate
```

3. Install required dependencies:

```bash
pip install -r requirements.txt
```

# Usage

As of now, there are no deployments/explicit-frontend to run the model. A sample `test.py` has been provided, simply tweak the required parameters and run the file using `python3 test.py`.

```python
# test.py
import joblib
import pandas as pd
model = joblib.load("aircraft_classifier.pkl")
# Example input for prediction
new_aircraft = pd.DataFrame(
    [
        {
			# input here(+ve integers)
            "Speed (km/h)": ,
            "Weight (kg)": ,
            "Operational Range (km)": ,
        }
    ]
)
type = model.predict(new_aircraft)
print(f"The aircraft type is: {type[0]}")
```

#### Sample Output

`The aircraft type is: Fighter`

# Limitations

Although the accuracy is nearly 80%, due to the imbalanced nature of the database, the predictions will be somewhat biased. The `fighter`, `bomber` and `trainer` types will be predicted more or less correctly (as evidenced by the recall(1.00, 1.00, 1.00) and F1 scores(0.8, 0.91, 1.00)). However, the `reconnaissance` type will almost always be predicted incorrectly (zero recall), due to the small sample-size in the original dataset. Upsampling yielded almost similar results. Thus, this is a limitation.

# Acknowledgements

The dataset has been taken from kaggle.

# License

This project is licensed under The Unlicense License.
