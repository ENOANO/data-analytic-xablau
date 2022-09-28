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

for dd in alunos:
    print(dd)