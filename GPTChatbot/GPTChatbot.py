import io
import os
import requests

def chat(message):
    """Chats with the user using ChatGPT."""
    response = requests.post("https://api.openai.com/v1/engines/chatGPT/completions",
                             headers={"Authorization": "Bearer Insert Your OWN API key here!"},
                             data={"prompt": message})
    if response.status_code == 200:
        return response.json()["choices"][0]["text"]
    else:
        return "An error occurred."

if __name__ == "__main__":
    print("Welcome to the ChatGPT chatbot!")
    while True:
        message = input("Enter your message: ")
        response = chat(message)
        print(response)
