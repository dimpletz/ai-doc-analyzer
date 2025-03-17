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

## License

MIT