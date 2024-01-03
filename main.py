import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import OpenAI
import os


os.environ["OPENAI_API_KEY"] = "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"
llm = OpenAI(temperature=0.5)
template = """
You are a Translator model
Your task is to translate the below text from {input_lang} to {output_lang}
Text: {text}
"""
prompt = PromptTemplate(
    input_variables = ["input_lang", "output_lang", "text"],
    template = template
)

st.header('Translator App')
col1, col2 = st.columns(2)
with col1:
    st.image(image="translator.png",width=200)
with col2:
    st.markdown("This is an App to translate text from one language to another.")
colx, coly = st.columns(2)
with colx:
    input_lang = st.selectbox(
        "Select input language",
        {"English","Spanish","Portugese", "Arabic","German", "Japanese","Russian"}
    )
with coly:
    output_lang = st.selectbox(
        "Select output language",
        {"English","Spanish","Portugese", "Arabic","German", "Japanese","Russian"}
    )
input_text = st.text_area(label="",placeholder="Input your text",key="input_text")
final_prompt = prompt.format(input_lang = input_lang,output_lang = output_lang,text = input_text)
translated_text = llm(final_prompt)
st.write(f"The translated text is : {translated_text}")