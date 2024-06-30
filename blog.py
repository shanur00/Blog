import streamlit as st

# Set the title of the Streamlit app
st.title("Spring Boot")

st.markdown("# Implementing PUT")

# Read the blog content from the text file
try:
    with open("blog_content.txt", "r") as file:
        blog_text = file.read()
except FileNotFoundError:
    blog_text = "No blog content found. Please make sure `blog_content.txt` exists."

# Display the blog content
if blog_text:
    st.write("### Blog Post")
    st.markdown(blog_text)
