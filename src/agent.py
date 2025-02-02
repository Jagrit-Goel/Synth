from src.document_processing import extract_text_from_pdf, extract_text_from_docx
from src.embeddings import get_embeddings
from src.pinecone_integration import store_embeddings_in_pinecone, query_pinecone
from src.voice_interaction import recognize_speech, synthesize_speech

def process_document(file_path):
    if file_path.endswith('.pdf'):
        text = extract_text_from_pdf(file_path)
    elif file_path.endswith('.docx'):
        text = extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file type")

    embedding = get_embeddings(text)
    store_embeddings_in_pinecone(file_path, embedding)
    return "Document processed and stored."

def interact_with_user():
    question = recognize_speech()
    if question:
        embedding = get_embeddings(question)
        answer = query_pinecone(embedding)
        audio_response = synthesize_speech(answer)
        return audio_response
    else:
        return "Sorry, I couldn't understand your question."
