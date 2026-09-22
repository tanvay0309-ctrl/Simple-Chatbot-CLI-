"""
Task 8: Simple Rule-Based Chatbot (CLI)
----------------------------------------
A basic chatbot that responds to greetings, FAQs, and simple
conversation using if-elif statements to match keywords in
the user's input.
"""

import random
from datetime import datetime


def get_response(user_input):
    """Return a chatbot response based on keywords in user_input."""
    text = user_input.lower().strip()
    words = text.split()  # for whole-word matching (avoids "yo" matching inside "you")

    # --- Greetings ---
    if any(word in words for word in ["hello", "hi", "hey", "yo"]):
        return random.choice([
            "Hello there! How can I help you today?",
            "Hi! What can I do for you?",
            "Hey! Good to see you."
        ])

    # --- Farewells ---
    elif any(word in text for word in ["bye", "goodbye", "see you", "exit", "quit"]):
        return "Goodbye! Have a great day. 👋"

    # --- How are you ---
    elif "how are you" in text:
        return "I'm just a program, but I'm running smoothly! How about you?"

    # --- Name questions ---
    elif "your name" in text:
        return "I'm ChatBot, a simple rule-based assistant."

    elif "my name is" in text:
        name = text.split("my name is")[-1].strip().title()
        return f"Nice to meet you, {name}!"

    # --- Time / Date ---
    elif "time" in text:
        return f"The current time is {datetime.now().strftime('%H:%M:%S')}."

    elif "date" in text or "today" in text:
        return f"Today's date is {datetime.now().strftime('%Y-%m-%d')}."

    # --- FAQs ---
    elif "what can you do" in text or "help" in text:
        return ("I can chat with you, tell you the time/date, answer a few "
                "FAQs, and respond to greetings. Try asking 'what is your name?' "
                "or 'what is python?'")

    elif "what is python" in text:
        return "Python is a popular, easy-to-read programming language used for many things, including AI!"

    elif "who created you" in text or "who made you" in text:
        return "I was built as a simple Python project using if-elif logic."

    elif "thank" in text:
        return "You're welcome! 😊"

    elif "weather" in text:
        return "Sorry, I can't check live weather, but I hope it's nice outside!"

    # --- Fallback ---
    else:
        return "I'm not sure I understand. Could you rephrase that, or type 'help' to see what I can do?"


def main():
    print("=" * 50)
    print(" Simple Rule-Based Chatbot (type 'quit' to exit)")
    print("=" * 50)

    while True:
        user_input = input("\nYou: ")

        if user_input.lower().strip() in ["quit", "exit", "bye", "goodbye"]:
            print("Bot: Goodbye! Have a great day. 👋")
            break

        response = get_response(user_input)
        print(f"Bot: {response}")


if __name__ == "__main__":
    main()