from datetime import datetime

def get_day_suffix(day):
    if 11 <= day <= 13:
        return "th"
    else:
        return {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")

def chatbot_response(user_input):
    user_input = user_input.lower()

    # 1. Greetings
    if any(word in user_input for word in ["hi", "hello", "hey"]):
        return "Hello! 😊 Hope you’re having a great day. How can I help you?"

    # 2. Name / Identity
    elif "who are you" in user_input or "your name" in user_input:
        return "I am RuleBot 🤖, a simple rule-based chatbot created using Python."

    # 3. Help / Doubts
    elif "help" in user_input or "clear my doubts" in user_input:
        return "Of course! 👍 You can ask me about Python, time, date, or general questions."

    # 4. Time
    elif "time" in user_input:
        return "Current time is " + datetime.now().strftime("%I:%M:%S %p")

    # 5. Date
    elif "date" in user_input:
        today = datetime.now()
        day = today.day
        suffix = get_day_suffix(day)
        return f"Today's date is {day}{suffix} {today.strftime('%B %Y')}"

    # 6. Day
    elif "day" in user_input:
        return "Today is " + datetime.now().strftime("%A")

    # 7. Python explanation
    elif "what is python" in user_input or "basics of python" in user_input:
        return (
            "Python is a high-level, easy-to-learn programming language. 🐍\n"
            "It is widely used in web development, AI, data science, automation, and more."
        )

    # 8. Goodbye
    elif "bye" in user_input:
        return "Goodbye! 👋 It was nice talking to you. Have a wonderful day! 🌟"

    # Default response
    else:
        return "Sorry 🤔 I didn’t understand that. Please try asking something else."

def run_chatbot():
    print("🤖 RuleBot is Online!")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ")
        response = chatbot_response(user)
        print("RuleBot:", response)

        if "bye" in user.lower():
            break

run_chatbot()
