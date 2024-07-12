import openai

openai.api_key = "sk-proj-o8f3hfOEwZ3m7RYqemwKT3BlbkFJA1nmM8e8GKw7emMq0Lh"

messages = []
system_msg = input("What is your name?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready!")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")