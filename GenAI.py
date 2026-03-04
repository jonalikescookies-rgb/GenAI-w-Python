import os
from google import genai
from dotenv import load_dotenv

load_dotenv()
apikey = os.getenv("API_Key")
client=genai.Client(api_key=apikey)

def modelchoose():
    while True:
        model_choice = input("Choose Model Number:\n1. Gemini 2.5 Flash \n2.Gemini 3.0 Flash \n3.Gemini 3.1 Pro \nModel Number: ")
        if model_choice == "1":
            return "gemini-2.5-flash"

        elif model_choice == "2":
            return "gemini-3-flash-preview"

        elif model_choice == "3":
            return "gemini-3.1-pro-preview"

        else:
            print("invalide model number")

chosen_model = modelchoose()
        
        

chat = client.chats.create(model= chosen_model)
query =""

while query != "/exit":

    if query == "/exit":
        print("Goodbye")
        break

    query=input("Type Query: ")

    response= chat.send_message(query)

    print("Gemini: ", response.text)