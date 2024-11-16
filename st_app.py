from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
import streamlit as st

st.title("VidVibe")

template = """Question: {question}

Answer: """

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="vidvibe")
chain = prompt | model

if "history" not in st.session_state:
    st.session_state.history = []

question = st.chat_input("Text")

if question:
    answer = chain.invoke({"question": question})
    st.session_state.history.append({"question": question, "answer": answer})

for i, entry in enumerate(st.session_state.history):
    st.write(f"**You :** {entry['question']}")
    st.write(f"**VidVibe :** {entry['answer']}")
