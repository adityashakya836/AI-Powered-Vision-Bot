import json
import streamlit as st
import google.generativeai as genai
genai.configure(api_key = 'you_google_api_key')

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history = [])

def get_gemini_reponse(question):
    response = chat.send_message(question, stream = True)
    return response

st.set_page_config(page_title = 'Q&A Demo')
st.header("Gemini LLM Application")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input = st.text_input('Input:', key = 'input')
submit = st.button('Ask the question')

if submit and input:
    response = get_gemini_reponse(input)

    # Add user query and response to session chat history
    st.session_state['chat_history'].append(("You", input))
    st.subheader('The Response is')
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

st.subheader("The Chat History is")
for role, text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")
