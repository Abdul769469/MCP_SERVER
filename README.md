# 📺 YouTube Video RAG Chatbot

A smart AI system that watches YouTube videos for you and answers 
any questions about the video content using **Groq Cloud AI**!

---

## 🎯 What Does This Project Do?

1. You paste any YouTube video URL
2. The system automatically fetches the video transcript
3. It creates a smart summary of the whole video
4. You can then chat and ask any question about the video!

---

## 🏆 Key Features

- 🎬 Automatically extracts YouTube video transcripts
- 📝 Generates structured video summaries
- 💬 Interactive Q&A chatbot about the video
- 🧠 Uses RAG (Retrieval Augmented Generation)
- ⚡ Powered by Groq Cloud for super fast responses

---

## 🛠️ Technologies Used

| Tool | Purpose |
|------|---------|
| Python | Main programming language |
| Groq Cloud API | Fast AI responses |
| LangChain | RAG pipeline framework |
| FAISS | Vector search database |
| HuggingFace Embeddings | Text embeddings |
| YouTube Transcript API | Fetch video transcripts |
| Google Colab | Development environment |

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-00A36C?style=for-the-badge&logo=langchain&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-FF6B35?style=for-the-badge&logo=groq&logoColor=white)


YouTube URL
↓
Fetch Transcript
↓
Split into Chunks
↓
Create Vector Embeddings
↓
Store in FAISS Database
↓
User asks a Question
↓
Find Relevant Chunks
↓
Send to Groq AI
↓
Get Smart Answer! 🤖


---

## 🚀 How To Run

### Step 1 — Open Google Colab
Go to colab.research.google.com

### Step 2 — Add your Groq API Key
In Colab click the 🔑 key icon on the left
Add a secret called:
Paste your key from console.groq.com

### Step 3 — Install all libraries
```python
pip install langchain langchain-community langchain-groq langchain-core \
            langchain-text-splitters faiss-cpu sentence-transformers \
            youtube-transcript-api
```

### Step 4 — Paste your YouTube URL
```python
YOUTUBE_URL = "https://youtu.be/your-video-id"
```

### Step 5 — Run all cells in order!

---

## 💬 How To Use The Chatbot

After running all cells you will see:

Then you can:
- Type any question about the video
- Type **summary** to see the full summary
- Type **quit** to exit

Example questions:
---

## 📋 Video Summary Format

The AI generates a structured summary with:

- 🎯 Main Topic
- 🔑 Key Points
- 💡 Important Insights
- 📌 Conclusion

---

## 🔑 Get Your Free Groq API Key

1. Go to console.groq.com
2. Sign up for free
3. Click API Keys and Create API Key
4. Add it to Google Colab secrets

---

## 💼 Skills Demonstrated

- RAG system design and implementation
- LangChain pipeline building
- Vector embeddings and FAISS search
- YouTube API integration
- Prompt engineering
- Conversational AI chatbot
- Google Colab development

---

## 👨‍💻 Built By

Abdul — AI and Data Science enthusiast 🚀



---

## 🧠 How It Works
