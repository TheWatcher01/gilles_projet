# Importing the required libraries
from bs4 import BeautifulSoup
import csv

# Function to extract text content from local HTML file using a CSS selector.


def extract_content_from_html(file_path, css_selector):
    # Open and read the local HTML file
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all elements matching the CSS selector
    elements = soup.select(css_selector)

    # Extract and return the text content of each element
    return [element.get_text(strip=True) for element in elements]


# Example usage
file_path = "/home/thewatcher/gilles_projet/fichier_html/google_dorks/site_www.in-cosmetics.com inurl_exhibitor-details intext__COMPANY EMAIL_ - Recherche Google.html"
css_selector = "#rso > div > div > div > div > div > span"
content_list = extract_content_from_html(file_path, css_selector)

# Write the results to a CSV file
with open('results.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for content in content_list:
        writer.writerow([content])
