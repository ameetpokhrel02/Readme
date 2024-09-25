import random

# Define a dictionary of intents and responses
intents = {
    'greeting': ['Hello!', 'Hi!', 'Hey!'],
    'goodbye': ['Goodbye!', 'See you later!', 'Farewell!'],
    'thanks': ['You\'re welcome!', 'No problem!', 'Thank you too!'],
    'unknown': ['I didn\'t understand that.', 'Can you please rephrase?', 'Sorry, I\'m not sure what you mean.']
}

# Define a function to respond to user input
def respond(user_input):
    # Tokenize the user input
    tokens = user_input.split()

    # Check for exact matches
    if user_input.lower() in ['hello', 'hi', 'hey']:
        return random.choice(intents['greeting'])
    elif user_input.lower() in ['goodbye', 'bye', 'see you later']:
        return random.choice(intents['goodbye'])
    elif user_input.lower() in ['thanks', 'thank you']:
        return random.choice(intents['thanks'])

    # Check for keywords
    for token in tokens:
        if token.lower() in ['hello', 'hi', 'hey']:
            return random.choice(intents['greeting'])
        elif token.lower() in ['goodbye', 'bye', 'see you later']:
            return random.choice(intents['goodbye'])
        elif token.lower() in ['thanks', 'thank you']:
            return random.choice(intents['thanks'])

    # If no match, return a random unknown response
    return random.choice(intents['unknown'])

# Test the chatbot
while True:
    user_input = input('You: ')
    response = respond(user_input)
    print('Chatbot:', response)