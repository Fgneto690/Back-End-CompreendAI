from fastapi import FastAPI
from models.schemas import TextInput
from services.simplifier import simplificar_texto
from services.pdf_reader import ler_pdf
from fastapi import UploadFile, File
from fastapi import HTTPException
from services.ocr_reader import ler_imagem
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware


#iniciar servidor: uvicorn main:app --reload
app = FastAPI()
load_dotenv()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "CompreendAI backend is up!"}

@app.post("/simplify")
def simplify(input: TextInput):
    try:
        result = simplificar_texto(input.text)  # Simplifica o texto
        return {"simplified_text": result}  # Retorna o texto simplificado
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/upload_pdf")
def upload_pdf(file: UploadFile = File(...)):
    texto = ler_pdf(file.file)  # Extrai o texto do PDF
    if not texto:
        raise HTTPException(status_code=400, detail="Erro ao processar o PDF ou nenhum texto encontrado.")
    return {"texto": texto}  # Retorna o texto extraído

@app.post("/upload_image")
def upload_img(file: UploadFile = File(...)):
    texto = ler_imagem(file.file)

    if not texto:
        raise HTTPException(status_code=400, detail="Erro ao processar imagem")

    return {"texto": texto}