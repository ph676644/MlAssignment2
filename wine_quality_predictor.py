import joblib
import numpy as np

whitemodel = joblib.load("./models/white_wine_quality_model.pkl")
redmodel = joblib.load("./models/red_wine_quality_model.pkl")


def predict_white(input):
    input_new = np.array(input).reshape(1,-1)
    return whitemodel.predict(input_new)[0]

def predict_red(input):
    input_new = np.array(input).reshape(1,-1)
    return redmodel.predict(input_new)[0]
