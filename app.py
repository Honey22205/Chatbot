import streamlit as st
import json
import random

# Load intents and modell
with open("intents.json") as file:
    intents = json.load(file)

# Function to generate chatbot response
def get_bot_response(user_message):
    for intent in intents["intents"]:
        if user_message.lower() in [p.lower() for p in intent["patterns"]]:
            return random.choice(intent["responses"])
    return "Sorry, I don't understand that."

# Streamlit UI
def main():
    # Set title and description for the app
    st.title("Chatbot")
    st.write("Ask me anything!")

    # Get user input from Streamlit's text input widget
    user_message = st.text_input("You: ", "")

    if user_message:
        # Get chatbot response
        bot_response = get_bot_response(user_message)

        # Display the conversation
        st.write(f"**You:** {user_message}")
        st.write(f"**Bot:** {bot_response}")

if __name__ == "__main__":
    main()
