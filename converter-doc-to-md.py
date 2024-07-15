import subprocess

def convert_md_to_pdf(md_file, pdf_file):
    try:
        # Convert Markdown to HTML
        html_file = md_file.replace('.md', '.html')
        subprocess.run(['gh-md-to-html', md_file, html_file], check=True)

        # Convert HTML to PDF
        subprocess.run(['wkhtmltopdf', html_file, pdf_file], check=True)

        print(f'Successfully converted {md_file} to {pdf_file}')
    except subprocess.CalledProcessError as e:
        print(f'Error: {e}')

# Usage example
md_file = 'BRUNO_LUIS_SANTINATO_Curriculum-Update-English-2024.md'
pdf_file = 'BRUNO_LUIS_SANTINATO_Curriculum-Update-English-2024.pdf'
convert_md_to_pdf(md_file, pdf_file)