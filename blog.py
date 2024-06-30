import streamlit as st

# Set the title of the Streamlit app
st.title("My Blog")

# Instructions for the user
st.write("Copy and paste your blog post text below:")

# Text input area for the user to paste the blog content
blog_text = st.text_area("Blog Content", height=300)

# Display the blog content
if blog_text:
    st.write("### Blog Post")
    st.markdown(blog_text)
