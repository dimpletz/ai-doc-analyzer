"""
AI Document Analyzer - Main Script

This script serves as the entry point for the document analysis tool. It handles:
1. Command-line argument parsing
2. User input for file paths
3. Orchestration of the document analysis process

The analyzer can process PDF, DOCX, and TXT files to:
- Extract and summarize text
- Identify named entities (people, organizations, locations)
- Extract key terms and concepts

Usage:
    python app/main.py                     # Interactive mode
    python app/main.py path/to/file.pdf    # Direct mode
    python -m app.main                     # Module mode

Author: Ofelia Webb <ofelia.b.webb@gmail.com>
"""

import argparse
import os
import sys

# Add the project root directory to Python path for imports
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from app.utils.document_analyzer import extract_text, analyze_text, summarize_text

def get_file_path():
    """
    Get the document file path either from command line arguments or user input.
    
    The function first checks for command-line arguments. If none are provided,
    it prompts the user interactively until a valid file path is entered.
    
    Returns:
        str: Valid path to an existing document file
    """
    parser = argparse.ArgumentParser(description="Analyze a document file.")
    parser.add_argument("file_path", type=str, nargs='?', help="Path to the document file")
    args = parser.parse_args()

    if args.file_path:
        return args.file_path
    
    while True:
        file_path = input("\nEnter the path to your document (PDF, DOCX, or TXT): ").strip()
        if os.path.exists(file_path):
            return file_path
        print(f"Error: File '{file_path}' does not exist. Please try again.")

def main(file_path):
    """
    Main function to process and analyze the document.
    
    This function orchestrates the document analysis process:
    1. Extracts text from the document
    2. Performs named entity recognition
    3. Extracts keywords
    4. Generates a summary
    
    Args:
        file_path (str): Path to the document file to analyze
    """
    print(f"\nProcessing file: {file_path}")

    try:
        text = extract_text(file_path)
        if not text:
            print("Error: No text extracted from the document.")
            return
        
        # Named Entity Recognition & Keyword Extraction
        entities, keywords = analyze_text(text)

        # Summarization (Limiting input size to avoid memory overload)
        summary = summarize_text(text[:1000])  

        # Display results
        print("\n--- Extracted Summary ---\n", summary)
        print("\n--- Named Entities ---\n", entities)
        print("\n--- Keywords ---\n", keywords[:20])  # Show top 20 keywords

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = get_file_path()
    main(file_path)