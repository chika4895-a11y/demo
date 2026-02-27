from google import genai
import streamlit as st
 
client = genai.Client(api_key="AIzaSyBcFX9BMiimytaC3cpzIOsgMbaLr1zbmh4")
 
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain MERN in simple terms"
)
 

 
st.write(response.text)