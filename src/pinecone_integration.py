import json
import numpy as np
from pinecone import Pinecone, ServerlessSpec

# Load Pinecone API Key
with open('config/api_keys.json') as f:
    keys = json.load(f)

# Initialize Pinecone instance with the API key
pc = Pinecone(api_key=keys['pinecone_api_key'])

# Create and connect to Pinecone index
index_name = "document-index"

# Check if the index exists; if not, create it
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name, 
        dimension=1536, 
        metric='euclidean',
        spec=ServerlessSpec(
    cloud='aws',
    region='us-east-1'  # Change to a supported region
)
    )

# Connect to the index
index = pc.Index(index_name)

def store_embeddings_in_pinecone(doc_id, embedding):
    index.upsert([(doc_id, embedding)])

def query_pinecone(question_embedding):
    result = index.query([question_embedding], top_k=1, include_metadata=True)
    return result['matches'][0]['metadata']['text']
