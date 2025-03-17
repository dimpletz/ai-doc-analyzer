"""
Tests for the utils module.

This module contains tests for the document analyzer and model manager functionality,
including text extraction, analysis, and summarization features.
"""
import pytest
from app.utils import example_util_function
from app.utils.document_analyzer import extract_text, analyze_text, summarize_text
from app.models.model_manager import ModelManager
import os

def test_example_util_function():
    """
    Test the example utility function.
    """
    assert example_util_function() == "This is an example utility function"

@pytest.fixture
def sample_text():
    """
    Fixture providing sample text for testing.
    """
    return """
    The quick brown fox jumps over the lazy dog.
    This is a sample text for testing the document analyzer.
    It contains multiple sentences and some basic punctuation.
    """

@pytest.fixture
def model_manager():
    """
    Fixture providing a ModelManager instance for testing.
    """
    return ModelManager()

def test_extract_text_from_txt(tmp_path, sample_text):
    """
    Test text extraction from a TXT file.
    """
    # Create a test file
    test_file = tmp_path / "test.txt"
    test_file.write_text(sample_text)
    
    # Test extraction
    extracted_text = extract_text(str(test_file))
    assert extracted_text.strip() == sample_text.strip()

def test_extract_text_invalid_file():
    """
    Test text extraction with an invalid file.
    """
    with pytest.raises(ValueError):
        extract_text("nonexistent.txt")

def test_analyze_text(model_manager, sample_text):
    """
    Test text analysis functionality.
    """
    # Test entity recognition
    entities = model_manager.get_entities(sample_text)
    assert isinstance(entities, list)
    
    # Test keyword extraction
    keywords = model_manager.get_keywords(sample_text)
    assert isinstance(keywords, list)
    assert len(keywords) > 0

def test_summarize_text(model_manager, sample_text):
    """
    Test text summarization functionality.
    """
    # Test summarization
    summary = model_manager.get_summary(sample_text)
    assert isinstance(summary, str)
    assert len(summary) > 0
    assert len(summary) < len(sample_text)

def test_model_manager_singleton():
    """
    Test that ModelManager follows the singleton pattern.
    """
    manager1 = ModelManager()
    manager2 = ModelManager()
    assert manager1 is manager2

def test_model_manager_lazy_loading():
    """
    Test that models are loaded lazily.
    """
    manager = ModelManager()
    # Models should not be loaded initially
    assert manager._ner is None
    assert manager._keyword_extractor is None
    assert manager._summarizer is None
    
    # Models should be loaded when first accessed
    manager.get_entities("test")
    assert manager._ner is not None
    
    manager.get_keywords("test")
    assert manager._keyword_extractor is not None
    
    manager.get_summary("test")
    assert manager._summarizer is not None