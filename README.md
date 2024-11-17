# VidVibe

# 🚀 YouTube Video Summarizer & Interactive Chat Session  

[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-orange)](https://streamlit.io/)  
[![Hugging Face](https://img.shields.io/badge/Powered%20by-Hugging%20Face-yellow)](https://huggingface.co/)  

Transform long YouTube videos into concise summaries and engage in context-aware interactive chat sessions—all running locally!  

---

## 🧐 What is it?  

This project revolutionizes content consumption by:  
1. **Automatically transcribing YouTube videos** using state-of-the-art AI models.  
2. **Summarizing** lengthy content into digestible insights.  
3. Enabling **chat sessions** where you can ask questions about the video’s content in real-time.  

---

## ✨ Key Features  

- **Accurate Transcriptions**: Powered by Hugging Face's Whisper model, ensuring reliable and multilingual transcription.  
- **Interactive Chat**: A custom Llama 3.2 model from Ollama responds intelligently to your questions.  
- **Characters**: Custom characters can be added for a more engaging experience.
- **Streamlit Frontend**: User-friendly interface for seamless interaction.  
- **Local Execution**: Complete privacy as everything runs on your machine.  
- **Scalable Architecture**: Ready to integrate PDFs, podcasts, and more formats in the future.  

---

## 💡 How It Works  

1. **Fetch and Process Video**:  
   - You input a YouTube video URL.  
   - The audio is downloaded using the Pytube library.  

2. **Transcription**:  
   - Hugging Face Whisper model transcribes the audio into text.  

3. **Summarization**:  
   - The transcription is summarized for quick insights.  

4. **Chat Session**:  
   - Engage in a real-time Q&A session using a locally-hosted Llama 3.2 model.  
   - Ask questions based on the summarized/transcribed content.  

---

## 🚀 Quickstart  

### Prerequisites  
- Python 3.8+  
- Hugging Face Transformers Library  
- Streamlit  
- Ollama (Llama 3.2 setup)  

### Installation  

1. **Clone the repository**  
   ```bash  
   git clone https://github.com/Daedalus19/CodeClutchers-ESummit-2024.git 
   cd CodeClutchers-ESummit-2024``` 

2. **Install dependencies**

    ```bash
    Copy code
    pip install -r requirements.txt```

3. **Start the application**

    ```bash
    Copy code
    streamlit run st_app.py```  

4. **Usage**

    - Input a YouTube link into the interface.
    - Wait for transcription and summarization.
    - Start asking questions in the chat session.

---

## 🛠️ Tech Stack

- **Backend:**

    - Pytube for audio extraction.
    - Hugging Face Whisper Model for transcription.
    - Ollama's Llama 3.2 for custom chat responses.

- **Frontend:**

    - Streamlit for a lightweight, interactive user interface.

---

## 🌟 Why This Project Matters
- **Time-Efficiency:** Skip hours of video watching by jumping straight to relevant content.
- **Privacy-First:** No data leaves your local environment.
- **Scalable Potential:**
    - Integrate more formats (PDFs, podcasts, etc.)
    - Expand to multiple languages and regional markets.

---

## 🛣️ Roadmap
1. **Multi-Language Support:** Enable transcription and chat in more languages.
2. **Advanced Summarization:** Use topic clustering and sentiment analysis.
3. **Cloud Support:** Provide a hybrid option for faster processing.
4. **Enterprise Features:**
    - API access for businesses.
    - Collaboration tools for teams.

---

## 📊 Investor Potential
- **Target Market:**

    - Content creators, students, professionals, and educators.
    - Massive market for video summarization and interactive AI tools.

- **Revenue Opportunities:**

    - Freemium model with premium features.
    - Subscription services.
    - B2B licensing and integrations.

- **Scalability:**

    - Add support for additional formats (PDFs, podcasts).
    - Expand into regional markets with language localization.

---

## 👨‍💻 Contact
For inquiries, suggestions, or investment opportunities:
Email: susmitghosh09@gmail.com
LinkedIn: [Susmit Ghosh](https://www.linkedin.com/in/ghoshsusmit/)
GitHub: [Daedalus](https://github.com/Daedalus19)
