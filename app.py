import google.generativeai as genai
import streamlit as st

genai.configure(api_key="AIzaSyCwT6bAjVZ-6TWih4xBFBnX28uiyNlHXlE")

#setting up the headers
st.title("💬 An AI Code Reviewer")

#taking user input
user_prompt = st.text_area("Enter your Python code hear...")

#if the button is clicked, generate responses
if st.button("Generate") == True:
    model1 = genai.GenerativeModel(model_name='models/gemini-1.5-pro-latest',
                              system_instruction="""You are a friendly AI assistant.
                                                     identify bug error. without out solution.
                                                   """)
    model2 = genai.GenerativeModel(model_name='models/gemini-1.5-pro-latest',
                              system_instruction="""Provide the fixed code snippets.  
                                                    remind the user that you are a python code review assistant.
                                                   """)
    
    #if the prompt is provided
    st.subheader("Code Review")
    #st.markdown("<h3 style='font-size:20px;'>Bug Report</h3>", unsafe_allow_html=True)
    
    if user_prompt:
        st.markdown("<h3 style='font-size:20px;'>Bug Report</h3>", unsafe_allow_html=True)

        response1= model1.generate_content(user_prompt)
        st.write(response1.text)
        st.markdown("<h3 style='font-size:20px;'>Fixed Code</h3>", unsafe_allow_html=True)
        response2= model2.generate_content(user_prompt)
        st.write(response2.text)