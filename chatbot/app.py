from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv()
prompt=ChatPromptTemplate.from_messages(
  [
    ("system","You are a helpful assistant. Please respond to the user queries"),
    ("user","Question: {question}")
  ]
)
st.title("Langchain Demo With Groq Api")
input_text=st.text_input("Enter your prompt")
llm = ChatGroq(
  model="openai/gpt-oss-20b",
  temperature=0.1,
  max_tokens=1024,
) 
output_parser=StrOutputParser()
chain=prompt | llm | output_parser
if input_text:
  st.write(chain.invoke({'question':input_text}))