def get_response(user_input):
    """Function to return chatbot reply based on user input."""
    user_input = user_input.lower().strip()

    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    elif user_input == "what is your name":
        return "I am a simple chatbot created for a Python task."
    elif user_input == "help":
        return "You can say: hello, how are you, what is your name, bye"
    else:
        return "Sorry, I don't understand that. Type 'help' to see what I can respond to."


def chatbot():
    """Main chatbot loop."""
    print("Chatbot: Hi! I'm a simple rule-based chatbot.")
    print("Chatbot: Type 'bye' anytime to exit the chat.\n")

    while True:
        user_input = input("You: ")

        response = get_response(user_input)
        print("Chatbot:", response)

        # Exit condition
        if user_input.lower().strip() == "bye":
            break


# ------------------- Main Program -------------------
if __name__ == "__main__":
    chatbot()