from datetime import datetime
import numpy as np
import json

def parseNomesERelacoes(dados):

    dados = list(filter(lambda x: len(x) > 0 ,dados.split("::")))

    nomes = list()
    apelidos = list()
    relacoes = list()

    for entry in dados:

        entry = str(entry).split(".")

        for info in entry:

            while len(info) > 0 and info[0] == " ":
                info = info[1:]

            if (info == ""): continue
            if (info.isnumeric()): continue
            if (info == "Proc"): continue
            if (info.startswith("Em Anexo:")): continue
            if (info == "Doc"): continue
            if (info == "danificado"): continue
            if (any(char.isdigit() for char in info)): continue

            nome_e_relacao = info.split(",",2)

            if len(nome_e_relacao) > 1:

                if (not nome_e_relacao[1].startswith(" ")):

                    relacoes.append(nome_e_relacao[1])

            else:

                tds_os_nomes = nome_e_relacao[0].split(" ")

                nomes.append(tds_os_nomes[0])
                apelidos.append(tds_os_nomes[len(tds_os_nomes)-1])

    return nomes,apelidos,relacoes

def parseLine(line):

    dados = line.split("::",2)

    dados[0] = int(dados[0])
    dados[1] = datetime.strptime(dados[1], '%Y-%m-%d')

    dados[2],apelidos,relacoes = parseNomesERelacoes(dados[2])

    return [dados[0],dados[1],dados[2],apelidos,relacoes]

def readData():

    res = list()

    with open("processos.txt") as f:

        for line in f:

            line = line[:-1]

            if line != "":

                res.append(parseLine(line))

    return res

def dict_to_csv(dic):

    res = ""
    
    for key in dic.keys():

        res += f"{key};{dic[key]}\n"

    return res

def print_output_in_file(file_path,output):

    f = open(file_path, "w")
    f.write(output)
    f.close()

def processos_por_ano(data):

    res = dict()

    for entry in data:

        key = entry[1].year

        if key in res:

            res[key] += 1

        else:

            res[key] = 1

    keys = list(res.keys())

    keys.sort()

    return {key: res[key] for key in keys}

def nomes_proprios_mais_usados(data):

    res = dict()

    for entry in data:

        for nome in entry[2]:

            if nome in res:

                res[nome] += 1

            else:

                res[nome] = 1

    keys = list(res.keys())
    values = list(res.values())
    sorted_value_index = np.argsort(values)
    
    sorted_dict = {keys[i]: values[i] for i in sorted_value_index}

    new_keys = list(sorted_dict.keys())

    new_keys = new_keys[::-1]

    return new_keys[:5]

def apelidos_mais_usados(data):

    res = dict()

    for entry in data:

        for nome in entry[3]:

            if nome in res:

                res[nome] += 1

            else:

                res[nome] = 1

    keys = list(res.keys())
    values = list(res.values())
    sorted_value_index = np.argsort(values)
    
    sorted_dict = {keys[i]: values[i] for i in sorted_value_index}

    new_keys = list(sorted_dict.keys())

    new_keys = new_keys[::-1]
    
    return new_keys[:5]

def frequencia_de_relacoes(data):

    res = dict()

    for entry in data:

        for nome in entry[4]:

            if nome in res:

                res[nome] += 1

            else:

                res[nome] = 1

    keys = list(res.keys())
    values = list(res.values())
    sorted_value_index = np.argsort(values)
    
    sorted_dict = {keys[i]: values[i] for i in sorted_value_index}

    new_keys = list(sorted_dict.keys())

    new_keys = new_keys[::-1]

    return {key:sorted_dict[key] for key in new_keys}

def convert_data_to_json(number_of_lines):

    data = dict()

    data["processos"] = list()

    with open("processos.txt") as f:

        for i in range(0,number_of_lines-1):

            info = f.readline()[:-3].split("::",5)

            entry = dict()

            entry["Pasta"] = info[0]
            entry["Data"] = info[1]
            entry["Nome"] = info[2]
            entry["Pai"] = info[3]
            entry["Mae"] = info[4]
            entry["Observacoes"] = info[5]

            data["processos"].append(entry)

    return json.dumps(data)

def main():

    data = readData()

    print_output_in_file("output1.csv",dict_to_csv(processos_por_ano(data)))
    print_output_in_file("output2.txt",str(nomes_proprios_mais_usados(data)))
    print_output_in_file("output3.txt",str(apelidos_mais_usados(data)))
    print_output_in_file("output4.csv",dict_to_csv(frequencia_de_relacoes(data)))
    print_output_in_file("output5.json",convert_data_to_json(20))

main()