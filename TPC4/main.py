import re
import json

path = input("INPUT FILE PATH: ")

f = open(path, "r")

fields = re.sub(r"{(\d+),(\d+)}",r"{\1;\2}",f.readline()[:-1]).split(",")

data = []

for x in f:

    if x[-1] == '\n':

        x = x[:-1]

    values = x.split(",")

    elem = dict()
    index = 0

    for field in fields:

        if field == '': continue

        number_of_elems = re.search(r"{(\d+)}",field)
        number_of_elems = int(number_of_elems.group()[1:][:-1]) if number_of_elems != None else 0

        if number_of_elems == 0:

            number_of_elems = re.search(r"{(\d+);(\d+)}", field)
            number_of_elems = int(number_of_elems.group().split(";")[1][:-1]) if number_of_elems != None else 0

        # se number_of_elems = 0 não é um array
        # se for um intervalo, considera o maximo
        # em ambos os casos, está projetado para falta de info

        function_name = None

        if re.search(r"::sum",field):

            function_name = "sum"

        elif re.search(r"::media",field):

            function_name = "media"

        if number_of_elems == 0: # implica que function_name == None

            elem[field] = values[index]
            index += 1

        else:

            array = []

            for i in range(0,number_of_elems):

                value = values[index]

                index += 1

                if (value != ''):

                    array.append(int(value))
            
            if function_name == None:

                elem[field] = array

            else:

                field_name = field.split("{")[0] + "_" + function_name

                _sum = 0

                for array_value in array:

                    _sum += array_value

                if function_name == "sum":

                    elem[field_name] = _sum
                
                elif function_name == "media":

                    elem[field_name] = _sum / len(array)


    data.append(elem)    

f.close()

json_string = json.dumps(data, ensure_ascii=False, indent=2)

f = open("output.json", "w", encoding="utf8")

f.write(json_string)

f.close()