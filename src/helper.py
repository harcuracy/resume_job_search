import fitz
from typing import List, Dict, Any
import langchain_groq
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
import os

# Load environment variables from .env file
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def get_groq_client():
    """
    Get the Groq client for making API calls.
    
    Returns:
        ChatGroq: An instance of the Groq client.
    """
    return ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name="meta-llama/llama-4-scout-17b-16e-instruct",
        max_tokens=1000,
        temperature=0.7,)



def ask_groq(prompt: str, max_tokens: int = 300) -> str:
    """
    Sends a prompt to the Groq API and returns the generated response.

    Args:
        prompt (str): The input prompt to send.
        max_tokens (int): Maximum number of tokens to generate.

    Returns:
        str: The generated text from Groq.
    """
    groq_client = get_groq_client()

    response = groq_client.invoke(
        prompt,
        max_tokens=max_tokens
    )

    return response.content if hasattr(response, "content") else str(response)


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract text from a PDF file using PyMuPDF.
    
    Args:
        pdf_path (str): Path to the PDF file.
    
    Returns:
        str: Extracted text from the PDF.
    """
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text




