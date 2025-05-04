import os
from flask import Flask, request, render_template
from azure.storage.blob import BlobServiceClient
from werkzeug.utils import secure_filename
import openai

# For DOCX and PDF parsing
import docx
from PyPDF2 import PdfReader

app = Flask(__name__)
UPLOAD_FOLDER = 'resumes'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Azure Config
BLOB_CONNECTION_STRING = os.getenv("AZURE_BLOB_CONNECTION_STRING")
BLOB_CONTAINER_NAME = "resumes"
openai.api_key = os.getenv("AZURE_OPENAI_KEY")
openai.api_base = "https://YOUR_RESOURCE_NAME.openai.azure.com/"
openai.api_type = "azure"
openai.api_version = "2023-05-15"
DEPLOYMENT_NAME = "YOUR_DEPLOYMENT_NAME"

blob_service_client = BlobServiceClient.from_connection_string(BLOB_CONNECTION_STRING)

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'docx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text(filepath, ext):
    if ext == 'pdf':
        reader = PdfReader(filepath)
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    elif ext == 'docx':
        doc = docx.Document(filepath)
        return "\n".join(para.text for para in doc.paragraphs)
    else:
        with open(filepath, "r", encoding='utf-8', errors='ignore') as f:
            return f.read()

@app.route('/', methods=['GET', 'POST'])
def index():
    match_result = ""
    if request.method == 'POST':
        resume_file = request.files.get('resume')
        job_desc = request.form.get('jobdesc', '')

        if resume_file and allowed_file(resume_file.filename):
            filename = secure_filename(resume_file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            resume_file.save(filepath)

            # Upload to Azure Blob
            blob_client = blob_service_client.get_blob_client(container=BLOB_CONTAINER_NAME, blob=filename)
            with open(filepath, "rb") as data:
                blob_client.upload_blob(data, overwrite=True)

            ext = filename.rsplit('.', 1)[1].lower()
            resume_text = extract_text(filepath, ext)

            # Prompt
            prompt = f"""
            You are an expert resume evaluator. Evaluate the following resume against the job description and return:
            - A match score out of 100
            - 2–3 strengths
            - 2–3 suggested improvements

            Resume:
            {resume_text}

            Job Description:
            {job_desc}
            """

            response = openai.ChatCompletion.create(
                engine=DEPLOYMENT_NAME,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=400
            )

            match_result = response['choices'][0]['message']['content']

    return render_template('index.html', match=match_result)

if __name__ == '__main__':
    app.run(debug=True)
