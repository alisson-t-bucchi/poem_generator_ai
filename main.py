import cohere
from config import API_KEY
import streamlit as st

co = cohere.Client(API_KEY)

st.title("AI Poem generator")
st.divider()

number_of_lines = st.number_input("Enter number of lines: ")
theme = st.text_input("Enter one theme about your poem: ")

prompt = f"Write a poem with {round(number_of_lines)} lines about {theme}."

try:
    #Generating responses
    response = co.generate(
        model='command-r-08-2024',
        prompt=prompt,
        max_tokens=500,
        temperature=0.7
    )
    # Show result -> run streamlit: streamlit run <file.py>
    st.divider()
    generated_text = response.generations[0].text.strip()
    lines = generated_text.split("\n")

    st.title(f"Your AI poem:")
    st.text(" ")

    for line in lines:
        st.write(line)

except cohere.errors.CohereError as e:
    print(f"Erro na API da Cohere: {e}")



