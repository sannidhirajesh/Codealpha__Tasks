import re
import os

def read_file(filename):
    """Read content from input file"""
    if not os.path.exists(filename):
        print("File not found!")
        return ""
    
    with open(filename, "r") as file:
        return file.read()


def extract_emails(text):
    """Extract emails using regex"""
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+"
    return re.findall(pattern, text)


def save_emails(emails, output_file):
    """Save emails to output file"""
    with open(output_file, "w") as file:
        for email in emails:
            file.write(email + "\n")


def display_emails(emails):
    """Display emails on screen"""
    if len(emails) == 0:
        print("No emails found.")
    else:
        print("\n📧 Extracted Emails:")
        for email in emails:
            print(email)


def main():
    print("📂 Email Extraction Tool")

    input_file = "input.txt"
    output_file = "emails.txt"

    # Step 1: Read file
    text = read_file(input_file)

    if text == "":
        return

    # Step 2: Extract emails
    emails = extract_emails(text)

    # Step 3: Display emails
    display_emails(emails)

    # Step 4: Save emails
    save_emails(emails, output_file)

    print("\n✅ Emails saved to", output_file)


# Run the program
if __name__ == "__main__":
    main()
