from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import datetime

training_data = [
    ("hi", "greeting"),
    ("hello", "greeting"),
    ("good morning", "greeting"),
    ("hey", "greeting"),

    ("weather today", "weather_query"),
    ("is it raining", "weather_query"),
    ("sunny", "weather_query"),
    ("cloudy", "weather_query"),

    ("what time is it", "time_query"),
    ("time now", "time_query"),
    ("time?", "time_query"),
    ("what's the time on clock?", "time_query"),
    ("clock time", "time_query"),

    ("show my tasks", "view_tasks"),
    ("what's my schedule", "view_tasks"),
    ("what do we have to do today?", "view_tasks"),
    ("today's tasks list", "view_tasks"),
    ("Show my schedule", "view_tasks"),

    ("add buy milk", "add_task"),
    ("remind me to study", "add_task"),
    ("put swimming in the schedule", "add_task"),
    ("remind me to complete my homework by 4", "add_task")
]

texts = [t[0].lower() for t in training_data]
labels = [t[1] for t in training_data]

vectorizer = CountVectorizer()
x = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(x, labels)

tasks = []

def predict_intent(user_input):
    x = vectorizer.transform([user_input])
    return model.predict(x)[0]

def chatbot():

    while True:
        user_input = input("You: ")

        if user_input == "exit":
            break

        intent = predict_intent(user_input)
        
        if intent == "greeting":
            print("Bot: How can I help you?")
        
        elif intent == "time_query":
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print("Bot: Current time is ", current_time)

        elif intent == "weather_query":
            print("Bot: Can't access the weather data right now.")
        
        elif intent == "view_tasks":
            if tasks:
                print("Bot: Today's schedule ")
                for task in tasks:
                    print("- ", task)
            else:
                print("Bot: Today's schedule is empty")
        
        elif intent == "add_tasks":
            task = user_input
            tasks.append(task)
            print("Bot: Schedule has been updated!")

        else:
            print("Bot: Sorry, I don't understand that.")
chatbot()