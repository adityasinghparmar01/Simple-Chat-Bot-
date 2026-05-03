from dotenv import load_dotenv
# Load environment variables (Api keys) from .env file to this file 
load_dotenv()

#in langchain -> langchain -> models -> chat_models  OR   model class -> init_chat_model.py
# you can choose difernet models from langchain -> models -> chat_models and then import the model you want to use in this file and then initialize the model and then you can use the model to get the response from the model by passing the question to the invoke function of the model

# from langchain.chat_models import init_chat_model
# # this is the function to initialize the chat model and we can specify the model name and other parameters in this function 
# model = init_chat_model("gpt-4.10")

# OR     -> model class is different is different fro init_chat_model in this we import asingle specific model and then initialize the model and then use the model to get the response from the model by passing the question to the invoke function of the model  

# from langchain_openai import ChatOpenAI
# model = ChatOpenAI(model="gpt-4.10")
 

# model = init_chat_model("google_genai:gemini-2.5-flash-lite")

# grok
# model = init_chat_model("groq:openai/gpt-oss-120b")

# from langchain_groq import ChatGroq
# model = ChatGroq(model="openai/gpt-oss-120b")

# now mistral model is free to use
from langchain_mistralai import ChatMistralAI
model = ChatMistralAI(model="mistral-small-2506" , temperature=0.9 , max_tokens=1000)
# temperature is a parameter that controls the randomness of the response from the model. The higher the temperature, the more random the response will be. The lower the temperature, the more deterministic the response will be.
# lower temp -> mathematical and logical questions
# higher temp -> creative and open ended questions like poetry, story writing, etc.

# max_tokens is a parameter that controls the maximum number of tokens that the model can generate in the response. The higher the max_tokens, the longer the response will be. The lower the max_tokens, the shorter the response will be.
# max_token matlab number of words 


response = model.invoke("give me a paragraph on ML")
# you have to save your question in a variable and then pass it to the invoke function to get the response from the model

print(response.content)