# Galaxy Tools and Workflows RAG Knowledge Base

This project implements a Retrieval Augmented Generation (RAG) system to create a searchable knowledge base of Galaxy tools and workflows.

## Project Overview

The goal is to build a system that can answer natural language queries about Galaxy tools and workflows. This is achieved by:
1.  Creating a database of all available Galaxy tools and workflows.
2.  Processing this data into a structured text format.
3.  Generating vector embeddings for each tool and workflow document.
4.  Storing these embeddings in a searchable vector index.
5.  Using a Large Language Model (LLM) to generate answers based on the retrieved information.

## Data Processing

### Data Extraction and Formatting
Tool and workflow information is extracted and converted into a standardized text format.

#### Tool Example
```text
NAME: NCBI Accession Download
DESCRIPTION: Download sequences from GenBank/RefSeq by accession through the NCBI ENTREZ API
IS_WORKFLOW_COMPATIBLE: true
PANEL_SECTION_NAME: Get Data
```

#### Workflow Example
```text
TYPE: Workflow
TITLE: post-curation-processing
DESCRIPTION: Post-curation processing workflow for VGP assemblies...
WORKFLOW_CLASS: Galaxy
TOOLS USED:
- cutadapt
- mashmap
- gfastats
- JBrowse2
- imagemagick_image_montage
```

### Document Chunking

Each tool or workflow is treated as a single, distinct document.

## RAG Pipeline

1. Embedding Generation: Each document is passed through an embedding model from Hugging Face's sentence-transformers library to create a vector representation.
    - **Model**: sentence-transformers/all-MiniLM-L6-v2

2. Vector Storage: The generated embeddings and their corresponding metadata are stored in a FAISS index for efficient similarity searching.

3. Retrieval and Generation:

    - When a user submits a prompt, the system searches the vector database to find the most relevant documents.
    - The retrieved documents are then passed as context to a locally running LLM (via Ollama) to generate a final answer.

## Future Work
Two-Step Retrieval: Implement a more advanced retrieval process where a cross-encoder reranks the top-k results from the initial bi-encoder search to improve relevance.