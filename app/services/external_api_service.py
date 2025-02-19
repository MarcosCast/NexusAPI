import httpx

def call_external_api(query: str) -> dict:
    """
    Aqui estou simulando a chamada, mas n posso esquecer de implementar a chamada real antes de mandar para prod
    """
    # Exemplo básico utilizando httpx:
    # response = httpx.post("https://api.exemplo.com/query", json={"query": query})
    # return response.json()
    return {"query": query, "response": "Resposta simulada da API externa."}
