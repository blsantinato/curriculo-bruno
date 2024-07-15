import sys
import markdown
from docx import Document

def convert_md_to_docx(md_file, docx_file):
    # Read the Markdown file
    with open(md_file, 'r') as file:
        md_content = file.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(md_content)

    # Create a new Document
    doc = Document()

    # Add the HTML content to the Document
    doc.add_paragraph(html_content)

    # Save the Document as a DOCX file
    doc.save(docx_file)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python converter.py input.md output.docx')
        sys.exit(1)

    md_file = sys.argv[1]
    docx_file = sys.argv[2]

    convert_md_to_docx(md_file, docx_file)