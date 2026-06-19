import os
import faiss
import sentence_transformers
from dotenv import load_dotenv
from parse import parse_tools, to_embedding_text


load_dotenv()
model = sentence_transformers.SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2",
    token=os.getenv("HF_TOKEN"))

# Load the FAISS index and tools
index = faiss.read_index("data/tools.faiss")
tools = parse_tools("data/tools.txt")
texts = [to_embedding_text(tool) for tool in tools]

while True:
    query = input("\n\nEnter your query (or 'exit' to quit): ")
    if query.lower() == 'exit':
        break

    query_embedding = model.encode(
        [query], 
        convert_to_numpy=True, 
        show_progress_bar=True)
    
    distances, indices = index.search(query_embedding, k=5)
    
    print("\n\nQuery:", query)
    # print("Distances:\n", distances)
    # print("Indices:\n", indices)
    
    results = [texts[i] for i in indices[0]]

    for result in results:
        print(result)
        print("=" * 80)