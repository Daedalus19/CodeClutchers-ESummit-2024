from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
import streamlit as st
import modelCreation
import os
import transcribe

st.title("VidVibe")

vid_link = st.text_input("Enter a YouTube video link:", key="vid_link")

if not vid_link:
    st.warning("Please enter a YouTube video link to proceed.")
    st.stop()

if "is_transcribed" not in st.session_state:
    st.session_state.is_transcribed = False

if not st.session_state.is_transcribed:
    transcribe.yt_download(vid=vid_link)
    transcript = transcribe.transcribe()
    transcribe.write_file(text=transcript)

    with open("assets\\transcribe.txt") as file:
        context = file.read()

    modelCreation.create_chat_model(context=context, vid_link=vid_link)
    os.system('ollama create vidvibe -f ./Vidvibe')

    st.session_state.is_transcribed = True

template = """Question: {question}

Answer: """

model = OllamaLLM(model="vidvibe")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

if "history" not in st.session_state:
    st.session_state.history = []

question = st.chat_input("Text")

if question:
    answer = chain.invoke({"question": question})
    st.session_state.history.append({"question": question, "answer": answer})

for i, entry in enumerate(st.session_state.history):
    st.write(f"*You :* {entry['question']}")
    st.write(f"*VidVibe :* {entry['answer']}")