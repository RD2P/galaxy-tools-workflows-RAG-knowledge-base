import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import faiss

from parse import parse_tools, to_embedding_text

load_dotenv()

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2",
    token=os.getenv("HF_TOKEN")
)

# create embeddings
tools: list[str] = parse_tools("data/tools.txt")
texts: list[str] = [to_embedding_text(tool) for tool in tools]
embeddings = model.encode(texts, convert_to_numpy=True)

# create index and save to file
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)
faiss.write_index(index, "data/tools.faiss")