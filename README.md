# AI Document Analyzer

An intelligent document analysis tool that leverages AI models to extract insights from documents.

Author: Ofelia Webb <ofelia.b.webb@gmail.com>

An intelligent document analysis tool that can extract text, identify entities, find keywords, and generate summaries from PDF, DOCX, and TXT files using state-of-the-art AI models.

## Features

- Text extraction from multiple document formats (PDF, DOCX, TXT)
- Named Entity Recognition (NER) to identify organizations, people, locations, etc.
- Keyword extraction to identify important terms
- AI-powered text summarization
- Interactive command-line interface

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/dimpletz/ai-doc-analyzer.git
   cd ai-doc-analyzer
   ```

2. Install Poetry if you haven't already:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. Install dependencies:
   ```bash
   poetry install
   ```

## Usage

You can run the application in several ways:

1. Interactive mode (will prompt for file path):
   ```bash
   poetry run python app/main.py
   ```

2. Direct mode with file path:
   ```bash
   poetry run python app/main.py path/to/your/document.pdf
   ```

3. As a Python module:
   ```bash
   poetry run python -m app.main
   ```

The analyzer will output:
- A concise summary of the document
- Named entities found (companies, people, locations, etc.)
- Key terms and concepts from the text

## Testing

The project includes comprehensive tests for all major components. To run the tests:

1. Run all tests:
   ```bash
   poetry run pytest
   ```

2. Run tests with coverage report:
   ```bash
   poetry run pytest --cov=app tests/
   ```

3. Run specific test files:
   ```bash
   poetry run pytest tests/test_main.py
   poetry run pytest tests/test_utils.py
   ```

The test suite includes:
- Unit tests for document text extraction
- Tests for AI model functionality (NER, keyword extraction, summarization)
- Integration tests for the main application
- Tests for error handling and edge cases
- Tests for the ModelManager singleton pattern and lazy loading

## Supported File Formats

- PDF (*.pdf)
- Microsoft Word (*.docx)
- Plain Text (*.txt)

## Dependencies

- transformers: For AI models (NER, summarization)
- torch: Deep learning backend
- pdfplumber: PDF text extraction
- python-docx: Word document processing
- scikit-learn: Machine learning utilities
- joblib: Parallel computing support
- pytest: Testing framework
- pytest-cov: Test coverage reporting

## License

MIT