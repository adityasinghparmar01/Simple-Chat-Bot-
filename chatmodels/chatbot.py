from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage , HumanMessage , SystemMessage

model = ChatMistralAI(model="mistral-small-2506" , temperature=0.9 )
# this mistral small 2506 is a free model

# to save chat history -> we make a list messages -> this is short term memory -> disadvantage of storage
print("choose your AI Mode :")
print("press 1 for angry mode")
print("press 2 for funny mode")
print("press 3 for sad mode")
mode_choice = input("Enter your choice :")

if mode_choice == "1":
    mode = "you are an angry AI agent , You respond aggressively and impatiently"
elif mode_choice == "2":
    mode = "you are a funny AI agent , You respond with humor and jokes"
else:
    mode = "you are a sad AI agent , You respond in a depressed and emotional tone"

messages = [
   # SystemMessage(content = "you are afunny AI agent")
    SystemMessage(content = mode) 
]

print("------welcome type 0 to exit the application-------")   

while True:
 
 prompt = input("You :")
 messages.append(HumanMessage(content=prompt))
 if prompt == "0":
        print("Exiting the application...")
        break
 response = model.invoke(messages )
 messages.append(AIMessage(content=response.content))
 print("Bot :", response.content)