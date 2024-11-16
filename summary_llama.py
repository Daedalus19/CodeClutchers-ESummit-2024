# Make a 2nd model using llama to summarise text

from langchain_ollama import OllamaLLM

model = OllamaLLM(model="llama3.2")



result = model.invoke(input="")
print(result)