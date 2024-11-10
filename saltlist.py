#pip install pymupdf

import fitz  # PyMuPDF
import re  # Regular expressions for pattern matching
# Define your input file and output file paths
input_pdf = 'Lab 6 - Salted Hashes.pdf'  # Update with your actual input file path
output_file = 'salts.txt'      # Output file to save words


# Define a function to clean text according to the rules
#def clean_text(text):
    # Step 1: Preserve URLs (domains with dots) as single words by temporarily replacing them with placeholders
#    url_pattern = r'\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b'  # Match URLs like www.example.com, example.com, etc.
#    urls = re.findall(url_pattern, text)  # Find all URLs
#    for idx, url in enumerate(urls):
#        # Replace the URL with a unique placeholder (e.g., <URL0>, <URL1>, etc.)
#        text = text.replace(url, f"<URL{idx}>")

# Define a function to clean text according to the rules
def clean_text(text):
    # Step 1: Preserve URLs (domains with dots) as single words by temporarily replacing them with placeholders
    url_pattern = r'\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b'  # Match URLs like www.example.com, example.com, etc.
    urls = re.findall(url_pattern, text)  # Find all URLs
    for idx, url in enumerate(urls):
        # Replace the URL with a unique placeholder (e.g., <URL0>, <URL1>, etc.)
        text = text.replace(url, f"<URL{idx}>")

    # Step 2: Replace parentheses with space
    text = re.sub(r'[()]+', ' ', text)  # Replace parentheses with space

    # Step 3: Remove punctuation marks followed by a space, but keep the space
    text = re.sub(r'[.,:;-]\s+', ' ', text)  # Replace period, comma, colon, hyphen + space with a space

    # Step 4: Remove any remaining punctuation (periods, commas, colons, hyphens, etc.)
    text = re.sub(r'[.,:;-]', '', text)  # Remove remaining punctuation marks

    # Step 5: Split by whitespace and process each word
    words = text.split()

    # Step 6: Reinsert URLs back into the text
    for idx, word in enumerate(words):
        if word.startswith("<URL"):  # Detect placeholders for URLs
            url_idx = int(word[4:-1])  # Extract the index from the placeholder like <URL0>
            words[idx] = urls[url_idx]  # Reinsert the original URL

    return words


# Open the PDF file using PyMuPDF
try:
    with fitz.open(input_pdf) as pdf_document:
        # Using a set to store unique words
        unique_words = set()

        # Iterate over each page in the PDF
        for page_num in range(pdf_document.page_count):
            page = pdf_document.load_page(page_num)  # Load the page

            # Extract text from the page
            text = page.get_text("text")  # Extract plain text from the page

            # Check if any text is extracted
            if not text.strip():
                print(f"Warning: No text extracted from page {page_num + 1}")
                continue  # Skip pages with no text

            # Clean the text to remove unwanted characters and process based on the rules
            words = clean_text(text)

            # Add words to the set to ensure uniqueness
            unique_words.update(words)

        # Write unique words to the output file
        with open(output_file, 'w', encoding='utf-8') as outfile:
            for word in unique_words:
                outfile.write(word + '\n')

        print(f"Unique words from PDF have been saved to {output_file}")

except Exception as e:
    print(f"Error: {e}")