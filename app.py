from flask import Flask, request, jsonify
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

app = Flask(__name__)

# Load the vector store
embeddings = OpenAIEmbeddings()
vector_store = FAISS.load_local("faiss_index", embeddings)

# Initialize the LLM (using a free LLM API)
llm = OpenAI(api_key="sk-5678efgh5678efgh5678efgh5678efgh5678efgh")

# Create a retrieval-based QA chain
qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vector_store.as_retriever())

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({"error": "No message provided"}), 400
    
    # Get the response from the QA chain
    response = qa_chain.run(user_input)
    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)