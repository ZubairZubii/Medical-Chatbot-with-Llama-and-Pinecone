from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain_community.vectorstores import Pinecone as LangchainPinecone
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from src.prompt import *
import os
from pinecone import Pinecone as PineconeClient, ServerlessSpec

app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')

# Download the HuggingFace embeddings model
embeddings = download_hugging_face_embeddings()

# Initialize the Pinecone client with the new class
pc = PineconeClient(
    api_key=PINECONE_API_KEY,
    environment=PINECONE_API_ENV
)

index_name = "medical-bot"

# Create the index if it doesn't exist (set the dimension directly to 384)
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=384,  # Set dimension to 384 for the 'all-MiniLM-L6-v2' model
        metric='euclidean',
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1'  # Change as necessary
        )
    )

# Load the existing index
docsearch = LangchainPinecone.from_existing_index(index_name, embeddings)

PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

chain_type_kwargs = {"prompt": PROMPT}

llm = CTransformers(model="model/llama-2-7b-chat.ggmlv3.q4_0.bin",
                    model_type="llama",
                    config={'max_new_tokens': 512,
                            'temperature': 0.8})

qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=docsearch.as_retriever(search_kwargs={'k': 2}),
    return_source_documents=True,
    chain_type_kwargs=chain_type_kwargs
)

# List of common greetings or starter messages
starter_messages = ["hello", "hi", "hey", "greetings", "good morning", "good evening", "good afternoon"]

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"].strip().lower()  # Normalize the input message
    input = msg
    print(input)
    
    # Check if the input is a common greeting
    if input in starter_messages:
        # Respond with an introduction message for the chatbot
        return "I am the medical chatbot. You can ask me about medical-related information, conditions, and treatments."

    # If it's not a greeting, proceed with the QA system
    result = qa({"query": input})
    print("Response : ", result["result"])
    return str(result["result"])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
