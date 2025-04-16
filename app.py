import streamlit as st
from comment_engine import generate_comment

st.set_page_config(page_title="Instagram Comment Generator", page_icon="💬")

st.title("💬 Instagram Comment Generator")
st.write("Type a post description or caption and get a fun comment!")

user_input = st.text_area("Enter Instagram post/caption:")

if st.button("Generate Comment"):
    if user_input.strip():
        comment = generate_comment(user_input)
        st.success(comment)
    else:
        st.warning("Please enter some text to generate a comment.")
