import datetime

def rule_based_chatbot():
    print("=" * 50)
    print("🤖 Rule-Based AI Chatbot (CLI Version)")
    print("Goal: Responds to predefined user inputs using if-else logic.")
    print("Type 'bye', 'exit', or 'quit' to end the chat loop.")
    print("=" * 50)
    print("\nBot 🤖: Hello! I am your rule-based AI assistant. How can I help you today?\n")

    # Continuous Loop as specified in requirements
    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nBot 🤖: Goodbye! Session ended.")
            break

        if not user_input:
            continue

        text = user_input.lower()

        # Decision-making logic using IF-ELSE control flow
        if text in ["hello", "hi", "hey", "greetings", "good morning", "good evening"]:
            print("Bot 🤖: Hello there! 👋 Welcome! How can I assist you today?\n")

        elif text in ["bye", "exit", "quit", "goodbye", "see ya"]:
            print("Bot 🤖: Goodbye! 👋 Have a great day!\n")
            print("Chat loop terminated by exit command.")
            break  # Exit continuous loop

        elif "how are you" in text or "how do you do" in text:
            print("Bot 🤖: I'm doing great, thank you for asking! 😊 Ready for your questions.\n")

        elif "name" in text or "who are you" in text:
            print("Bot 🤖: My name is RuleBot! I operate on rule-based decision-making logic.\n")

        elif "help" in text or "what can you do" in text:
            print("Bot 🤖: Here are some commands you can try:")
            print("  - Greetings ('hello', 'hi')")
            print("  - Identity ('what is your name')")
            print("  - Status ('how are you')")
            print("  - Jokes ('tell me a joke')")
            print("  - Time ('what time is it')")
            print("  - Exit ('bye', 'exit')\n")

        elif "joke" in text or "funny" in text:
            print("Bot 🤖: Why do programmers prefer dark mode? Because light attracts bugs! 🐛😂\n")

        elif "time" in text or "clock" in text:
            now_str = datetime.datetime.now().strftime("%I:%M %p")
            print(f"Bot 🤖: The current time is 🕒 {now_str}.\n")

        else:
            print("Bot 🤖: I'm sorry, I don't understand that command yet 🤔. Type 'help' to see what I can do!\n")

if __name__ == "__main__":
    rule_based_chatbot()
