alunos = [
    {
        "nome":"Vinicius",
        "idade": 28
    }
]

aluno = {}
aluno["nome"] = input("Digite o nome")
aluno["idade"] = input("Digite a idade")
alunos.append(aluno)

for aluno in alunos:
    print(aluno)

