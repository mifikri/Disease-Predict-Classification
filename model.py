from keras.models import model_from_json
import numpy as np

def load_model():
    load_model = model_from_json(open('model.json').read())
    load_model.load_weights('model_weights.h5')
    return load_model	

def predict(input_symptoms):
    model = load_model()
    #predictions = np.argmax(model.predict(np.array([input_symptoms])))
    #predictions = np.argmax(model.predict(input_symptoms), axis=1)
    predictions = np.argmax(model.predict(np.array(input_symptoms)), axis=1)
    return int(predictions)

