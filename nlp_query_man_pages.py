import json
import spacy
import re

# Load Spacy model
nlp = spacy.load("en_core_web_sm")

# Load man pages from json
with open('man_pages.json') as f:
    man_pages = json.load(f)

def search_man_pages(query):
    keywords = query.lower().split()

    results = []
    for man_page, details in man_pages.items():
        # Ensure details is a dictionary (not a string)
        if isinstance(details, dict):
            relevant_sections = {}
            for section, content in details.items():
                if isinstance(content, str):  # Check if content is a string (man text)
                    if any(keyword in content.lower() for keyword in keywords):
                        # Extract only a snippet from the section
                        snippet = content[:500]  # Limit snippet size
                        relevant_sections[section] = snippet

            # If relevant sections found, add to results
            if relevant_sections:
                results.append({
                    'man_page': man_page,
                    'relevant_sections': relevant_sections
                })
        else:
            print(f"Skipping {man_page}, as its details are not in the expected format.")

    return results

def format_answer(results):
    answer = ""
    for result in results:
        answer += f"Man Page: {result['man_page']}\n"
        for section, content in result['relevant_sections'].items():
            answer += f"\nSection: {section.capitalize()}\n"
            answer += f"{content}\n"
        answer += "\n"
    return answer

# Example usage
user_query = "I want to create an XFS filesystem"
results = search_man_pages(user_query)

if results:
    print(format_answer(results))
else:
    print("No relevant information found.")

