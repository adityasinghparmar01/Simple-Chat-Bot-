from langchain_huggingface import HuggingFaceEmbedddings 

embedding = HuggingFaceEmbedddings(
    model = "sentence-transformers/all-MiniLM-L6-v2"
)
texts = [
    "hello this adi",
    "hello your name is yt",
    "and i am fine"
]
vector = embedding.embed_documents(texts)  
print(vector)
# this creates a 384 dimension dense vector of each sentence