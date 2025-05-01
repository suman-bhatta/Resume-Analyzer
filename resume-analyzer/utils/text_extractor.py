import re
from pdfminer.high_level import extract_text

def get_text(pdf):
    return extract_text(pdf)

def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group(0) if match else None

def extract_phone(text):
    match = re.search(r'(\+?\d{1,3}[\s-]?)?\d{10}', text)
    return match.group(0) if match else None

def split_sections(text):
    sections = {}
    sections["experience"] = re.findall(r'(?:at\s)?(\b[A-Z][a-z]+\b).*(\d{4})', text)
    sections["education"] = re.findall(r'(Bachelor|Master|PhD)[\w\s,]*', text, re.I)
    return sections
