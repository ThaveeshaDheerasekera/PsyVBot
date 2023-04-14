import os
import re
import string
import numpy as np
import tensorflow as tf
from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences

# Load trained LSTM model
lstm_model = load_model('models/final_models/lstm_e10_b32.h5')

# Load word to index and index to word mappings
word2index = {"<PAD>": 0, "<UNK>": 1, "<EOS>": 2, "hello": 3, "how": 4, "are": 5, "you": 6, "i": 7, "am": 8, "good": 9, "bye": 10, "diagnose": 11, "quit": 12}
index2word = {0: "<PAD>", 1: "<UNK>", 2: "<EOS>", 3: "hello", 4: "how", 5: "are", 6: "you", 7: "i", 8: "am", 9: "good", 10: "bye", 11: "diagnose", 12: "quit"}

# Define user inputs list
user_inputs = []

# Start conversation with user
print("-------------------------------------------------------------------------------------")
print("---- PsyVBot ----")
print("-------------------------------------------------------------------------------------")
print("-- Important --")
print("\t- Enter \"diagnose\" to get a diagnosis")
print("\t- Enter \"exit\" to exit the chatbot. (This option will NOT provide a diagnosis)")
print("-------------------------------------------------------------------------------------")
print("PsyVBot: Hi! I'm here to listen. How are you feeling today?")

# Define maximum length of input sequence
max_len = 20

# Initialize tokenizer
tokenizer = Tokenizer(filters='', lower=False)

def preprocess_text(user_input):
    # Convert to lowercase
    user_input = user_input.lower()
    # Remove non-alphanumeric characters
    user_input = re.sub(r'\W+', ' ', user_input)
    # Remove extra spaces
    user_input = re.sub(r'\s+', ' ', user_input)
    # Truncate to maximum length
    user_input = user_input[:max_len]
    # Add start and end tokens
    user_input = "<START> " + user_input + " <END>"
    return user_input


def generate_response(user_input, max_len=20):
    input_seq = tokenizer.texts_to_sequences([user_input])[0]
    input_seq = pad_sequences([input_seq], maxlen=max_len, padding='post')
    predicted_seq = lstm_model.predict(input_seq)[0]
    predicted_seq = np.argmax(predicted_seq, axis=-1)
    output = tokenizer.sequences_to_texts([predicted_seq])[0]
    return output


while True:
    # Get user input
    user_input = input("User: ")

    # Add user input to list
    user_inputs.append(user_input)

    # Check if user wants to end the conversation
    if user_input.lower() == "quit":
        print("PsyVBot: It was nice talking to you. Take care!")
        # Clear user inputs list
        user_inputs = []
        break

    # Check if user wants to diagnose depression
    if user_input.lower() == "diagnose":
        # Check if user has provided enough input to diagnose depression
        if len(user_inputs) < 10:
            print("PsyVBot: Sorry, I need more information to diagnose your condition. Can you tell me more about how you've been feeling?")
            continue
        # Preprocess user input
        user_input_seq = []
        for user_input in user_inputs:
            user_input = preprocess_text(user_input)
            for word in user_input.split():
                if word in word2index:
                    user_input_seq.append(word2index[word])
                else:
                    user_input_seq.append(word2index["<UNK>"])
        user_input_seq = np.array(user_input_seq)
        # Use LSTM model to predict depression diagnosis
        predicted_output = lstm_model.predict(np.array([user_input_seq]))
        if predicted_output > 0.5:
            print("PsyVBot: Based on what you've told me, you might be showing signs of depression. It's important to take care of your mental health. Have you considered talking to a professional about how you're feeling?")
        else:
            print("PsyVBot: It sounds like you're doing well. Keep up the good work!")
        # Clear user inputs list
        user_inputs = []
        continue

    # Generate response
    response = generate_response(user_input, max_len)

    # Print response
    print("PsyVBot:", response)

    # Ask follow-up questions based on the response
    if "how" in response.lower():
        follow_up = input("PsyVBot: How do you feel about that?")
        user_inputs.append(follow_up)
    elif "why" in response.lower():
        follow_up = input("PsyVBot: Why do you think that is?")
        user_inputs.append(follow_up)
    elif "tell me more" in response.lower():
        follow_up = input("PsyVBot: Can you elaborate on that?")
        user_inputs.append(follow_up)
    elif "what can i do" in response.lower():
        follow_up = input("PsyVBot: Have you considered talking to a therapist?")
        user_inputs.append(follow_up)
