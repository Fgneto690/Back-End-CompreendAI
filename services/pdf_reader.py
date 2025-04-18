import fitz

# função que recebe caminho de um PDF e retorna o texto
def ler_pdf(file_obj):
    try:
        file_obj.seek(0)
        documento = fitz.open(stream=file_obj.read(), filetype="pdf")
        texto = ""
        for pagina in documento:
            texto += pagina.get_text()
        documento.close()
        return texto

    except Exception as e:
        return None
