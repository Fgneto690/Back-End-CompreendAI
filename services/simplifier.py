import google.generativeai as genai
from dotenv import load_dotenv
import os

# Tenta carregar o .env
loaded = load_dotenv() 


# Tenta configurar a API
try:
    # Tenta pegar a chave da variável de ambiente
    api_key = os.environ['GOOGLE_API_KEY'] 
    # Não imprima a chave inteira por segurança, mas pode mostrar uma parte para confirmar:
    genai.configure(api_key=api_key)
except KeyError:
    exit() 

# Define o modelo
modelo = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")

# Função de simplificação
def simplificar_texto(texto):
    try:
        response = modelo.generate_content(
            f"Reescreva o texto abaixo de forma clara, simples e acessível: {texto}"
        )
        # Vamos tentar pegar o conteúdo da forma esperada
        if response and response.candidates:
            return response.candidates[0].content.parts[0].text
        else:
            return "⚠️ Erro: resposta inesperada da IA"
    except Exception as e:
        return "⚠️ Erro ao processar o texto na IA."

