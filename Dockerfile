# Use a lightweight Python base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

COPY app/requirements.txt .
RUN pip config set global.timeout 200
RUN pip install --no-cache-dir -r requirements.txt


# Copy the rest of the application code
COPY app/ ./app

# Download necessary NLTK data (only if your code uses NLTK)
RUN python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"

# Run your app (adjust based on whether it's Streamlit, Flask, etc.)
CMD ["streamlit", "run", "app/ui.py"]

