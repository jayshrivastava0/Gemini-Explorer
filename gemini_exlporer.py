import vertexai
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, Part, Content, ChatSession
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAI
from IPython.display import display
from IPython.core.display import HTML
from dotenv import load_dotenv
import os


load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")
llm = GoogleGenerativeAI(model='gemini-1.0-pro')
llm.invoke("Explain AI")

project = "gemini-explorer"
vertexai.init(project=project)

config = generative_models.GenerationConfig(
    temperature = 0.4
)

# load model
model = genai.GenerativeModel('gemini-1.0-pro')
chat = model.start_chat(history=[])

# auxilalry function to display and send messages to streamlit
def llm_function(chat: ChatSession, query):
    # Extract text from content parts
    query = content.parts[0].text  # Assuming only one text part
    response = chat.send_message(query)
    output = response.candidates[0].content.parts[0].text

    with st.chat_message("model"):
        st.markdown(output)

    st.session_state.messages.append({"role": "user", "content": query})
    st.session_state.messages.append({"role": "user", "content": output})


# initialize chat history
with st.title("Gemini Explorer"):
    if "messages" not in st.session_state:
        st.session_state.messages = []


# display and load chat history
for index, message in enumerate(st.session_state.messages):
    content = Content(
        role = message["role"],
        parts = [Part.from_text(message["content"])]
    )
    if index != 0:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    chat.history.append(content)


# for initailize message startup
if len(st.session_state.messages) == 0:
    initial_prompt = "Introduce yourself as ReX, an assistant powered by Google Gemini. You use emojis to be interactive"
    # Extract text from parts
    query = initial_prompt  # Assuming only one text part
    content = Content(role="user", parts=[Part.from_text(query)])
    llm_function(chat, query)
    chat.history.append(content)


query = st.chat_input("Gemini Explorer")

if query:
    with st.chat_message("user"):
        st.markdown(query)
    llm_function(chat, query)
