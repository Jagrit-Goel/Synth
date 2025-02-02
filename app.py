from flask import Flask, request, jsonify
from src.agent import process_document, interact_with_user

app = Flask(__name__)
# Handle the root URL
@app.route('/')
def home():
    return "Welcome to the Synth app!"

# Handle the favicon request to prevent 404 errors
@app.route('/favicon.ico')
def favicon():
    return '', 204  # Return empty response to avoid 404 for favicon
@app.route('/upload', methods=['POST'])
def upload_document():
    file = request.files['file']
    file_path = f"uploads/{file.filename}"
    file.save(file_path)

    response = process_document(file_path)
    return jsonify({"message": response})

@app.route('/ask', methods=['POST'])
def ask_question():
    audio_response = interact_with_user()
    return jsonify({"audio_url": audio_response})

if __name__ == "__main__":
    app.run(debug=True)

