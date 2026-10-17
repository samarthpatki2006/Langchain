import streamlit as st
import requests

if "output_text" not in st.session_state:
  st.session_state.output_text = ""

models={
  "openai/gpt-oss-20b":"OpenAi GPT OSS 20b",
  "openai/gpt-oss-safeguard-20b":"OpenAi GPT OSS Safeguard 120b",
  "qwen/qwen3.8-27b":"Qwen 3.8"
}

def get_response_model1(text):
  payload = {"text": text}
  response = requests.post("http://localhost:8000/openai-model-20b", json=payload)
  return response.json()

def get_response_model2(text):
  payload = {"text": text}
  response = requests.post("http://localhost:8000/openai-model-120b", json=payload)
  return response.json()

def get_response_model3(text):
  payload = {"text": text}
  response = requests.post("http://localhost:8000/qwen-model-27b", json=payload)
  return response.json()

def handle_click():
  if input_text and selected_model:
    with st.spinner("Generating response..."):
      try:
        if selected_model=="openai/gpt-oss-20b":
          result = get_response_model1(input_text)
          st.session_state.output_text = result.get("result", result)
        elif selected_model=="openai/gpt-oss-safeguard-20b":
          result = get_response_model2(input_text)
          st.session_state.output_text = result.get("result", result)
        else:
          result = get_response_model3(input_text)
          st.session_state.output_text = result.get("result", result)
      except Exception as e:
        st.session_state.output_text = f"Error connecting to backend: {e}"

st.title("Multi Model LLM Usage")
input_text = st.text_input("Enter your topic for an essay:")
selected_model=st.selectbox(
  "Choose an Model:",
  options=list(models.keys()),
  format_func=lambda key: models[key]
)
st.button("Get Response",on_click=handle_click)
container=st.empty()

if st.session_state.output_text:
  if "Error connecting" in str(st.session_state.output_text):
    container.error(st.session_state.output_text)
  else:
    container.write(st.session_state.output_text)