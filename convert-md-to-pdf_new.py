import pdfkit
import markdown
import os

def convert_md_to_html(md_file, html_file):
    try:
        with open(md_file, 'r', encoding='utf-8') as file:
            markdown_text = file.read()
            # Converte markdown para HTML com suporte a imagens e tabelas
            html_text = markdown.markdown(
                markdown_text,
                extensions=['extra', 'tables', 'fenced_code']
            )

            # Adiciona um cabeçalho básico com CSS para imagens
            html_template = f"""
            <html>
            <head>
                <meta charset="utf-8">
                <style>
                    body {{ font-family: Arial, sans-serif; }}
                    img {{ max-width: 100%; height: auto; }}
                </style>
            </head>
            <body>
                {html_text}
            </body>
            </html>
            """

            with open(html_file, 'w', encoding='utf-8') as output_file:
                output_file.write(html_template)

        print("Conversão para HTML concluída!")
    except Exception as e:
        print(f"Falha na conversão para HTML: {str(e)}")

def convert_html_to_pdf(html_file, pdf_file):
    try:
        options = {
            "enable-local-file-access": None,  # Permite acesso a imagens locais
            "encoding": "UTF-8"
        }
        pdfkit.from_file(html_file, pdf_file, options=options)
        print("Conversão para PDF concluída!")
    except Exception as e:
        print(f"Falha na conversão para PDF: {str(e)}")

if __name__ == "__main__":
    md_file = "BRUNO_LUIS_SANTINATO_Curriculo-Atualizado-2024.md"
    html_file = "BRUNO_LUIS_SANTINATO_Curriculo-Atualizado-2026.html"
    pdf_file = "BRUNO_LUIS_SANTINATO_Curriculo-Atualizado-2026.pdf"
    convert_md_to_html(md_file, html_file)
    convert_html_to_pdf(html_file, pdf_file)