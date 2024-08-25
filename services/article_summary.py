import openai
import os
from utils.env_loader import load_env_vars


"""
Service for generating article summaries.

This module contains the logic for generating summaries of articles
using the OpenAI API.

Modules:
    openai: OpenAI library for interacting with GPT models.
    os: Used to retrieve environment variables.
    utils.env_loader: Loads environment variables from the .env file.

Functions:
    summarize_article: Generates a summary for a given article link.
"""

load_env_vars()

openai.api_key = os.getenv("OPENAI_API_KEY")

def summarize_article(link: str) -> str:
    """
    Generates a summary for the given article link using the OpenAI API.
    
    Args:
        link (str): The URL of the article to summarize.
    
    Returns:
        str: The generated summary of the article.
    """
    # Simulate a summary; replace with actual API call
    response = openai.Completion.create(
        engine="gpt-4o-mini",
        prompt=f"Summarize the article at this link: {link}",
        max_tokens=150
    )
    summary = response.choices[0].text.strip()
    return summary

