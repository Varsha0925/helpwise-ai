import streamlit as st
import json
from datetime import datetime
from run import qa_chain  # Import the QA chain from backend

# Set up Streamlit page
st.set_page_config(page_title="HelpWise AI", page_icon="🤖")
st.title("💬 HelpWise AI - Customer Support Chatbot")
st.markdown("Ask me anything about **HelpWise AI** features like Auto-FAQ, Smart Chatbot, Analytics, Multilingual Support, and more!")

# Function to log basic analytics
def log_analytics(question, category="general"):
    log_data = {
        "timestamp": datetime.now().isoformat(),
        "question": question,
        "category": category
    }
    with open("analytics/log.json", "a") as logfile:
        logfile.write(json.dumps(log_data) + "\n")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Reset chat functionality
if st.button("🔁 Reset Chat"):
    st.session_state.chat_history = []
    st.rerun()

# User input
user_query = st.text_input("Ask your question about HelpWise AI:")

# Process user query
if user_query:
    response = qa_chain.run({
        "question": user_query,
        "chat_history": st.session_state.chat_history
    })

    # Fallback mechanism
    if not response or "i don't know" in response.lower() or "i'm not sure" in response.lower():
        response = "❌ Sorry, I couldn't find an answer to that. Please contact support at support@helpwise.ai."

    # Update chat history
    st.session_state.chat_history.append((user_query, response))

    # Log analytics
    log_analytics(user_query, category="feature")  # You can update category based on keyword detection

    # Display current response
    st.markdown(f"**HelpWise AI:** {response}")

# Display chat history
if st.session_state.chat_history:
    st.markdown("---")
    st.markdown("### 📜 Chat History")
    for question, answer in st.session_state.chat_history:
        st.markdown(f"**You:** {question}")
        st.markdown(f"**HelpWise AI:** {answer}")

# Auto-scroll to latest message
st.markdown("<script>window.scrollTo(0, document.body.scrollHeight);</script>", unsafe_allow_html=True)
