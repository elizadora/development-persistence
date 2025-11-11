from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import asyncio
import pandas as pd

# incializar API
app = FastAPI()
lock = asyncio.Lock()

# configurar CORS para permitir requisições do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# modelo do produto
class Produto(BaseModel):
    nome: str
    categoria: str
    preco: float


# pegando dados do csv 
produtos_df = pd.read_csv("produtos.csv")
contador_id = 0

if not produtos_df.empty:
    contador_id = int(produtos_df["id"].max() + 1)
else:
    contador_id = 1


# retorna todos os produtos
@app.get("/produtos")
def listar_produtos():
    return JSONResponse(content=produtos_df.to_dict(orient="records"), status_code=200)

# retorna o produto com o id formatado
@app.get("/produtos/{id:int}")
def obter_produto(id: int):
    produto = produtos_df[produtos_df["id"] == id]

    if produto.empty:
        raise HTTPException(status_code=404, detail=f"Produto com id {id} não encontrado")
    
    return JSONResponse(content=produto.to_dict(orient="records")[0], status_code=200)

# cadastrar um novo produto
@app.post("/produtos")
async def criar_produto(produto: Produto):
    async with lock:
        global produtos_df, contador_id
        novo_produto = {
            "id": contador_id,
            "nome": produto.nome,
            "categoria": produto.categoria,
            "preco": produto.preco
        }
        produtos_df = produtos_df._append(novo_produto, ignore_index=True)
        produtos_df.to_csv("produtos.csv", index=False)

        contador_id += 1

    return JSONResponse(
        content={
            "messagem": "Produto criado com sucesso",
            "produto": novo_produto
        },
        status_code=201
    )

# atualizar os dados de um produto existente
@app.put("/produtos/{id}")
async def atualizar_produto(id: int, produto: Produto):
    async with lock:
        global produtos_df

    produto_antigo_idx = produtos_df.index[produtos_df["id"] == id]

    if produto_antigo_idx.empty:
        raise HTTPException(status_code=404, detail=f"Produto com id {id} não encontrado")

    produtos_df.loc[produto_antigo_idx, ["nome", "categoria", "preco"]] = [produto.nome, produto.categoria, produto.preco]
    produtos_df.to_csv("produtos.csv", index=False)

    return JSONResponse(
        content={
            "messagem": f"Produto {id} atualizado com sucesso",
            "produto": produtos_df.loc[produto_antigo_idx].to_dict(orient="records")[0]
        },
        status_code=200
    )

# remover o produto com o id informado
@app.delete("/produtos/{id}")
async def apagar_produto(id: int):
    async with lock:
        global produtos_df

        produto_apagar_idx = produtos_df.index[produtos_df["id"] == id]

        if produto_apagar_idx.empty:
            raise HTTPException(status_code=404, detail=f"Produto com id {id} não encontrado")
        
        produtos_df = produtos_df.drop(produto_apagar_idx).reset_index(drop=True)
        produtos_df.to_csv("produtos.csv", index=False)
        
        return JSONResponse(
            content={
                "messagem": f"Produto {id} apagado com sucesso"
            },
            status_code=200
        )

#retorna os produtos com o maior valor
@app.get("/produtos/maior-valor")
def maior_valor_produto():
    produto_valor = produtos_df["preco"].max()
    
    produtos_maior_valor = produtos_df[produtos_df["preco"] == produto_valor]
    print(produtos_maior_valor)

    return JSONResponse(
        content=produtos_maior_valor[["nome", "preco"]].to_dict(orient="records"),
        status_code=200
    )

#retorna os produtos com o menor valor
@app.get("/produtos/menor-valor")
def menor_valor_produto():
    produto_valor = produtos_df["preco"].min()
    
    produtos_menor_valor = produtos_df[produtos_df["preco"] == produto_valor]

    return JSONResponse(
        content=produtos_menor_valor[["nome", "preco"]].to_dict(orient="records"),
        status_code=200
    )

# retorna a média dos preços
@app.get("/produtos/media")
def media_preco_produto():
    media = produtos_df["preco"].mean()

    return JSONResponse(
        content={"media": round(media, 2)},
        status_code=200
    )

# retorna os produtos mais caros(acima da media)
@app.get("/produtos/acima-media")
def produtos_acima_media():
    media = produtos_df["preco"].mean()
    produtos_acima_media = produtos_df[produtos_df["preco"] >= media]

    return JSONResponse(
        content=produtos_acima_media.to_dict(orient="records"),
        status_code=200
    )

# retorna os produtos mais baratos(abaixo da media)
@app.get("/produtos/abaixo-media")
def produtos_abaixo_media():
    media = produtos_df["preco"].mean()
    produtos_abaixo_media = produtos_df[produtos_df["preco"] < media]

    return JSONResponse(
        content=produtos_abaixo_media.to_dict(orient="records"),
        status_code=200
    )


