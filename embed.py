import os
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

load_dotenv()

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2",
    token=os.getenv("HF_TOKEN")
)


def parse_tools(file_path) -> list[str]:
    """Parses the tools from the given file path. Each tool is separated by an empty line."""
    tools = []
    current = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            if line == "" and current:
                tools.append("\n".join(current))
                current = []
            else:
                current.append(line)

        if current:
            tools.append("\n".join(current))

    return tools


def to_embedding_text(tool: str) -> str:
    """Structures the tool information for embedding."""
    return f"""
TYPE: TOOL
{tool}
""".strip()


tools: list[str] = parse_tools("data/tools.txt")

texts: list[str] = [to_embedding_text(tool) for tool in tools]

embeddings = model.encode(texts, convert_to_numpy=True)