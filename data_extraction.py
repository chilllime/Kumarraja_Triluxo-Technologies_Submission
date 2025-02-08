from langchain.document_loaders import WebBaseLoader

# URL to extract data from
url = "https://brainlox.com/courses/category/technical"

# Load the data from the URL
loader = WebBaseLoader(url)
data = loader.load()

# Print the extracted data
print(data)