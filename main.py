from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modelo de dados recebido
class SubjectRequest(BaseModel):
    subject: str

@app.post("/contar_palavras")
async def contar_palavras(dados: SubjectRequest):
    subject = dados.subject

    # Contar número de palavras (separa por espaços)
    num_palavras = len(subject.split())

    return {
        "subject": subject,
        "num_palavras": num_palavras
    }
