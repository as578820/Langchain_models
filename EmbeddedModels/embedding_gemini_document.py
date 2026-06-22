from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)

documents = [
    "Delhi is capital of India",
    "Kolkata is capital of west bengal",
    "Paris is capital of France"
]

result = embedding.embed_documents(documents)

print(len(result))
print(result)