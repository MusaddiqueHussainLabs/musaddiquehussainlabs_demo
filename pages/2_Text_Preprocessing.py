from pydantic_settings import BaseSettings
import streamlit as st
from musaddiquehussainlabs.text_preprocessing import preprocess_text, preprocess_operations

st.subheader('1) Default Text Preprocessing', divider='rainbow')
col1, col2 = st.columns(2)

with col1:
    data_to_process  = st.text_area(label='input_text')
    button_clicked = st.button("Submit")

if button_clicked:
    preprocessed_text = preprocess_text(data_to_process)

    with col2:
        json_data = st.json(preprocessed_text)

st.subheader('2) Custom Text Preprocessing', divider='rainbow')
option = st.multiselect(
    'Please select operation type',
    (preprocess_operations.to_lower,
    preprocess_operations.to_upper,
    preprocess_operations.remove_number,
    preprocess_operations.remove_punctuation,
    preprocess_operations.remove_stopword,
    preprocess_operations.remove_itemized_bullet_and_numbering,
    preprocess_operations.remove_url,
    preprocess_operations.remove_special_character,
    preprocess_operations.keep_alpha_numeric,
    preprocess_operations.remove_whitespace,
    preprocess_operations.normalize_unicode,
    preprocess_operations.remove_freqwords,
    preprocess_operations.remove_rarewords,
    preprocess_operations.remove_email,
    preprocess_operations.remove_phone_number,
    preprocess_operations.remove_ssn,
    preprocess_operations.remove_credit_card_number,
    preprocess_operations.remove_emoji,
    preprocess_operations.remove_emoticons,
    preprocess_operations.convert_emoticons_to_words,
    preprocess_operations.convert_emojis_to_words,
    preprocess_operations.remove_html,
    preprocess_operations.chat_words_conversion,
    preprocess_operations.expand_contraction,
    preprocess_operations.tokenize_word,
    preprocess_operations.tokenize_sentence,
    preprocess_operations.stem_word,
    preprocess_operations.lemmatize_word,
    preprocess_operations.substitute_token))

# st.write('You selected:', option)

cust_col1, cust_col2 = st.columns(2)

with cust_col1:
    cust_data_to_process  = st.text_area(label='cust_input_text')
    cust_button_clicked = st.button("Submit Custom Operation")

if cust_button_clicked:
    preprocess_functions = option
    cust_preprocessed_text = preprocess_text(cust_data_to_process, preprocess_functions)

    with cust_col2:
        json_data = st.json(cust_preprocessed_text)

