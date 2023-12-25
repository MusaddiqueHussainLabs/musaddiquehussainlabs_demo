import streamlit as st
from musaddiquehussainlabs.nlp_components import nlp

st.subheader('NLP Tasks', divider='rainbow')
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



