def chatbot_response(user_input):
    # Convert input to lowercase to make the matching case-insensitive
    user_input = user_input.lower()

    # Greetings
    if user_input in ["hi", "hello", "hey"]:
        return "Hello! How can I assist you today?"

    # Farewells
    elif user_input in ["bye", "goodbye", "see you"]:
        return "Goodbye! Have a great day!"

    # Inquiries
    elif "how are you" in user_input:
        return "I'm a chatbot, so I don't have feelings, but I'm here to help you!"

    elif "what is your name" in user_input:
        return "I'm ChatBot, your virtual assistant."

    elif "tell me a joke" in user_input:
        return "Why did the computer show up at work late? It had a hard drive!"

    # Default response for unrecognized inputs
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

def main():
    print("ChatBot: Hello! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("ChatBot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    main()
