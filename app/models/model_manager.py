"""
Model Manager Module

This module manages the loading and usage of AI models for document analysis.
It provides a centralized way to handle different models while ensuring efficient
resource usage through lazy loading.

Features:
- Lazy loading of models to optimize memory usage
- Centralized model management
- Consistent API for different AI tasks
- Singleton pattern for efficient model sharing

Author: Ofelia Webb <ofelia.b.webb@gmail.com>

Models used:
- Named Entity Recognition (NER): BERT-based model
- Keyword Extraction: BERT-based token classification
- Text Summarization: DistilBART CNN model
"""

from transformers import pipeline

class ModelManager:
    """
    Manages AI models for document analysis tasks.
    
    This class implements the singleton pattern and lazy loading for AI models.
    Models are only loaded when first needed, helping to minimize memory usage
    and startup time.
    
    Attributes:
        _ner (Pipeline): Named Entity Recognition model
        _keyword_extractor (Pipeline): Keyword extraction model
        _summarizer (Pipeline): Text summarization model
    """
    
    def __init__(self):
        """Initialize the model manager with empty model placeholders."""
        self._ner = None
        self._keyword_extractor = None
        self._summarizer = None

    @property
    def ner(self):
        """
        Get the Named Entity Recognition model.
        
        Loads the model on first access using lazy loading pattern.
        
        Returns:
            Pipeline: Hugging Face pipeline for NER
        """
        if self._ner is None:
            self._ner = pipeline("ner")
        return self._ner

    @property
    def keyword_extractor(self):
        """
        Get the keyword extraction model.
        
        Loads the model on first access using lazy loading pattern.
        Uses a specialized BERT model fine-tuned for keyword extraction.
        
        Returns:
            Pipeline: Hugging Face pipeline for token classification
        """
        if self._keyword_extractor is None:
            self._keyword_extractor = pipeline("token-classification", 
                                             model="yanekyuk/bert-uncased-keyword-extractor")
        return self._keyword_extractor

    @property
    def summarizer(self):
        """
        Get the text summarization model.
        
        Loads the model on first access using lazy loading pattern.
        Uses a DistilBART model fine-tuned on CNN articles.
        
        Returns:
            Pipeline: Hugging Face pipeline for summarization
        """
        if self._summarizer is None:
            self._summarizer = pipeline("summarization")
        return self._summarizer

    def get_entities(self, text):
        """
        Extract named entities from text.
        
        Args:
            text (str): Input text to analyze
            
        Returns:
            dict: Dictionary mapping entity text to entity type
        """
        entities = self.ner(text)
        return {ent['word']: ent['entity'] for ent in entities}

    def get_keywords(self, text):
        """
        Extract keywords from text.
        
        Args:
            text (str): Input text to analyze
            
        Returns:
            list: List of extracted keywords
        """
        keywords = self.keyword_extractor(text)
        return [kw['word'] for kw in keywords]

    def get_summary(self, text, max_length=150):
        """
        Generate a summary of the input text.
        
        Args:
            text (str): Input text to summarize
            max_length (int, optional): Maximum length of the summary.
                Defaults to 150 tokens.
                
        Returns:
            str: Generated summary
        """
        return self.summarizer(text, max_length=max_length, 
                             min_length=50, do_sample=False)[0]['summary_text'] 