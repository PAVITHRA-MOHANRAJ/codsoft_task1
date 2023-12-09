def get_response(user_input):
    user_input = user_input.lower()

    
    responses = {
        "hi": "Hello!",
        "hello": "How can I help you?",
        
        "how is the weather today?": "It's raining cats and dogs here",
        "can you give me weather report for today?": "Sorry! currently I'm not connected to the weather department",

        "bye": "Goodbye!",
        
        "what's your name?": "I'm a chatbot!",
        "tell me a joke": "Sure, here's one: Why don't scientists trust atoms? Because they make up everything!",
        "how old are you?": "I'm a computer program, so I don't have an age!",
        "what's the weather like today?": "I'm not sure, you might want to check a weather app!",
        "who created you?": "I was created by a team of developers.",
        "what is your favorite color?": "I don't have a favorite color, unfortunately.",
        "do you like pizza?": "I don't have taste buds, but many people enjoy pizza!"
        
    }

    
    if user_input in responses:
        return responses[user_input]
    else:
        return "I'm not sure how to respond to that."


print("Bot: Hi, I'm a rule-based chatbot. Ask me something or say 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Bot: Goodbye!")
        break
    else:
        response = get_response(user_input)
        print("Bot:", response)
