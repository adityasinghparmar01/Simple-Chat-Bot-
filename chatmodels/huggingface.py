from dotenv import load_dotenv
# Load .env file
load_dotenv()

# Using API

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",   # repo id is the id of models in hugging face
    temperature=0.9,
    max_new_tokens=1000,
)
model = ChatHuggingFace(llm=llm)
response = model.invoke("who are you ?")
print(response.content)