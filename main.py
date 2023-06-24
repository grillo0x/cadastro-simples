from fastapi import FastAPI

pessoas = []
app = FastAPI()

@app.get("/cadastro")
async def register(nome: str, email: str):
    pessoa = {"nome": nome, "email": email}
    pessoas.append(pessoa)
    return pessoa

@app.get("/listar")
async def list():
    return pessoas

