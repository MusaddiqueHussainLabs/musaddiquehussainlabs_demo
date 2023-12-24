import streamlit as st
from musaddiquehussainlabs.nlp_components import nlp
import spacy

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    spacy.cli.download("en_core_web_sm")

st.write('The `nlp_components` module comprises essential tools for text analysis: tokenization for breaking text into units, part-of-speech tagging for grammatical labeling, and named entity recognition to identify entities like names or locations. These functions collectively enable in-depth linguistic analysis, facilitating tasks such as syntax parsing, entity categorization, and text structure comprehension within natural language processing workflows.')

option = st.selectbox(
    'Please select component type',
    ('tokenize','pos', 'lemma', 'morphology','dep', 'ner', 'norm'))

col1, col2 = st.columns(2)

with col1:
    data_to_process  = st.text_area(label='input_text')
    button_clicked = st.button("Submit")

if button_clicked:
    result = nlp.predict(component_type=option, input_text=data_to_process)

    with col2:
        json_data = st.json(result)



