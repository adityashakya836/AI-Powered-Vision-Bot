from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
import time

genai.configure(api_key = 'you_google_api_key')

## function to load Gemini Pro model and get reponses
model = genai.GenerativeModel('gemini-pro')
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title = 'Q&A Demo')
st.header("Gemini Application")

input = st.text_input("Input: ", key = 'input')
submit = st.button("Ask the question")

if submit:
    response = get_gemini_response(input)
    st.write(response)
