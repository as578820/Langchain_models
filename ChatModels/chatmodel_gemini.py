from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

response = model.invoke("Who was president of India in 2020?")

print(response.content)