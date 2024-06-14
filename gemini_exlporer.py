import vertexai
import streamlit as st
from vertexai.preview.language_models import ChatModel
from langchain_google_genai import GoogleGenerativeAI
import google.generativeai as genai
import os

# Set the environment variable for the Google API key
os.environ["GOOGLE_API_KEY"] = st.secrets["GOOGLE_API_KEY"]

# Write the Google credentials to a temporary file and set the environment variable
google_credentials_path = "google_credentials.json"  # Changed to current working directory
with open(google_credentials_path, 'w') as f:
    f.write(f'''
    {{
        "type": "{st.secrets['google_credentials']['type']}",
        "project_id": "{st.secrets['google_credentials']['project_id']}",
        "private_key_id": "{st.secrets['google_credentials']['private_key_id']}",
        "private_key": "{st.secrets['google_credentials']['private_key']}",
        "client_email": "{st.secrets['google_credentials']['client_email']}",
        "client_id": "{st.secrets['google_credentials']['client_id']}",
        "auth_uri": "{st.secrets['google_credentials']['auth_uri']}",
        "token_uri": "{st.secrets['google_credentials']['token_uri']}",
        "auth_provider_x509_cert_url": "{st.secrets['google_credentials']['auth_provider_x509_cert_url']}",
        "client_x509_cert_url": "{st.secrets['google_credentials']['client_x509_cert_url']}",
        "universe_domain": "{st.secrets['google_credentials']['universe_domain']}"
    }}
    ''')

# Set the environment variable to point to the temporary credentials file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = google_credentials_path

# Initialize Vertex AI with the project and location
project = st.secrets["google_credentials"]["project_id"]
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
