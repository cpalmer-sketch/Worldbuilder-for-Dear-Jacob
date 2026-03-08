import re

def find_keywords(text):
    words = re.findall(r'\b\w+\b', text.lower())
    keywords = set(w for w in words if len(w) > 4)
    return sorted(keywords)

def suggest_connections(keywords, existing_docs):
    suggestions = []
    for kw in keywords:
        for doc in existing_docs:
            if kw.lower() in doc.lower():
                suggestions.append(f"Keyword '{kw}' found in {doc}")
    return suggestions
