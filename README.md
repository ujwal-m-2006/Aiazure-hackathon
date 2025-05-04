Resume Analyzer & Job Matcher

 Project Description

**Resume Analyzer & Job Matcher** is an AI-powered web application that allows users to upload their resumes and get personalized job recommendations. The system uses Natural Language Processing (NLP) to analyze resume content and matches it with relevant job descriptions from a database or API. The platform helps job seekers identify the best opportunities based on their skills and experience.

 Azure Services Used

- **Azure OpenAI Service**: Used to perform semantic analysis on resumes and job descriptions using GPT-based models. It extracts key skills, experience, and recommends matching roles with reasoning.
- **Azure Blob Storage**: Used to securely store uploaded resumes (PDF or DOCX format) and job description data.

 Setup Instructions

 Prerequisites

- Node.js (v18+ recommended) or Python (if backend is Flask/Django)
- Azure subscription with access to OpenAI and Blob Storage
- Git & basic terminal access

 Clone Repository

```bash
git clone https://github.com/your-org/resume-analyzer-job-matcher
cd resume-analyzer-job-matcher

Frontend Setup
cd frontend
npm install
npm start

Backend Setup
cd backend
npm install

Environment Variables
Create a .env file in the backend folder and add the following
AZURE_OPENAI_KEY=your_openai_api_key
AZURE_OPENAI_ENDPOINT=https://your-openai-resource.openai.azure.com/
AZURE_BLOB_CONNECTION_STRING=your_blob_storage_connection_string
PORT=5000

Run the Backend
npm start

Key Features
Upload and parse resumes

Analyze resumes using Azure OpenAI

Match against curated job listings

Display top matches with confidence scores

Secure storage of documents using Azure Blob

Screenshots
Feature	Screenshot
Upload Resume	
Match Results	
Job Description View

Project Structure
resume-analyzer-job-matcher/
├── frontend/               # React frontend
├── backend/                # Node.js backend with Azure SDKs
├── screenshots/            # Screenshots for documentation
├── README.md
└── .env.example

 Security & Privacy
All files stored securely on Azure Blob with restricted access

No third-party sharing of resume or job data

Compliant with basic data protection principles

 Future Scope
Integration with LinkedIn Jobs or Indeed API

AI interview feedback from resumes

Multilingual resume support
