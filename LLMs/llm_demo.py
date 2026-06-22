from dotenv import load_dotenv

load_dotenv()

#from langchain_openai import OpenAI
from langchain.chat_models import init_chat_model

llm = init_chat_model("google_genai:gemini-3.5-flash")

result = llm.invoke("Hi, what's your name?")

print(result.content[0]['text'])