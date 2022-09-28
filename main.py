alunos = [
    {
        "nome":"Vinicius",
        "idade": 28
    }
]

for x in range(int(input("Quantos alunos serão cadastros\n"))):
    aluno = {}
    aluno["nome"] = input("Digite o nome")
    aluno["idade"] = input("Digite a idade")
    aluno["telefo"] = input("digite o telefone")
    alunos.append(aluno)

for aluno in alunos:
    print(aluno)

