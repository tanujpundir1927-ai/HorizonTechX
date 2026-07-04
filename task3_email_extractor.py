import re
import os

def extract_emails():
    # Creating a sample file for demonstration
    sample_text = """
    Hello, contact us at support@example.com for queries.
    You can also email admin@domain.org or sales@company.net.
    """
    with open("sample_emails.txt", "w") as f:
        f.write(sample_text)
        
    print("Reading from 'sample_emails.txt'...")
    
    # Extracting emails using regex
    with open("sample_emails.txt", "r") as file:
        content = file.read()
        
    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)
    
    # Saving to a new file
    with open("extracted_emails.txt", "w") as out_file:
        for email in emails:
            out_file.write(email + "\n")
            
    print(f"Found {len(emails)} emails.")
    print(f"Extracted Emails: {emails}")
    print("Saved them to 'extracted_emails.txt'.")

if __name__ == "__main__":
    extract_emails()