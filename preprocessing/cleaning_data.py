import pandas as pd
import numpy as np
from predict.prediction import predict


default_columns = ['price', 'bedrooms-number', 'area', 'kitchen', 'bathroom-number', 'balcony', 'building-state',
                   'master-bedroom-area', 'living-room-area', 'cellar', 'facades-number', 'terrace-area',
                   'garden-area', 'garage', 'apartment', 'bungalow', 'chalet', 'cottage', 'duplex',
                   'ground-floor', 'loft', 'mansion', 'master-house', 'mixed-building', 'penthouse', 'residence',
                   'studio', 'triplex', 'villa', 'Antwerp Province', 'Brussels-Capital Region',
                   'East Flanders Province', 'Flemish Brabant Province', 'Hainaut Province', 'Limburg Province',
                   'Liège Province', 'Luxembourg Province', 'Namur Province', 'Walloon Brabant Province',
                   'West Flanders Province']

zipcodes = {
    ("1000", "1299"): "Brussels-Capital Region",
    ("1300", "1499"): "Walloon Brabant Province",
    ("1500", "1999"): "Flemish Brabant Province",
    ("2000", "2999"): "Antwerp Province",
    ("3000", "3499"): "Flemish Brabant Province",
    ("3500", "3999"): "Limburg Province",
    ("4000", "4999"): "Liège Province",
    ("5000", "5999"): "Namur Province",
    ("6000", "6599"): "Hainaut Province",
    ("6600", "6999"): "Luxembourg Province",
    ("7000", "7999"): "Hainaut Province",
    ("8000", "8999"): "West Flanders Province",
    ("9000", "9999"): "East Flanders Province",
}


def preprocess(data):
    """
    Take a JSON formatted file as input
    :return: numpy array ready for prediction model
    """

    # Creating an empty DataFrame that matches the model
    zeros = np.zeros(shape=(1, len(default_columns)))
    df = pd.DataFrame(zeros, columns=default_columns)

    # Untransformed data
    df["bedrooms-number"] = data["data"]["bedrooms-number"]
    df["area"] = data["data"]["area"]
    df["terrace-area"] = data["data"]["terrace-area"]
    df["facades-number"] = data["data"]["facades-number"]

    # kitchen data cleaning
    if data["data"]["kitchen"] == "Not equipped":
        df["kitchen"] = 0
    elif data["data"]["kitchen"] == "Partially equipped":
        df["kitchen"] = 1
    elif data["data"]["kitchen"] == "Fully equipped":
        df["kitchen"] = 2
    elif data["data"]["kitchen"] == "Super equipped":
        df["kitchen"] = 3

    # property type cleaning
    property_type = data["data"]["property-type"]
    df[property_type] = 1

    # garden cleaning
    if data["data"]["garden-area"]:
        df["garden-area"] = data["data"]["garden-area"]
    else:
        df["garden-area"] = 0

    # zip-code transformation
    for k, v in zipcodes.items():
        if k[0] < data["data"]["zip-code"] < k[1]:
            df[v] = 1

    # garage
    if data["data"]["garage"]:
        df["garage"] = 1

    # bacony
    if data["data"]["balcony"]:
        df["balcony"] = 1

    # Building-state cleaning
    if data["data"]["building-state"] == "To be renovated":
        df["building-state"] = 0
    elif data["data"]["building-state"] == "Normal":
        df["building-state"] = 1
    elif data["data"]["building-state"] == "Excellent":
        df["building-state"] = 2
    elif data["data"]["building-state"] == "Fully renovated":
        df["building-state"] = 3
    elif data["data"]["building-state"] == "New":
        df["building-state"] = 4

    # Fill-in empty values
    df.replace("", 0)
    df.replace(np.nan, 0)
    df.fillna(0)

    return predict(np.array(df.values))
