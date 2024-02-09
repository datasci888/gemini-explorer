import vertexai
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, Part, Content, ChatSession

import vertexai

project = "gemini-explorer-412518"
vertexai.init(project=project)

# Now reload vertexai
import importlib
importlib.reload(vertexai)

config = generative_models.GenerationConfig(
temperature=0.4
)

model = GenerativeModel(
"gemini-pro",
generation_config=config
)

chat = model.start_chat()

def llm_function(chat: ChatSession, query):
    print("print(query), ", query)
    response = chat.send_message(query)
    output = response.candidates[0].content.parts[0].text

    with st.chat_message("model"):
        st.markdown(output)

    st.session_state.messages.append({
    "role": "user",
    "content": query
    })
    st.session_state.messages.append({
    "role": "model",
    "content": output
    })

st.title("Gemini Explorer")


if "messages" not in st.session_state:
    st.session_state.messages = []

for index, message in enumerate(st.session_state.messages):
    content = Content(
    role = message["role"],
    parts=[Part.from_text(message["content"])]
    )

    chat.history.append(content)

if len(st.session_state.messages) == 0:
    user_name = st.text_input("Please enter your name")
    initial_prompt = f"Hey I'm Rex! I'm glad to meet you, {user_name}. Let's have some fun conversations using emojis! "
    llm_function(chat, initial_prompt)

query = st.chat_input("What can I do for you dear?")
if query:
    with st.chat_message("user"):
        st.markdown(query)
    llm_function(chat, query)


