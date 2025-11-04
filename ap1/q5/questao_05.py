import requests
from bs4 import BeautifulSoup

with open("jogadas.html", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

tabela = soup.find("table")
vitorias_1 = 0


linhas = tabela.find_all("tr")

for linha in linhas:
    jogadas = linha.find_all("td")
    
    if jogadas and len(jogadas) > 0:
        jogador_1 = jogadas[0].get_text()
        jogador_2 = jogadas[1].get_text()

        if (jogador_1 == "pedra" and jogador_2 == "tesoura") or (jogador_1 == "tesoura" and jogador_2 == "papel") or (jogador_1 == "papel" and jogador_2 == "pedra"):
            vitorias_1 += 1
        
print("Vitorias do jogador 1:", vitorias_1)
    
