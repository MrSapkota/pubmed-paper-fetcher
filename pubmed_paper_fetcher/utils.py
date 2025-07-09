import re

# Simple heuristic to check for non-academic institutions
def is_non_academic(affiliation: str) -> bool:
    keywords = ["pharma", "biotech", "inc", "ltd", "gmbh", "corp", "co.", "company", "solutions", "industries"]
    university_keywords = ["university", "institute", "college", "school", "hospital", "center", "centre", "academy", "research", "dept"]
    
    affiliation_lower = affiliation.lower()
    return any(k in affiliation_lower for k in keywords) and not any(k in affiliation_lower for k in university_keywords)


# Extract email from text using regex
def extract_email(text: str) -> str:
    match = re.search(r"[\w\.-]+@[\w\.-]+\.\w+", text)
    return match.group(0) if match else None
