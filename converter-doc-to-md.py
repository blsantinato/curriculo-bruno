import docx
from markdownify import markdownify as md
import os

def ler_documento_word(caminho_arquivo):
    doc = docx.Document(caminho_arquivo)
    conteudo = []
    for p in doc.paragraphs:
        conteudo.append(p.text)
    return "\n".join(conteudo)

def converter_para_markdown(conteudo):
    return md(conteudo)

def salvar_markdown(caminho_arquivo, conteudo_md):
    with open(caminho_arquivo, 'w', encoding='utf-8') as f:
        f.write(conteudo_md)

def converter_word_para_markdown(caminho_entrada, caminho_saida):
    conteudo_word = ler_documento_word(caminho_entrada)
    conteudo_md = converter_para_markdown(conteudo_word)
    salvar_markdown(caminho_saida, conteudo_md)
    print(f"Conversão concluída. Arquivo Markdown salvo em: {caminho_saida}")

# Exemplo de uso:
caminho_entrada = 'BRUNO_LUIS_SANTINATO_Curriculo-Atualizado-2024.docx'
caminho_saida = 'BRUNO_LUIS_SANTINATO_Curriculo-Atualizado-2024.md'
converter_word_para_markdown(caminho_entrada, caminho_saida)
