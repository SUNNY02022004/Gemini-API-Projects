from dotenv import load_dotenv
import streamlit as st
import textwrap
import google.generativeai as genai

load_dotenv()




def get_gemini_response(question):

    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(question)
    return response.text

## Initialize our Streamlit app
st.set_page_config(page_title="Suki AI")
st.header("Gemini API Application")

input_text = st.text_input("Input: ", key="input")
submit_button = st.button("Submit")

if submit_button:
    response = get_gemini_response(input_text)
    st.subheader("The Result is:")
    st.write(response)
