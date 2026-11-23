import os
from pathlib import Path
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

INFO_FILE = Path(__file__).parent / "college_info.txt"

st.set_page_config(page_title="College Enquiry Chatbot", page_icon="🎓")
st.title("🎓 College Enquiry Chatbot")
st.caption("Ask about courses, fees, admissions, facilities and contact information.")


def load_college_info():
    if not INFO_FILE.exists():
        return ""
    return INFO_FILE.read_text(encoding="utf-8")


college_info = load_college_info()
api_key = os.getenv("GROQ_API_KEY")

if not college_info.strip():
    st.error("college_info.txt is missing or empty. Add college information and restart the app.")
    st.stop()
if not api_key:
    st.info("Set your Groq API key in the .env file to start chatting.")
    st.stop()

client = Groq(api_key=api_key)
SYSTEM_PROMPT = f"""You are a helpful college enquiry assistant. Answer student questions using ONLY the college information below.
Do not use outside knowledge, guess, or invent facts. If the answer is not found in the information, say: 'Sorry, this information is not available in the college information provided. Please contact the college office.'
Keep answers clear, polite, and concise. If the question is unrelated to the college, politely explain that you can answer college enquiries only.

COLLEGE INFORMATION:
{college_info}
"""

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("About")
    st.write("This chatbot uses the college information file as its source.")
    if st.button("Clear chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    st.caption("Replace the sample college_info.txt with verified college information.")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Ask a college question...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    with st.chat_message("assistant"):
        with st.spinner("Finding the answer..."):
            try:
                response = client.chat.completions.create(
                    model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
                    messages=[{"role": "system", "content": SYSTEM_PROMPT}] + st.session_state.messages,
                    temperature=0.2,
                )
                answer = response.choices[0].message.content or "Sorry, I couldn't generate an answer."
            except Exception as exc:
                answer = f"An error occurred while contacting the LLM API. Check your API key and internet connection. Details: {exc}"
        st.markdown(answer)
    st.session_state.messages.append({"role": "assistant", "content": answer})
