from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import CharacterTextSplitter

# Initialize the OpenAI embeddings
embeddings = OpenAIEmbeddings()

# Split the extracted data into smaller chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
texts = text_splitter.split_documents(data)

# Create embeddings and store them in a vector store
vector_store = FAISS.from_documents(texts, embeddings)

# Save the vector store locally
vector_store.save_local("faiss_index")