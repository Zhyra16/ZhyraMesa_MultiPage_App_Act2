import streamlit as st

st.title("🏠 Home")

st.header("Hello, I'm Zhyra!")
st.write("Welcome to my personal multipage portfolio app.")

name = st.text_input("What's your name?")

if name:
    st.success(f"Welcome {name}! Thank you for visiting my portfolio.")
