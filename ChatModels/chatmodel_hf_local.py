from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline

pipe = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    max_new_tokens=100
)

llm = HuggingFacePipeline(pipeline=pipe)

response = llm.invoke(
    "What is the capital of India?"
)

print(response)