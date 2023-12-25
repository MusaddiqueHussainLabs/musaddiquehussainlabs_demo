from pydantic_settings import BaseSettings
import streamlit as st
from musaddiquehussainlabs.document_analysis import DocumentAnalysis

st.secrets["GOOGLE_API_KEY"]

class DocumentAnalysisConstants(BaseSettings):

    full_analysis: str =  'full_analysis'
    language_detection: str = 'language_detection'
    deep_linguistic_analysis: str = 'deep_linguistic_analysis'
    keyphrase_extraction: str =  'keyphrase_extraction'
    entity_recognition: str = 'entity_recognition'
    sentiment_analysis: str = 'sentiment_analysis'
    pii_anonymization: str = 'pii_anonymization'

document_analysis_const =    DocumentAnalysisConstants()
document_analysis = DocumentAnalysis()

st.subheader('Document Analysis', divider='rainbow')

option = st.selectbox(
    'Please select analysis type',
    (document_analysis_const.full_analysis,
     document_analysis_const.language_detection,
     document_analysis_const.deep_linguistic_analysis,
     document_analysis_const.keyphrase_extraction,
     document_analysis_const.entity_recognition,
     document_analysis_const.sentiment_analysis,
     document_analysis_const.pii_anonymization))

col1, col2 = st.columns(2)

with col1:
    data_to_process  = st.text_area(label='input_text')
    button_clicked = st.button("Submit")

if button_clicked:
    if option == document_analysis_const.full_analysis:
        result = document_analysis.full_analysis(data_to_process)
    elif option == document_analysis_const.language_detection:
        result = document_analysis.language_detection(data_to_process)
    elif option == document_analysis_const.deep_linguistic_analysis:
        result = document_analysis.deep_linguistic_analysis(data_to_process)
    elif option == document_analysis_const.keyphrase_extraction:
        result = document_analysis.keyphrase_extraction(data_to_process)
    elif option == document_analysis_const.entity_recognition:
        result = document_analysis.entity_recognition(data_to_process)
    elif option == document_analysis_const.sentiment_analysis:
        result = document_analysis.sentiment_analysis(data_to_process)
    elif option == document_analysis_const.pii_anonymization:
        result = document_analysis.pii_anonymization(data_to_process)
    

    with col2:
        json_data = st.json(result)






