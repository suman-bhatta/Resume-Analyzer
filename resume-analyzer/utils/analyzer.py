def find_skills(text, skills):
    return [s for s in skills if s.lower() in text.lower()]

def highlight(text, skills):
    for skill in skills:
        text = text.replace(skill, f"**:green[{skill}]**")
    return text
