'''
Used for creating the custom model file
'''

import os

def create_chat_model(context:str, vid_link:str):
    details=f'''
FROM llama3.2

PARAMETER temperature 0.8

SYSTEM """
Answer all questions, based ONLY on the given context. If the answer is not present, say so.
This is a transcribed youtube video : {vid_link}. 
context : {context}
"""'''

    with open("Vidvibe","w") as file:
        file.write(details)


if __name__ == "__main__":
    with open("assets\\transcribe.txt") as file:
        context = file.read()
    
    create_chat_model(context)
    os.system('ollama create vidvibe -f ./Vidvibe')
