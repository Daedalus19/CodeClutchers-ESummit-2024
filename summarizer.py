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

