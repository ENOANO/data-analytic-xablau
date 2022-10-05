import xlrd

file = xlrd.open_workbook('estudantes.xlsx')
sheets = file.sheet_by_index(0)

alunos = []

for x in range(sheets.nrows):
    aluno = {}
    for y in range(sheets.ncols):
        if x != 0:
            aluno[sheets.cell_value(0, y)] = sheets.cell_value(x, y)
    
    if aluno:
        alunos.append(aluno)

for aluno in alunos:
    print("Aluno " + aluno["Nome"])
    media = (float(aluno["Ciencias"]) + float(aluno["Matematica"]) + float(aluno["Fisica"])) / 3
    print("Media " + str(media))
    assiduidade = (int(aluno["Frequencia"]) / 260) * 100
    if media >= 7 and assiduidade >= 70: 
        print("Situação: Aprovado")
    else:
        print("Situação: Reprovado")