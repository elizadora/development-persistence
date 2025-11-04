#pip install httpx
import httpx

BASE_URL = "http://127.0.0.1:8000"

def criar_aluno(aluno):
    resp = httpx.post(
        f"{BASE_URL}/alunos",
        json={"nome": aluno.get("nome"), "nota": aluno.get("nota")}
    )
    print(resp.json()["mensagem"])

def listar_alunos():
    resp = httpx.get(f"{BASE_URL}/alunos")
    print(resp.json())

def obter_nota(nome):
    resp = httpx.get(f"{BASE_URL}/alunos/{nome}")
    return resp.json()

print("==========Listando alunos ==========")
listar_alunos()

print("==========Criando alunos ==========")
criar_aluno({"nome":"Ana","nota":8.5})
criar_aluno({"nome":"Bruno","nota":5.0})

print("==========Listando alunos criados ==========")
listar_alunos()

print("==========Atualizando nota da Ana ==========")
criar_aluno({"nome":"Ana","nota":9.0})

print("==========Listando alunos atualizados ==========")
listar_alunos()

print("==========Obtendo nota do Bruno ==========")
print(obter_nota("Bruno"))