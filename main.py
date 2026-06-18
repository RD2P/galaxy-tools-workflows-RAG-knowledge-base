import os
import faiss
import sentence_transformers
from dotenv import load_dotenv
from parse import parse_tools, to_embedding_text


load_dotenv()
model = sentence_transformers.SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2",
    token=os.getenv("HF_TOKEN"))

query = "Which tools are used for quality control?"
query_embedding = model.encode(
    [query], 
    convert_to_numpy=True, 
    show_progress_bar=True)
 
index = faiss.read_index("data/tools.faiss")
distances, indices = index.search(query_embedding, k=5)
 
print("Query:", query)
print("distances:\n", distances)
print("indices:\n", indices)
 
tools = parse_tools("data/tools.txt")
texts = [to_embedding_text(tool) for tool in tools]

results = [texts[i] for i in indices[0]]

for result in results:
    print(result)
    print("=" * 80)