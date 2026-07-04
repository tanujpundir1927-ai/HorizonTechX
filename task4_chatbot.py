def chatbot():
    print("Chatbot: Hi! I am a simple chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower().strip()
        
        if user_input in ["hi", "hello", "hey"]:
            print("Chatbot: Hello there!")
        elif user_input in ["how are you", "how are you?"]:
            print("Chatbot: I'm fine, thanks! How can I help you?")
        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a nice day!")
            break
        else:
            print("Chatbot: I am not sure how to respond to that. Try saying 'hello'.")

if __name__ == "__main__":
    chatbot()