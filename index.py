import streamlit as st

from hausa_translator import hausa_dict
from yoruba_translator import Yoruba_Dictionary
from igbo_dictionary import igbo_words
from swahili import swahili_dict
from tiv import tiv_translator


st.title("English To Foreign Language Dictionary")
st.write(
    "Choose a language and enter an English word to get a translation "
    "in Yoruba, Igbo, Hausa, Tiv, or Swahili"
)

# Language Selector
language = st.selectbox(
    "Choose a language",
    ("Hausa", "Yoruba", "Igbo", "Swahili", "Tiv")
)

# Word input
word = st.text_input("Enter an English word").lower().strip()

# Button
if st.button("Translate"):

    if word == "":
        st.warning("Please enter a word.")

    elif language == "Hausa":
        if word in hausa_dict:
            st.success(f"Hausa: {hausa_dict[word]}")
        else:
            st.error(f"'{word}' not found in Hausa dictionary.")

    elif language == "Yoruba":
        if word in Yoruba_Dictionary:
            st.success(f"Yoruba: {Yoruba_Dictionary[word]}")
        else:
            st.error(f"'{word}' not found in Yoruba dictionary.")

    elif language == "Igbo":
        if word in igbo_words:
            st.success(f"Igbo: {igbo_words[word]}")
        else:
            st.error(f"'{word}' not found in Igbo dictionary.")

    elif language == "Swahili":
        if word in swahili_dict:
            st.success(f"Swahili: {swahili_dict[word]}")
        else:
            st.error(f"'{word}' not found in Swahili dictionary.")

    elif language == "Tiv":
        if word in tiv_translator:
            st.success(f"Tiv: {tiv_translator[word]}")
        else:
            st.error(f"'{word}' not found in Tiv dictionary.")
