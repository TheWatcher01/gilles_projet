# Importing the BeautifulSoup library
from bs4 import BeautifulSoup

# Function to extract text content from local HTML file using a CSS selector


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

# Example usage (commented out to prevent execution)
# file_path = "path/to/your/localfile.html"
# css_selector = "#rso > div:nth-child(3) > div > div > div:nth-child(2) > div > span"
# content_list = extract_content_from_html(file_path, css_selector)
# for content in content_list:
#     print(content)
