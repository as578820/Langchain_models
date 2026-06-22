from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = HuggingFaceEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2"
)
documents = [
    "Delhi is capital of India",
    "Kolkata is capital of west bengal",
    "Paris is capital of France"
]

result = embedding.embed_documents(documents)

print(len(result))
print(result)