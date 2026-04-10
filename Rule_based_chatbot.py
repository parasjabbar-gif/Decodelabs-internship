# Rule-Based AI Chatbot
# Project 1 - DecodeLabs Internship

print("🤖 Chatbot: Hello! I am your AI assistant.")
print("Type 'exit' to end the chat.\n")

while True:
    user_input = input("You: ").lower()   # input convert into lowercase

    # Exit condition
    if user_input == "exit" or user_input == "bye":
        print("🤖 Chatbot: Goodbye! Have a nice day 😊")
        break

    # Greetings
    elif user_input == "hi" or user_input == "hello":
        print("🤖 Chatbot: Hello! How can I help you?")

    # Asking about chatbot
    elif user_input == "how are you":
        print("🤖 Chatbot: I am fine, thank you! 😊")

    # Name question
    elif user_input == "your name":
        print("🤖 Chatbot: I am a Rule-Based AI Chatbot 🤖")

    # Help command
    elif user_input == "help":
        print("🤖 Chatbot: You can say 'hi', 'how are you', or 'bye' to exit.")

    # Default response
    else:
        print("🤖 Chatbot: Sorry, I don't understand that. Please try something else.")