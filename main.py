'''
Main Code runner
'''

import os
import transcribe
import summarizer
import modelCreation

vid_link = input("Enter the vid link : ")
transcribe.yt_download(vid=vid_link)
transcript = transcribe.transcribe()
transcribe.write_file(text=transcript)

summary = summarizer.summary()

with open("assets\\transcribe.txt") as file:
    context = file.read()

modelCreation.create_chat_model(context=context,vid_link=vid_link)

os.system('ollama create vidvibe -f ./Vidvibe')

os.system("streamlit run st_app.py")