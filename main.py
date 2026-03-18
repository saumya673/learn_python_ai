import os

from fastapi import FastAPI
from langchain_openai import ChatOpenAI
import uvicorn
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/agent")
def call_agent(msg: str):
    try:
        model = ChatOpenAI(model="gpt-5", api_key=openai_api_key)
        response = model.invoke(msg)
        return response.content
    except Exception as err:
        return f"{err}"   


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)