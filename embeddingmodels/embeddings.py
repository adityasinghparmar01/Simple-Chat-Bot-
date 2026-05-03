from dotenv import load_dotenv
# Load environment variables (Api keys) from .env file to this file     
load_dotenv()
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
    model = 'text-embedding-3-large',
    dimensions = 64
    )
# dimensions is the number of dimensions in the vector that we want to create from the text. The higher the dimensions, the more accurate the vector will be but it will also take more time to create the vector. The lower the dimensions, the less accurate the vector will be but it will also take less time to create the vector.

# when you have one sentence that you want to convert into vector then you can use embed_query function and when you have multiple sentences that you want to convert into vector then you can use embed_documents function
texts = [
    "hello this adi",
    "hello your name is yt",
    "and i am fine"
]

# vectors = embeddings.embed_query("you are going to learn gen AI")
vector = embeddings.embed_documents(texts)  
print(vector)

# all these things need money so we go to hugging face
