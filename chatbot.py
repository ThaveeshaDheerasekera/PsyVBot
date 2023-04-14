import os
import random
import re
import string
import numpy as np
import tensorflow as tf
from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences

# Define keywords and responses
keywords = {
    "hello": ["Hello! How are you?", "Hi there! How can I help you?"],
    "sad": ["I'm sorry to hear that. Can you tell me more about why you're feeling sad?", 
            "It's okay to not be okay. I'm here to listen. What's been on your mind?"],
    "anxious": ["I'm sorry to hear that you're feeling anxious. Would you like to talk about what's been causing your anxiety?",
                "Anxiety can be tough to deal with. What's been on your mind lately?"],
    "depressed": ["Depression is a tough thing to go through. Can you tell me more about why you're feeling depressed?",
                  "It's okay to not be okay. I'm here to listen. What's been on your mind?"],
    "happy": ["I'm glad to hear that you're feeling happy! Is there anything specific that's made you happy?",
              "That's great to hear! What's been going well for you lately?"],
    "quit": ["It was nice talking to you. Take care!", "Goodbye! Don't hesitate to reach out if you need to talk."]
}

# Define a function to generate a response based on user input
def generate_response(input_text):
    # Remove punctuation and convert to lowercase
    input_text = input_text.lower().strip('!,.?')

    # Iterate through the keywords and check if they appear in the input text
    for keyword in keywords:
        if keyword in input_text:
            return random.choice(keywords[keyword])
    
    # If no keyword was found, return a generic response
    return "I'm sorry, I don't understand. Can you please rephrase your statement?"

# Initialize user inputs list
user_inputs = []

# Start conversation
print("PsyVBot: Hi! I'm here to listen...")

while True:
    # Get user input
    user_input = input("User: ")

    # Add user input to list
    user_inputs.append(user_input)

    # Check if user wants to end the conversation
    if user_input.lower() == "quit":
        print("PsyVBot:", random.choice(keywords["quit"]))
        # Clear user inputs list
        user_inputs = []
        break

    # Check if user wants to diagnose depression
    if user_input.lower() == "diagnose":
        print("PsyVBot: User inputs: ", user_inputs) # Print user inputs list
        # Check if user has provided enough input to diagnose depression
        if len(user_inputs) < 10:
            print("PsyVBot: Sorry, I need more information to diagnose your condition. Can you tell me more about how you've been feeling?")
            continue
        # Clear user inputs list
        user_inputs = []
        continue

    # Generate response
    response = generate_response(user_input)

    # Print response
    print("PsyVBot:", response)

    # Ask follow-up questions based on the response
    if "how" in response.lower():
        if "how do you feel" not in response.lower(): # Check if response already contains follow-up
            follow_up = input("PsyVBot: How do you feel about that?")
            user_inputs.append(follow_up)
    elif "why" in response.lower():
        if "why do you think" not in response.lower(): # Check if response already contains follow-up
            follow_up = input("PsyVBot: Why do you think that is?")
            user_inputs.append(follow_up)
    elif "tell me more" in response.lower():
        follow_up = input("PsyVBot: Can you elaborate on that?")
        user_inputs.append(follow_up)
    elif "what can i do" in response.lower():
        follow_up = input("PsyVBot: Have you considered talking to a therapist?")
        user_inputs.append(follow_up)