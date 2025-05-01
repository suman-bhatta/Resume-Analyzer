from pdfminer.high_level import extract_text
from sentence_transformers import SentenceTransformer, util
import json
import re

model = SentenceTransformer('all-MiniLM-L6-v2')

def extract_text_from_pdf(pdf_file):
    return extract_text(pdf_file)

def load_skills():
    with open('data/skills.json') as f:
        return json.load(f)

def extract_skills(text, skill_list):
    text = text.lower()
    return [skill for skill in skill_list if skill.lower() in text]

def extract_email(text):
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group(0) if match else "Not found"

def extract_phone(text):
    match = re.search(r'(\+?\d{1,3}[\s-]?)?\d{10}', text)
    return match.group(0) if match else "Not found"

def calculate_similarity(text1, text2):
    emb1 = model.encode(text1, convert_to_tensor=True)
    emb2 = model.encode(text2, convert_to_tensor=True)
    return round(util.pytorch_cos_sim(emb1, emb2).item() * 100, 2)
