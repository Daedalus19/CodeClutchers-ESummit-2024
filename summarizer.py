'''
    Using ollama llama3.2 and langchain  
'''

from langchain_ollama import OllamaLLM

def summary():
    model = OllamaLLM(model="llama3.2")

    with open("assets\\transcribe.txt") as file :
        prompt = file.read()

    prompt = "Summarise this, keeping the important points : " + prompt 
    result = model.invoke(input=prompt)
    
    with open("assets\\summary.txt","w") as fileObject :
        fileObject.write(result)

if __name__ == "__main__":
    summary()
    