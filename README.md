# 🤖 HelpWise AI – Customer Support Chatbot

HelpWise AI is an AI-powered chatbot that answers product-related questions about a fictional SaaS tool using LLMs and a knowledge base.

---

## 💡 Features
- 💬 Smart Chatbot with context memory
- 📚 Knowledge base-driven answers
- 🧠 LLM-powered (Flan-T5)
- 🔁 Resettable chat history
- 🌐 Multilingual Support

---

## ⚙️ Setup Instructions

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
## 🧱 System Architecture
Frontend: Streamlit for chat UI

Backend: LangChain with Flan-T5 from HuggingFace

Embedding: all-MiniLM-L6-v2

Vectorstore: FAISS

Analytics: Logs queries to analytics/log.json

Context: Previous questions retained using session state
## ✨ Prompt Engineering Approach
Uses semantic search to match user queries with relevant docs

LLM (Flan-T5) generates concise answers from retrieved content

Context history enables natural follow-up conversations
## 🚫 Limitations
Not connected to live APIs or databases

Limited fallback handling (basic response for unknowns)

Static knowledge base (manually updated)
## 🔮 Future Improvements
Add feedback mechanism (Was this helpful?)

Admin dashboard for analytics

Deploy with Docker or Streamlit Cloud

Expand multilingual capabilities
