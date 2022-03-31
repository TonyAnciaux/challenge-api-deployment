import pickle


def predict(array):
    """
    Takes the preprocessed data as an input
    :return: price prediction
    """
    file = "/model/model.sav"
    model = pickle.load(open(file, 'rb'))
    prediction = model.predict(array)

    return prediction
