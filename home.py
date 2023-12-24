import streamlit as st
import spacy

try:
    spacy.cli.download("en_core_web_lg")
    nlp = spacy.load("en_core_web_lg")
except OSError:
    spacy.cli.download("en_core_web_lg")


st.write('Hello World!!!')
st.write('update here')

option = st.selectbox(
    'Please select component type',
    ('ner', 'pos', 'dep', 'lemma'))

st.write('You selected:', option)

import streamlit as st

col1, col2 = st.columns(2)

with col1:
   txt_input = st.text_area(label='text_input')

with col2:
   json_data = st.json({"succeeded": True, "data": "cannot"})

