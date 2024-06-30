import streamlit as st

# Set the title of the Streamlit app
st.title("My Blog")

# Instructions for the user
st.write("The blog content is read from the `blog_content.txt` file.")

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
