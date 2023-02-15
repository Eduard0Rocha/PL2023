import pandas as pd

def parseLine(line):

    if (line[0] == 'i'): return None #primeira linha do ficheiro

    info = line.split(",")

    return (int(info[0]), info[1], int(info[2]), int(info[3]), int(info[4]), info[5] == '1')

def readData():

    res = list()

    with open("myheart.csv") as f:

        for line in f:
  
            res.append(parseLine(line[:-1]))

    res.pop(0)

    return res

def tem_doenca(entry):

    return entry[5]

def e_homem(entry):

    return entry[1] == "M"

def nr_homens_e_mulheres(data):

    nr_homens = 0
    nr_mulheres = 0

    for entry in data:

        if (e_homem(entry)):

            nr_homens += 1
        
        else:

            nr_mulheres += 1

    return (nr_homens,nr_mulheres)

def nr_homens_e_mulheres_com_doenca(data):

    nr_homens = 0
    nr_mulheres = 0

    for entry in data:

        if (tem_doenca(entry)):

            if (e_homem(entry)):

                nr_homens += 1
            
            else:

                nr_mulheres += 1

    return (nr_homens,nr_mulheres)

def distr_por_sexo(data):

    data_nr_homens_mulheres = nr_homens_e_mulheres(data)
    data_nr_homens_mulheres_com_doenca = nr_homens_e_mulheres_com_doenca(data)

    table = [[data_nr_homens_mulheres_com_doenca[0],data_nr_homens_mulheres_com_doenca[1]],[data_nr_homens_mulheres[0]-data_nr_homens_mulheres_com_doenca[0],data_nr_homens_mulheres[1]-data_nr_homens_mulheres_com_doenca[1]]]

    return pd.DataFrame(table,columns = ["Homem","Mulher"],index=["Com Doença","Sem Doença"])

def idade_no_escalao(entry,min_idade,max_idade):

    idade = entry[0]

    return idade >= min_idade and idade <= max_idade 

def distr_escalao(min_idade, max_idade, data):

    nr_cm_doenca = 0
    nr_sem_doenca = 0

    for entry in data:

        if (idade_no_escalao(entry,min_idade,max_idade)):

            if (tem_doenca(entry)):

                nr_cm_doenca += 1

            else:

                nr_sem_doenca += 1

    return [nr_cm_doenca,nr_sem_doenca]

#MIN_IDADE: 28
#MAX_IDADE: 77

def distr_por_idade(data):

    min_idade = 25

    table = []
    rows = []

    while (min_idade < 80):

        table.append(distr_escalao(min_idade,min_idade+4,data))
        
        rows.append(f"[{min_idade},{min_idade+4}]")

        min_idade += 5

    return pd.DataFrame(table,columns = ["Com Doença", "Sem Doença"],index=rows)

def get_colesterol(entry):

    return entry[3]

def colestrol_no_nivel(entry,min_c,max_c):

    c = get_colesterol(entry)

    return c >= min_c and c <= max_c

def distr_nivel_c(min_c,max_c,data):

    nr_cm_doenca = 0
    nr_sem_doenca = 0

    for entry in data:

        if (colestrol_no_nivel(entry,min_c,max_c)):

            if (tem_doenca(entry)):

                nr_cm_doenca += 1

            else:

                nr_sem_doenca += 1

    return [nr_cm_doenca,nr_sem_doenca]


#MIN_COLESTEROL: 0
#MAX_COLESTEROL: 603

def distr_por_colesterol(data):

    min_colesterol = 0

    table = []
    rows = []

    while (min_colesterol < 610):

        table.append(distr_nivel_c(min_colesterol,min_colesterol+9,data))

        rows.append(f"[{min_colesterol},{min_colesterol+9}]")

        min_colesterol += 10

    return pd.DataFrame(table,columns=["Com Doença","Sem Doença"],index=rows)

def main():

    data = readData()

    print("\nQUERIES\n")
    print("1: Distribuição da doença por sexo")
    print("2: Distribuição da doença por escalões etários")
    print("3. Distribuição da doença por níveis de colesterol")
    print("0: Sair")

    op = int(input("\nOP: "))
    if (op >= 1 and op <= 3): print("\nRESULT:\n")
    else: return

    if (op == 1):
        
        print(distr_por_sexo(data))

    elif (op == 2):

        print(distr_por_idade(data))

    elif (op == 3):

        print(distr_por_colesterol(data))

    main()


main()