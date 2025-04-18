🧠 CompreendAI - Back-End
O Back-End do CompreendAI é responsável por processar textos, simplificar conteúdos complexos e realizar extrações de texto de PDFs e imagens. Ele utiliza FastAPI para criar uma API moderna e eficiente, além de integrar serviços de IA para simplificação de texto.

🚀 Tecnologias Utilizadas

Python 3.10+
FastAPI: Framework para criação de APIs rápidas e modernas.
PyMuPDF: Extração de texto de arquivos PDF.
Pytesseract + Pillow: OCR para leitura de texto em imagens.
Google Generative AI: Modelo Gemini para simplificação de texto.
Dotenv: Gerenciamento de variáveis de ambiente.

📦 Estrutura do Projeto

```bash 
    Back-End/
    ├── main.py                # Arquivo principal da API
    ├── models/
    │   └── schemas.py         # Schemas para validação de dados
    ├── services/
    │   ├── simplifier.py      # Serviço de simplificação de texto
    │   ├── pdf_reader.py      # Serviço de leitura de PDFs
    │   └── ocr_reader.py      # Serviço de OCR para imagens
    ├── .env                   # Variáveis de ambiente
    ├── requirements.txt       # Dependências do projeto
    └── README.md              # Documentação do Back-End
``` 

🛠️ Funcionalidades

POST /simplify: Recebe um texto e retorna a versão simplificada.
POST /upload_pdf: Recebe um arquivo PDF e extrai o texto.
POST /upload_image: Recebe uma imagem e extrai o texto usando OCR.

📦 Requisitos

Python: Versão 3.10 ou superior.
Conta no Google AI Studio: Para utilizar o modelo de simplificação de texto.

🛠️ Instalação
Clone o repositório:
```bash 
git clone https://github.com/seu-usuario/compreendai-backend.git
cd compreendai/Back-End
```

Crie e ative um ambiente virtual:
```bash 
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```
Instale as dependências:
```bash 
pip install -r requirements.txt
```
Configure o arquivo .env: Crie um arquivo .env na raiz do Back-End com o seguinte conteúdo:

GOOGLE_API_KEY=sua_chave_api_aqui

Inicie o servidor:
```bash 
uvicorn main:app --reload
```
Acesse a documentação interativa:

http://localhost:8000/docs

📌 Roadmap
✅ Integração com IA (Google Generative AI).
✅ Upload e leitura de PDFs.
✅ Upload e leitura de imagens com OCR.
✅ Simplificação de texto.
🟡 Exportar resultado em formato PDF.
🟡 Níveis de simplificação (leve, moderada, intensa).

👤 Autor
Desenvolvido por Francisco Soares como parte do projeto CompreendAI, com foco em acessibilidade e inclusão.
Linkedin: https://www.linkedin.com/in/francisco-soares-6b285a235/
GitHub: https://github.com/Fgneto690

📄 Licença
Este projeto é apenas para fins educacionais, testes e uso pessoal.

