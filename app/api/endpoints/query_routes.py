from fastapi import APIRouter

router = APIRouter()

@router.post("/ask")
async def ask_query(question: str):
    """
    Estou simulando uma resposta até configurar as respostas para as perguntas nesse endpoint.
    """
    return {"question": question, "answer": "Esta é uma resposta simulada."}
