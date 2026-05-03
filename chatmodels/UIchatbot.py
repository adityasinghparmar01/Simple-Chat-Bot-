# always make your streamlit UI file from chatgpt -> by giving your orginial file like here chatbot.py
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

# Page config
st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="centered")

# Custom styling
st.markdown("""
    <style>
        .chat-box {
            padding: 12px;
            border-radius: 12px;
            margin-bottom: 10px;
            font-size: 16px;
            font-weight: 500;
        }

        .user {
            background-color: #DCF8C6;
            color: black;
            text-align: right;
        }

        .bot {
            background-color: #8B4513;   /* Brown */
            color: white;                /* White text */
            text-align: left;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 AI Chatbot")

# Initialize model
model = ChatMistralAI(model="mistral-small-2506", temperature=0.9)

# Mode selection
mode_option = st.selectbox(
    "Choose your AI Mode:",
    ["Angry 😡", "Funny 😂", "Sad 😢"]
)

# Map mode
if mode_option == "Angry 😡":
    mode = "you are an angry AI agent, You respond aggressively and impatiently"
elif mode_option == "Funny 😂":
    mode = "you are a funny AI agent, You respond with humor and jokes"
else:
    mode = "you are a sad AI agent, You respond in a depressed and emotional tone"

# Initialize session state
if "messages" not in st.session_state or st.session_state.get("mode") != mode:
    st.session_state.mode = mode
    st.session_state.messages = [
        SystemMessage(content=mode)
    ]

# Display chat
st.subheader("Chat")

for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        st.markdown(f"<div class='chat-box user'>You: {msg.content}</div>", unsafe_allow_html=True)
    elif isinstance(msg, AIMessage):
        st.markdown(f"<div class='chat-box bot'>Bot: {msg.content}</div>", unsafe_allow_html=True)

# Input
user_input = st.text_input("Type your message:")

col1, col2 = st.columns([1, 1])

with col1:
    send = st.button("Send")

with col2:
    clear = st.button("Clear Chat")

# Send logic
if send and user_input:
    st.session_state.messages.append(HumanMessage(content=user_input))

    response = model.invoke(st.session_state.messages)

    st.session_state.messages.append(AIMessage(content=response.content))

    st.rerun()

# Clear chat
if clear:
    st.session_state.messages = [SystemMessage(content=mode)]
    st.rerun()