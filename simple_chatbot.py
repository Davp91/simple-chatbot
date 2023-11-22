def chatbot():
    print("Welcome to the chatbot! Type 'quit' to exit.")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "quit":
            print("Chatbot: Goodbye!")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello there!")
        elif "how are you" in user_input:
            print("Chatbot: I'm a bot, so I'm always functioning as expected!")
        elif "your name" in user_input:
            print("Chatbot: I am a simple Python Chatbot.")
        elif "weather" in user_input:
            print("Chatbot: I'm not sure about the weather, but it's always sunny in the digital world!")
        elif "age" in user_input:
            print("Chatbot: Sorry, I do not age")
        else:
            print("Chatbot: Sorry, I don't understand that.\nPlease ask me about my name, or the weather")

if __name__ == "__main__":
    chatbot()
