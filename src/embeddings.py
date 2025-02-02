import openai
import numpy as np
import json

# Load OpenAI API Key
with open('config/api_keys.json') as f:
    keys = json.load(f)
openai.api_key = keys['openai_api_key']

def get_embeddings(text):
    response = openai.Embedding.create(
        model="text-embedding-ada-002",
        input=text
    )
    return np.array(response['data'][0]['embedding'])
