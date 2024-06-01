from dotenv import load_dotenv
load_dotenv()  # Loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

# Configure the Generative AI model with the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Initialize the Streamlit app
st.set_page_config(page_title="Suki AI", page_icon=":robot_face:", layout="wide")

# Custom CSS for better visuals
st.markdown("""
    <style>
        .stApp {
            background-color: #f4f4f9;
        }
        .header {
            color: #1f77b4;
            text-align: center;
            font-size: 36px;
        }
        .subheader {
            color: #ff7f0e;
            text-align: left;
            font-size: 24px;
        }
        .user_input {
            border: 2px solid #1f77b4;
            border-radius: 5px;
            padding: 10px;
            width: 100%;
            font-size: 16px;
        }
        .response {
            background-color: #dff0d8;
            padding: 10px;
            border-radius: 5px;
            margin: 5px 0;
        }
        .history {
            background-color: #f0f8ff;
            padding: 10px;
            border-radius: 5px;
            margin: 5px 0;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="header">Gemini API Application</div>', unsafe_allow_html=True)

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input("Input:", key="input", placeholder="Type your question here...", help="Enter your query to get a response from the Gemini API")
submit = st.button("Submit")

if submit and input:
    response = get_gemini_response(input)
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input))
    st.markdown('<div class="subheader">The Result is:</div>', unsafe_allow_html=True)
    for chunk in response:
        st.markdown(f'<div class="response">{chunk.text}</div>', unsafe_allow_html=True)
        st.session_state['chat_history'].append(("Bot", chunk.text))

st.markdown('<div class="subheader">History:</div>', unsafe_allow_html=True)

for role, text in st.session_state['chat_history']:
    st.markdown(f'<div class="history"><strong>{role}:</strong> {text}</div>', unsafe_allow_html=True)
