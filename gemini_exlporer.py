import vertexai
import streamlit as st
import vertexai.preview import generative_models
import vertexai.preview.generative_models import GenerativeModel, Part, Content, ChatSession

project = "gemini-explorer"
vertexai.init(project=project)

config = generative_models.GenerationConfig(
    temperature = 0.4
)

# load model
model = GenerativeModel(
    "gemini-pro", 
    generation_config = config
)

chat = model.start_chat()

# auxilalry function to display and send messages to streamlit
def llm_function(chat: ChatSession, query):
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
        parts = [Part(text = message["content"])]
    )
    if index != 0:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    chat.history.append(content)


# for initailize message startup
if len(st.session_state.messages) == 0:
    pass

query = st.chat_input("Gemini Explorer")

if query:
    with st.chat_message("user"):
        st.markdown(query)
    llm_function(chat, query)
