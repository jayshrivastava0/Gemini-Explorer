import vertexai
import streamlit as st
from vertexai.preview.language_models import ChatModel
from langchain_google_genai import GoogleGenerativeAI
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from a .env file if it exists
load_dotenv()

# Set the environment variable for the Google service account JSON key
json_key_path = "gemini-explorer-426001-b6fb214bf408.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = json_key_path

# Initialize Vertex AI with the project and location
project = "gemini-explorer"
vertexai.init(project=project, location="us-central1")

# Load model
model = genai.GenerativeModel('gemini-1.0-pro')
chat = model.start_chat()

# Auxiliary function to display and send messages to Streamlit
def llm_function(chat, query):
    response = chat.send_message(query)
    output = response.text

    with st.chat_message("model"):
        st.markdown(output)

    st.session_state.messages.append({"role": "user", "content": query})
    st.session_state.messages.append({"role": "model", "content": output})

# Initialize chat history
st.title("Gemini Explorer")
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display and load chat history
for index, message in enumerate(st.session_state.messages):
    if index != 0:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# For initializing message startup
if len(st.session_state.messages) == 0:
    initial_prompt = "Introduce yourself as ReX, an assistant powered by Google Gemini. You use emojis to be interactive"
    llm_function(chat, initial_prompt)

query = st.chat_input("Gemini Explorer")

if query:
    with st.chat_message("user"):
        st.markdown(query)
    llm_function(chat, query)
