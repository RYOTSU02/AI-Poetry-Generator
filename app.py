import streamlit as st
from transformers import pipeline

# Load the text generation model
poetry_generator = pipeline("text-generation", model="gpt-2")

# Streamlit UI
st.title("✨ AI-Powered Poetry Writer ✨")
st.write("Generate a personalized poem based on your mood and theme!")

# User inputs
mood = st.text_input("Enter the mood (e.g., joyful, melancholic, nostalgic):")
theme = st.text_input("Enter the theme (e.g., love, adventure, nature):")

# Generate poem
if st.button("Generate Poem"):
    prompt = f"A {mood} poem about {theme}..."
    poem = poetry_generator(prompt, max_length=100, do_sample=True)[0]['generated_text']
    st.subheader("Here is your AI-generated poem:")
    st.write(poem)
