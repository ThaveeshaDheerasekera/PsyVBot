import random
from afinn import Afinn
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from keras.models import load_model
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

# Define keywords and responses
keywords = {
    "greetings": ["Hello! How are you?",
                  "Hi! I'm here to listen. How are you feeling today?"],
    "positive" : ["That's wonderful news! Can you share more about what happened?",
                   "I'm happy to hear that things are going well for you. What's been making you feel good?",
                   "It's great to see you feeling positive. Can you tell me more about what's been making you feel that way?",
                   "I'm glad to hear that you're feeling happy! Is there anything specific that's made you happy?",
                   "That's great to hear! What's been going well for you lately?"],
    "negative": ["I'm sorry to hear that. Would you like to talk about it?",
                 "That sounds difficult. How have you been coping with it?",
                 "I'm here to listen. Do you want to talk about what's been bothering you?",
                 "It's okay to not be okay. I'm here to listen. What's been on your mind?"],
    "neutral" : ["I see. Can you tell me more about that?",
                 "Interesting. Can you elaborate on what you mean?",
                 "Okay. Can you give me more details about that?"],
    "quit": ["It was nice talking to you. Take care!", 
             "Goodbye! Don't hesitate to reach out if you need to talk."]
}

greetings = ['hello', 'hi', 'hey', 'howdy', 'heyy']

# Define a list of follow-up questions
follow_ups = [
    "Can you tell me more about that?",
    "How did that make you feel?",
    "What do you think caused that?",
    "Have you experienced this before?",
    "What do you think could help?",
]

# Initialize sentiment analyzer and AFINN lexicon
sid = SentimentIntensityAnalyzer()
afinn = Afinn()

# Function to generate response based on user input
def generate_response(user_input):
    # Check if the user input is a greeting
    if user_input.lower() in greetings:
        response = random.choice(keywords['greetings'])
    else:
        # Perform sentiment analysis on user input using AFINN lexicon
        sentiment = afinn.score(user_input)
        
        # Generate response based on sentiment
        if sentiment > 0:
            response = random.choice(keywords['positive'])
        elif sentiment < 0:
            response = random.choice(keywords['negative'])
        else:
            response = random.choice(keywords['neutral'])
        
        # If the sentiment is negative, include a follow-up question
        if sentiment < 0:
            response += " " + random.choice(follow_ups)
    
    return response


# Initialize user inputs list
user_inputs = []

# Start conversation with user
print("-------------------------------------------------------------------------------------")
print("---- PsyVBot ----")
print("-------------------------------------------------------------------------------------")
print("-- Important --")
print("\t- Enter \"diagnose\" to get a diagnosis")
print("\t- Enter \"exit\" to exit the chatbot. (This option will NOT provide a diagnosis)")
print("-------------------------------------------------------------------------------------")
print("PsyVBot: Hi! I'm here to listen...")

while True:
    # Get user input
    user_input = input("User: ")

    # Check if user wants to end the conversation
    if user_input.lower() == "quit":
        print("PsyVBot:", random.choice(keywords["quit"]))
        # Clear user inputs list
        user_inputs = []
        break

    # Check if user wants to diagnose depression
    if user_input.lower() == "diagnose":
        # Check if user has provided enough input to diagnose depression
        if len(user_inputs) < 10:
            print("PsyVBot: Sorry, I need more information to diagnose your condition. Can you tell me more about how you've been feeling?")
        else:
            # Print user inputs list
            print("PsyVBot: User inputs: ", user_inputs)

            # Define the maximum number of words to keep based on the size of your vocabulary
            max_words = 20000
            tokenizer = Tokenizer(num_words=max_words)

            # Fit the tokenizer on your input list
            tokenizer.fit_on_texts(user_inputs)

            # Convert the input list into numerical sequences using the tokenizer
            sequences = tokenizer.texts_to_sequences(user_inputs)

            # Pad the sequences to ensure they all have the same length
            max_len = 100
            padded_sequences = pad_sequences(sequences, maxlen=max_len)

            # Load the saved model from the .h5 file
            from keras.models import load_model
            model = load_model('my_model.h5')

            # Make a prediction on the padded sequences
            predictions = model.predict(padded_sequences)

            # Round the predictions to get binary classification labels
            binary_predictions = [round(pred[0]) for pred in predictions]

            # Determine the prediction for the current user input
            input_sequences = tokenizer.texts_to_sequences([user_input])
            padded_input_sequences = pad_sequences(input_sequences, maxlen=max_len)
            input_predictions = model.predict(padded_input_sequences)
            binary_input_predictions = [round(pred[0]) for pred in input_predictions]
            print("PsyVBot: Based on the information you've provided, it appears that you are", "depressed" if any(binary_input_predictions) else "not depressed", "with a confidence level of", max(binary_predictions))
        
        break

    # Check if user input is empty
    if user_input.strip() == "":
        print("PsyVBot: Please say something.")
        continue

    # Add user input to list
    user_inputs.append(user_input)

    # Generate response
    response = generate_response(user_input)

    # Print response
    print("PsyVBot:", response)
