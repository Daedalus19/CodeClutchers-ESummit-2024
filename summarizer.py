
'''
    using Pegasus model from Hugging face
'''


# its slow
from transformers import pipeline

pipe = pipeline("summarization", model="google/pegasus-large")

def chunk_text(text, chunk_size=512):
    words = text.split()
    return [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]



with open("assets\\transcribe.txt", "r") as file:
    context = file.read()
context_chunks = chunk_text(context)

for text in context_chunks:
    print(pipe(text))



'''
    Using ollama llama3.2 and langchain  
'''

# Make a 2nd model using llama to summarise text

from langchain_ollama import OllamaLLM

def summary():
    model = OllamaLLM(model="llama3.2")

    with open("assets\\transcribe.txt") as file :
        prompt = file.read()

    prompt = "Summarise this : " + prompt 
    result = model.invoke(input=prompt)
    
    with open("assets\\summary.txt","w") as fileObject :
        fileObject.write(result)

if __name__ == "__main__":
    summary()
    