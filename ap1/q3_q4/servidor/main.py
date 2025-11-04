from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

contador_id = 4


alunos_df = pd.DataFrame({
    "id": [1, 2, 3],
    "nome": ["Lucas", "Mateus", "Camila"],
    "nota": [4, 6.8, 9]
})

class Aluno(BaseModel):
    nome: str
    nota: float


@app.get("/alunos")
def listar_alunos():
    return alunos_df.to_dict(orient="records")


@app.get("/alunos/{nome}")
def obter_nota(nome:str):
    aluno = alunos_df[alunos_df["nome"] == nome]

    if aluno.empty:
        raise HTTPException(status_code=404, detail="aluno nao registrado")


    return aluno.to_dict(orient="records")[0].get("nota")    


@app.post("/alunos")
def adicionar_aluno(aluno: Aluno):
    global alunos_df, contador_id

    if alunos_df[alunos_df["nome"] == aluno.nome].empty:

        novo_aluno = {
            "id": contador_id,
            "nome": aluno.nome,
            "nota": aluno.nota
        }

        alunos_df = alunos_df._append(novo_aluno, ignore_index = True)

        contador_id = contador_id + 1

        return {
            "mensagem": "aluno criado com sucesso"
        }
    
    else:
        aluno_antigo_idx = alunos_df.index[alunos_df["nome"] == aluno.nome]
        alunos_df.loc[aluno_antigo_idx, ["nota"]] = [aluno.nota]

        return{
            "mensagem": "aluno teve nota atualizada"
        }

