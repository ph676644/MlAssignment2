import joblib
import numpy as np

whitemodel = joblib.load("white_wine_quality_model.pkl")
redmodel = joblib.load("red_wine_quality_model.pkl")

features = [
    "fixed acidity", "volatile acidity", "citric acid", "residual sugar",
    "chlorides", "free sulfur dioxide", "total sulfur dioxide",
    "density", "pH", "sulphates", "alcohol"
]

#input here
wine_input = [7.4, 0.70, 0.00, 1.9, 0.076, 11.0, 34.0, 0.9978, 3.51, 0.56, 9.4] #temp values


X_new = np.array(wine_input).reshape(1, -1)
predicted_quality = whitemodel.predict(X_new)[0]

print(f"Predicted Wine Quality: {predicted_quality:.2f}")