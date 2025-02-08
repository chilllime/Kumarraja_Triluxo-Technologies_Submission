# Kumarraja_Triluxo-Technologies_Submission
AI Task 

# Custom Chatbot using Langchain and Flask

This project creates a custom chatbot using Langchain and Flask. It extracts data from a given URL, creates embeddings, and stores them in a vector store. A Flask RESTful API is then used to handle the conversation.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/chilllime/Kumarraja_Triluxo-Technologies_Submission.git
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the Flask server:
   ```bash
   python app.py
4. Send a POST request to /chat with a JSON payload containing the user's message:
   ```bash
   {
    "message": "Your question here"
   }
   
   
