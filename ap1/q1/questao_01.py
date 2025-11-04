alunos_nome = []
alunos_curso = []
alunos_nota = [] 

with open("./dados_alunos.txt", "r") as file:
    linha = file.readline()

    while linha:
        nome, curso, nota = linha.strip().split("#")
        alunos_nome.append(nome)
        alunos_curso.append(curso)
        alunos_nota.append(float(nota))
    
        linha = file.readline()


print("Média da turma:", round(sum(alunos_nota) / len(alunos_nota), 2))
print("Maior nota:", max(alunos_nota), "(", alunos_nome[alunos_nota.index(max(alunos_nota))], ")")
print("Menor nota:", min(alunos_nota), "(", alunos_nome[alunos_nota.index(min(alunos_nota))], ")")



