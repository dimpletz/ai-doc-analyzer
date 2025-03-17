"""
Tests for the main module.

This module contains tests for the main application functionality,
including argument parsing and document analysis features.
"""
import pytest
from app.main import main, parse_args
import os

def test_parse_args():
    """
    Test argument parsing functionality.
    """
    # Test with required arguments
    args = parse_args(['--input', 'test.txt', '--output', 'output.txt'])
    assert args.input == 'test.txt'
    assert args.output == 'output.txt'
    assert args.verbose is False
    assert args.quiet is False

    # Test with optional arguments
    args = parse_args(['--input', 'test.txt', '--output', 'output.txt', '--verbose', '--quiet'])
    assert args.verbose is True
    assert args.quiet is True

def test_main_with_valid_file(tmp_path):
    """
    Test main function with a valid input file.
    """
    # Create a test file
    test_file = tmp_path / "test.txt"
    test_file.write_text("This is a test document for analysis.")
    
    # Test with the created file
    assert main(['--input', str(test_file), '--output', str(tmp_path / "output.txt")]) == 0

def test_main_with_invalid_file():
    """
    Test main function with an invalid input file.
    """
    assert main(['--input', 'nonexistent.txt', '--output', 'output.txt']) == 1

def test_main_with_missing_args():
    """
    Test main function with missing required arguments.
    """
    assert main([]) == 1

def test_main_with_invalid_output_path(tmp_path):
    """
    Test main function with invalid output path.
    """
    # Create a test file
    test_file = tmp_path / "test.txt"
    test_file.write_text("This is a test document for analysis.")
    
    # Test with invalid output path
    assert main(['--input', str(test_file), '--output', '/invalid/path/output.txt']) == 1