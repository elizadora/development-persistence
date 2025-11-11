import httpx
import asyncio

BASE_URL = "http://127.0.0.1:8000"

def listar_produtos():
    resposta = httpx.get(f"{BASE_URL}/produtos")
    return(resposta.json())

def obter_produto(id):
    resposta = httpx.get(f"{BASE_URL}/produtos/{id}")
    return(resposta.json())

async def criar_produto(cliente, produto):
    resposta = await cliente.post(
        f"{BASE_URL}/produtos",
        json={"nome": produto.get("nome"), "categoria": produto.get("categoria"), "preco": produto.get("preco")}
    )
    return(resposta.json())

async def atualizar_produto(cliente, id, produto):
    resposta = await cliente.put(
        f"{BASE_URL}/produtos/{id}",
        json={"nome": produto.get("nome"), "categoria": produto.get("categoria"), "preco": produto.get("preco")}
    )
    return(resposta.json())


async def apagar_produto(cliente, id):
    resposta = await cliente.delete(f"{BASE_URL}/produtos/{id}")
    return(resposta.json())

def produto_maior_valor():
    resposta = httpx.get(f"{BASE_URL}/produtos/maior-valor")
    return(resposta.json())

def produto_menor_valor():
    resposta = httpx.get(f"{BASE_URL}/produtos/menor-valor")
    return(resposta.json())

def media():
    resposta = httpx.get(f"{BASE_URL}/produtos/media")
    return(resposta.json())

def produtos_acima_media():
    resposta = httpx.get(f"{BASE_URL}/produtos/acima-media")
    return(resposta.json())

def produtos_abaixo_media():
    resposta = httpx.get(f"{BASE_URL}/produtos/abaixo-media")
    return(resposta.json())


async def controlador():
    while True:
        async with httpx.AsyncClient() as cliente:
            print("Escolha uma das opcoes abaixo:")
            print("1 - Listar todos os produtos")
            print("2 - Obter um produto pelo ID")
            print("3 - Criar um novo produto")
            print("4 - Atualizar um produto existente")
            print("5 - Apagar um produto")
            print("6 - Produto de maior valor")
            print("7 - Produto de menor valor")
            print("8 - Media dos valores dos produtos")
            print("9 - Produtos acima da media")
            print("10 - Produtos abaixo da media")

            escolha = input("Digite o numero da opcao desejada: ")

            if escolha == "1":
                print(listar_produtos())

            elif escolha == "2":
                id = input("Digite o ID do produto: ")
                print(obter_produto(id))

            elif escolha == "3":
                nome = input("Digite o nome do produto: ")
                categoria = input("Digite a categoria do produto: ")
                preco = float(input("Digite o preco do produto: "))
                produto = {"nome": nome, "categoria": categoria, "preco": preco}
                print(await criar_produto(cliente, produto))

            elif escolha == "4":
                id = input("Digite o ID do produto a ser atualizado: ")
                nome = input("Digite o novo nome do produto: ")
                categoria = input("Digite a nova categoria do produto: ")
                preco = float(input("Digite o novo preco do produto: "))
                produto = {"nome": nome, "categoria": categoria, "preco": preco}
                print(await atualizar_produto(cliente, id, produto))

            elif escolha == "5":
                id = input("Digite o ID do produto a ser apagado: ")
                print(await apagar_produto(cliente,id))

            elif escolha == "6":
                print(produto_maior_valor())

            elif escolha == "7":
                print(produto_menor_valor())

            elif escolha == "8":
                print(media())

            elif escolha == "9":
                print(produtos_acima_media())

            elif escolha == "10":
                print(produtos_abaixo_media())
                
            elif escolha == "11":
                break
            else:
                print("Opcao invalida. Por favor, tente novamente.")



asyncio.run(controlador())