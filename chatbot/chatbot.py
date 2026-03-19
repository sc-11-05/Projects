import datetime

tasks = []

# identifying the intent of the user
def classify_intent(user_input):
    text = user_input.lower()

    if any(word in text for word in ["add", "remind", "create"]):
        return "add_task"

    elif any(word in text for word in ["show", "list", "schedule", "tasks"]):
        return "view_tasks"

    elif any(word in text for word in ["weather", "rain", "sunny", "cloudy"]):
        return "weather_query"

    elif any(word in text for word in ["time", "clock", "hour", "minute"]):
        return "time_query"

    elif any(word in text for word in ["hello", "hi", "hey"]):
        return "greeting"

    else:
        return "unknown"

def greeting():
    print ("Bot: Hi there, How may I help you.")

def time_query():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"Bot: Current time is {current_time}")

def weather_query():
    print("Bot: Weather feels nice")

def add_task(user_input):
    # task = user_input.replace("add", "").replace("remind", "").strip()
    # tasks.append(task)
    text = user_input

    if "add" in text:
        task = text.split("add",1)[1]
    elif "remind me to" in text:
        task = text.split("remind me to", 1)[1]
    
    else:
        task = text

    task = task.strip()
    tasks.append(task)
    print(f"Bot: '{task}' has been added to your schedule")

def view_tasks():
    if tasks:
        print("Bot: Today's schedule: ")
        for t in tasks:
            print("-" + t)
    else:
        print("Bot: No schedule allotted")

def chatbot():
    while True:

        user_input = input("You: ").lower()

        if user_input == "exit":
            break
            
        intent = classify_intent(user_input)

        if intent == "greeting":
            greeting()
        
        elif intent == "time_query":
            time_query()

        elif intent == "weather_query":
            weather_query()

        elif intent == "add_task":
            add_task(user_input)
        
        elif intent == "view_tasks":
            view_tasks()
        
        else:
            print("Sorry, I didn't understand that.")
            

chatbot()