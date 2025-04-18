import pytesseract
from PIL import Image, ImageFilter, ImageOps

def preprocessar_imagem(imagem):
    imagem = imagem.convert("L")  # Converte para tons de cinza
    imagem = ImageOps.invert(imagem)  # Inverte preto e branco
    imagem = imagem.filter(ImageFilter.SHARPEN)  # Aplica leve nitidez
    return imagem

def ler_imagem(file_obj):
    try:
        file_obj.seek(0)
        imagem = Image.open(file_obj)
        imagem = preprocessar_imagem(imagem)
        texto = pytesseract.image_to_string(imagem, lang='por')
        return texto
    except Exception as e:
        return None
