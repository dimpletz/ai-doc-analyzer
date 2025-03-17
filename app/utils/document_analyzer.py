"""
Document Analyzer Module

This module provides functionality for analyzing documents using AI models.
It handles text extraction from various file formats and performs advanced
NLP tasks such as named entity recognition, keyword extraction, and text summarization.

The module uses:
- pdfplumber for PDF text extraction
- python-docx for Word document processing
- Hugging Face Transformers for AI-powered analysis

Author: Ofelia Webb <ofelia.b.webb@gmail.com>
"""

import os
import pdfplumber
import docx
from ..models.model_manager import ModelManager

# Initialize model manager as a singleton for efficient model loading
model_manager = ModelManager()

def extract_text(file_path):
    """
    Extract text content from various document formats.
    
    Supports the following file formats:
    - PDF (.pdf): Uses pdfplumber for text extraction
    - Word (.docx): Uses python-docx for document parsing
    - Text (.txt): Direct file reading with UTF-8 encoding
    
    Args:
        file_path (str): Path to the document file
        
    Returns:
        str: Extracted text content from the document
        
    Raises:
        ValueError: If the file format is not supported
    """
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.pdf':
        with pdfplumber.open(file_path) as pdf:
            return "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    elif ext == '.docx':
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    elif ext == '.txt':
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        raise ValueError("Unsupported file format")

def analyze_text(text):
    """
    Perform named entity recognition and keyword extraction on the text.
    
    Uses AI models to:
    1. Identify named entities (people, organizations, locations)
    2. Extract important keywords and concepts
    
    Args:
        text (str): Input text to analyze
        
    Returns:
        tuple: (entities, keywords)
            - entities (dict): Dictionary of named entities and their types
            - keywords (list): List of important keywords from the text
    """
    entities = model_manager.get_entities(text)
    keywords = model_manager.get_keywords(text)
    return entities, keywords

def summarize_text(text, max_length=150):
    """
    Generate a concise summary of the input text using AI.
    
    Uses a pre-trained summarization model to create a shorter version
    of the input text while preserving the main ideas and key information.
    
    Args:
        text (str): Input text to summarize
        max_length (int, optional): Maximum length of the summary in tokens.
            Defaults to 150.
            
    Returns:
        str: Generated summary of the input text
    """
    return model_manager.get_summary(text, max_length=max_length)

def main(file_path):
    """
    Standalone function for testing the document analyzer.
    
    Args:
        file_path (str): Path to the document to analyze
    """
    text = extract_text(file_path)
    entities, keywords = analyze_text(text)
    summary = summarize_text(text[:1000])  # Limit input for summarization
    
    print("\n--- Extracted Summary ---\n", summary)
    print("\n--- Named Entities ---\n", entities)
    print("\n--- Keywords ---\n", keywords[:20])  # Display top 20 keywords

if __name__ == "__main__":
    file_path = input("Enter file path: ")
    main(file_path)
