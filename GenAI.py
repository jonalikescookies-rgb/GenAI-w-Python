import os
import sys
from google import genai
from dotenv import load_dotenv
from google.genai import types
print(r"""
  ██████╗   ██████╗   ██████╗   ██████╗  ██╗      ███████╗
 ██╔════╝  ██╔═══██╗ ██╔═══██╗ ██╔════╝  ██║      ██╔════╝
 ██║  ███╗ ██║   ██║ ██║   ██║ ██║  ███╗ ██║      █████╗
 ██║   ██║ ██║   ██║ ██║   ██║ ██║   ██║ ██║      ██╔══╝
 ╚██████╔╝ ╚██████╔╝ ╚██████╔╝ ╚██████╔╝ ███████╗ ███████╗
  ╚═════╝   ╚═════╝   ╚═════╝   ╚═════╝  ╚══════╝ ╚══════╝

	  ██████╗  ███████╗ ███╗   ██╗  █████╗  ██╗
	 ██╔════╝  ██╔════╝ ████╗  ██║ ██╔══██╗ ██║
	 ██║  ███╗ █████╗   ██╔██╗ ██║ ███████║ ██║
	 ██║   ██║ ██╔══╝   ██║╚██╗██║ ██╔══██║ ██║
	 ╚██████╔╝ ███████╗ ██║ ╚████║ ██║  ██║ ██║
	  ╚═════╝  ╚══════╝ ╚═╝  ╚═══╝ ╚═╝  ╚═╝ ╚═╝
""")


load_dotenv()
apikey = os.getenv("API_KEY")
client=genai.Client(api_key=apikey)


def modelchoose():
    while True:
        model_choice = input("Choose Model Number:\n1. Gemini 2.5 Flash \n2. Gemini 3.1 Flash \n3. Gemini 3.1 Pro \nGemini Version: ").strip()
        if model_choice == "1":
            return "Gemini 2.5 flash", "gemini-2.5-flash"

        elif model_choice == "2":
            return "Gemini 3.1 flash", "gemini-3.1-flash-lite-preview"
        elif model_choice == "3":
            return "Gemini 3.1 pro", "gemini-3.1-pro-preview"
        elif model_choice.lower() == "exit" or model_choice.lower() == "/exit":
            print("Goodbye")
            sys.exit()
        else:
            print("invalid model number")


model_name, chosen_model = modelchoose()

chat = client.chats.create(
    model= chosen_model,
    config={
        "system_instruction": "respond in plain text only. Do not use markdown or stars (**). Always use the metric system. The Users name is Admin.",
        "tools": [
            {
            "google_search": {}
                    }
                    ]
                }   
            )
                                           
        
            



query =""

print("\n—> starting Chat with ", model_name, "<—")

while True:
    query=input("\nType Query: ").strip()
    if query.lower() == "/exit" or query.lower() == "exit":
        print("Goodbye")
        break
    
    if query.lower() == "/clear" or query.lower() == "clear":
        os.system("cls" if os.name == "nt" else "clear")
        continue 
    
    
    
    print("\nGemini: ", end="", flush=True)

    response_stream= chat.send_message_stream(query)
    for chunk in response_stream:
        print(chunk.text, end="", flush=True)

    print()
