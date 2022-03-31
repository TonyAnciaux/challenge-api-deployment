import pickle
import json
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


def predict(array):
    """
    Takes the preprocessed data as an input
    :return: price prediction
    """
    file = "./model/model.sav"
    model = pickle.load(open(file, 'rb'))
    prediction = model.predict(array)

    return {"Predicted price": f"{prediction[0]:.2f}€"}
