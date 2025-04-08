import streamlit as st
from collections import Counter
import string

st.title("📝 Text Analyzer")

text = st.text_area("Enter your text here:")

if st.button("Analyze"):
    words = text.split()
    word_count = len(words)
    char_count = len(text)
    clean_text = text.translate(str.maketrans("", "", string.punctuation))
    most_common = Counter(clean_text.lower().split()).most_common(1)

    st.write(f"**Word Count:** {word_count}")
    st.write(f"**Character Count:** {char_count}")
    if most_common:
        st.write(f"**Most Common Word:** '{most_common[0][0]}' (appeared {most_common[0][1]} times)") 