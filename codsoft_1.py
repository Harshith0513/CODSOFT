from datetime import date, datetime

def greet():
    return "chatbot: hi! how can I help you?"

def get_name():
    return "chatbot: my name is chatbot."

def get_date():
    today_date = date.today()
    return f"chatbot: today's date is {today_date}"

def get_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    return f"chatbot: now the time is {current_time}"

def handle_input(user_input):
    responses = {
        "hi": greet,
        "what is your name": get_name,
        "what is the date today": get_date,
        "what is the time now": get_time,
        "bye": lambda: "chatbot: bye!"
    }
    
    return responses.get(user_input, lambda: "chatbot: sorry!...I didn't understand")()

def chatbot():
    while True:
        user_input = input("\nuser: ").strip().lower()
        response = handle_input(user_input)
        print(response)
        if user_input == "bye":
            break

chatbot()