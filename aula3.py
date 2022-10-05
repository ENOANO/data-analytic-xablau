alunos = [{"nome":"Vinicius", "ciencia":10, "matematica": 6, "frequencia":100}, 
{"nome":"Lucas", "ciencia":7, "matematica": 3, "frequencia":258}, 
{"nome":"Zaion", "ciencia":5, "matematica": 3, "frequencia":260}, 
{"nome":"Xablau", "ciencia":5, "matematica": 8, "frequencia":255}]


for aluno in alunos:
    print("Aluno " + aluno["nome"])
    media = (aluno["ciencia"] + aluno["matematica"]) / 2
    print("Media " + str(media))
    assiduidade = (aluno["frequencia"] / 260) * 100
    if media >= 7 and assiduidade >= 70: 
        print("Situação: Aprovado")
    else:
        print("Situação: Reprovado")