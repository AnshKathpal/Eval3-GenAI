import os
import openai
import sys
from flask import Flask, request,jsonify
from dotenv import load_dotenv,find_dotenv

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI

sys.path.append("../..")

_ = load_dotenv(find_dotenv())
openai.api_key = os.environ[
    "OPENAI_API_KEY"
]


app = Flask(__name__)

loader = PyPDFLoader("./docs/story.pdf")
pages = loader.load()


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap = 200
)

splits = text_splitter.split_documents(pages)
print(splits)

embiddings = OpenAIEmbeddings()

vectordb = Chroma.from_documents(
    documents=splits,
    embedding=embiddings
)

llm = ChatOpenAI(model_name = "gpt-3.5-turbo", temperature=1)

if __name__ == "__main__":
    app.run(debug=True)

