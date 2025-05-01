def calculate_score(matches, total, weight):
    if total == 0:
        return 0
    return (len(matches) / total) * weight

def total_score(skills_score, exp_score, edu_score):
    return round(skills_score + exp_score + edu_score, 2)
