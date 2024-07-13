import pdfkit
import markdown

def convert_md_to_html(md_file, html_file):
        try:
            with open(md_file, 'r') as file:
                markdown_text = file.read()
                html_text = markdown.markdown(markdown_text)
                with open(html_file, 'w') as output_file:
                    output_file.write(html_text)
            print("Conversion to HTML successful!")
        except Exception as e:
            print(f"Conversion to HTML failed: {str(e)}")

def convert_html_to_pdf(html_file, pdf_file):
        try:
            pdfkit.from_file(html_file, pdf_file)
            print("Conversion to PDF successful!")
        except Exception as e:
            print(f"Conversion to PDF failed: {str(e)}")

if __name__ == "__main__":
        md_file = "BRUNO_LUIS_SANTINATO_Curriculum-Update-English-2024.md"
        html_file = "BRUNO_LUIS_SANTINATO_Curriculum-Update-English-2024.html"
        pdf_file = "BRUNO_LUIS_SANTINATO_Curriculum-Update-English-2024.pdf"
        convert_md_to_html(md_file, html_file)
        convert_html_to_pdf(html_file, pdf_file)