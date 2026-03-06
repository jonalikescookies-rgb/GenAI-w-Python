import os
import sys
from google import genai
from dotenv import load_dotenv

load_dotenv()
apikey = os.getenv("API_KEY")
client=genai.Client(api_key=apikey)


def modelchoose():
    while True:
        model_choice = input("Choose Model:\nGemini (2.5) Flash \nGemini (3.0) Flash \nGemini (3.1) Pro \nGemini Version: ")
        if model_choice == "2.5":
            return "Gemini 2.5 flash", "gemini-2.5-flash"

        elif model_choice == "3.0":
            return "Gemini 3.0 flash", "gemini-3-flash-preview"
        elif model_choice == "3.1":
            return "Gemini 3.1 pro", "gemini-3.1-pro-preview"
        elif model_choice == "exit" or model_choice == "/exit":
            print("Goodbye")
            sys.exit()
        else:
            print("invalid model")


model_name, chosen_model = modelchoose()

chat = client.chats.create(
    model= chosen_model,
    config={
        "system_instruction": "respond in plain text only. Do not use markdown or stars (**). Always use the metric system. The Users name is Admin."
    }                           )



query =""

print("\n—> starting Chat with ", model_name, "<—")

while True:
    query=input("\nType Query: ")
    if query == "/exit" or query == "exit":
        print("Goodbye")
        break
    print("\nGemini: ", end="", flush=True)

    response_stream= chat.send_message_stream(query)
    for chunk in response_stream:
        print(chunk.text, end="", flush=True)

    print()
