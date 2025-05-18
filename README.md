Text Summarizer App
This is a lightweight web app built with Python, Streamlit, and NLTK to summarize large text blocks into concise summaries. It uses natural language processing to extract key sentences that best represent the original content.

🔍 Features
Paste or type long texts and receive brief summaries

Uses nltk for tokenization and stopword removal

Clean, interactive interface with Streamlit

Dockerized for seamless deployment

⚙️ Technologies
Python

Streamlit

NLTK

Docker

🚀 Getting Started
Run using Docker:

bash
Copy
Edit
docker build -t summarize-app .
docker run -p 8501:8501 summarize-app
Open your browser at: http://localhost:8501
