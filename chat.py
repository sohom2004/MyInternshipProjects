from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("API_KEY"))
model = genai.GenerativeModel("gemini-pro")

chat = model.start_chat(history=[])

st.set_page_config(page_title="ChatBot")
st.header("Gemini LLM ChatBot")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
input = st.text_input("Input:   ", key="input")
submit = st.button("Submit")

if submit and input:
    response = model.generate_content(input)
    st.session_state['chat_history'].append(("You", input))
    st.subheader("Response: ")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

st.subheader("Chat History: ")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")