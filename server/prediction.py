import json
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import logging
logging.getLogger('tensorflow').setLevel(logging.ERROR)

from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
from keras.models import load_model

# Load the saved model from the .h5 file
model = load_model('/Users/thaveesha/Projects/PsyVBot/models/final_models/lstm_e5_b32_es.h5')

def predict_depression(user_inputs):
    # Load the tokenizer that you used during training
    tokenizer = Tokenizer(num_words=5000)
    tokenizer.fit_on_texts(user_inputs)

    # Convert the input strings into sequences of integers
    sequences = tokenizer.texts_to_sequences(user_inputs)

    # Pad the sequences to a fixed length
    padded_sequences = pad_sequences(sequences, maxlen=100)

    # Make a prediction on the padded sequences
    predictions = model.predict(padded_sequences)

    prediction_avg = sum(predictions)/len(user_inputs)

        # Convert the ndarray to a list
    prediction_list = prediction_avg.tolist()

    # Return the prediction as a JSON-serializable string
    return json.dumps({'prediction': prediction_list})