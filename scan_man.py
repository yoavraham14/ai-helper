import os
import subprocess
import json
from tqdm import tqdm  # For progress bar

def extract_man_pages():
    try:
        # Get all available commands from `man -k .`
        man_pages = subprocess.check_output(['man', '-k', '.'], stderr=subprocess.DEVNULL).decode(errors='ignore').split('\n')
        man_pages = [page.split()[0] for page in man_pages if page]  # Extract only command names
        
        total_pages = len(man_pages)
        results = {}

        print(f"Scanning {total_pages} MAN pages...")

        with tqdm(total=total_pages, desc="Progress", unit="man") as pbar:
            for i, cmd in enumerate(man_pages):
                try:
                    # Update the progress bar with the current command
                    pbar.set_description(f"Scanning: {cmd}")
                    
                    # Format the output to plain text
                    man_text = subprocess.check_output(['man', '--ascii', cmd], stderr=subprocess.DEVNULL).decode(errors='ignore')
                    results[cmd] = man_text
                except subprocess.CalledProcessError:
                    results[cmd] = "Failed to retrieve"
                finally:
                    # Update the progress bar
                    pbar.update(1)

        return results

    except Exception as e:
        print(f"Error: {e}")
        return {}

# Save extracted data to a JSON file
man_data = extract_man_pages()
with open('man_pages.json', 'w') as file:
    json.dump(man_data, file)

print("MAN pages extracted and saved to man_pages.json")

