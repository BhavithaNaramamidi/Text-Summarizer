import logging
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation

# Configure logging to ensure it works with Streamlit
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

# Get a logger instance
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Add a handler if not already present
if not logger.handlers:
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(handler)

nltk.download('punkt')
logger.info("Downloaded punkt tokenizer")
nltk.download('stopwords')
logger.info("Downloaded stopwords")

def summarize_text(text, max_sentences=3):
    try:
        logger.info(f"Starting text summarization with max_sentences={max_sentences}")
        
        sentences = sent_tokenize(text)
        logger.info(f"Found {len(sentences)} sentences in input text")
        
        words = word_tokenize(text.lower())
        stop_words = set(stopwords.words('english') + list(punctuation))
        
        word_frequencies = {}
        for word in words:
            if word not in stop_words:
                word_frequencies[word] = word_frequencies.get(word, 0) + 1
        
        logger.info(f"Calculated frequencies for {len(word_frequencies)} unique words")
        
        sentence_scores = {}
        for sent in sentences:
            for word in word_tokenize(sent.lower()):
                if word in word_frequencies:
                    sentence_scores[sent] = sentence_scores.get(sent, 0) + word_frequencies[word]
        
        ranked = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
        summary = " ".join(ranked[:max_sentences])
        
        logger.info(f"Generated summary with {len(ranked[:max_sentences])} sentences")
        return summary
        
    except Exception as e:
        logger.error(f"Error during text summarization: {str(e)}")
        raise
