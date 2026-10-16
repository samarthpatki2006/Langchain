from fastapi import FastAPI
from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import uvicorn
import os

load_dotenv()
app = FastAPI(title="Langchain Server", version="1.0", description="A simple API server")

llm1 = ChatGroq(
  model="openai/gpt-oss-20b",
  max_tokens=512,
  temperature=0.1
)
llm2 = ChatGroq(
  model="openai/gpt-oss-safeguard-20b",
  max_tokens=512,
  temperature=0.1
)

class RequestBody(BaseModel):
  text: str

@app.post(path="/openai-model-20b")
def openai_model_20b(request: RequestBody):
  prompt = ChatPromptTemplate.from_template("Write a paragraph on the topic: {text}")
  output_parser = StrOutputParser()
  chain = prompt | llm1 | output_parser
  res = chain.invoke({"text": request.text})
  return {"result": res}

@app.post(path="/openai-model-120b")
def openai_model_safeguard_120b(request: RequestBody):
  prompt = ChatPromptTemplate.from_template("Write a paragraph on the topic: {text}")
  output_parser = StrOutputParser()
  chain = prompt | llm2 | output_parser
  res = chain.invoke({"text": request.text})
  return {"result": res}

if __name__ == "__main__":
  uvicorn.run(app, host="localhost", port=8000)