def chatbot_response(user_input):
    # Convert input to lowercase to make matching case-insensitive
    user_input = user_input.lower().strip()
    
    if "hello" in user_input or "hi" in user_input:
        return "Hi!"
    elif "how are you" in user_input:
        return "I'm fine, thanks!"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye!"
    else:
        return "I'm sorry, I don't understand that. Try asking 'hello', 'how are you', or 'bye'."

def main():
    print("Chatbot: Hello! Type 'bye' to exit the conversation.")
    
    # Loop to continuously handle user input
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")
        
        # Exit the loop if the user says bye
        if "bye" in user_input.lower():
            break

if __name__ == "__main__":
    main()