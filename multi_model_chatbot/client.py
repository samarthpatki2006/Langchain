import streamlit as st
import requests

models={
  "openai/gpt-oss-20b":"OpenAi GPT OSS 20b",
  "openai/gpt-oss-safeguard-20b":"OpenAi GPT OSS Safeguard 120b"
}

def get_response_model1(text):
  payload = {"text": text}
  response = requests.post("http://localhost:8000/openai-model-20b", json=payload)
  return response.json()

def get_response_model2(text):
  payload = {"text": text}
  response = requests.post("http://localhost:8000/openai-model-120b", json=payload)
  return response.json()

st.title("Multi Model LLM Usage")
input_text = st.text_input("Enter your topic for an essay:")
selected_model=st.selectbox(
  "Choose an Model:",
  options=list(models.keys()),
  format_func=lambda key: models[key]
)
if input_text and selected_model:
  with st.spinner("Generating response..."):
    try:
      if selected_model=="openai/gpt-oss-20b":
        result = get_response_model1(input_text)
        st.write(result.get("result", result))
      else:
        result = get_response_model2(input_text)
        st.write(result.get("result", result))
    except Exception as e:
      st.error(f"Error connecting to backend: {e}")