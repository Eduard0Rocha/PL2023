import re
from sys import stdin

def add_coin(coin, carteira):

    if coin in carteira:

        carteira[coin] += 1

    else:

        carteira[coin] = 1

def creditos_to_coins(creditos):

    coins = dict()

    while creditos > 0:

        if creditos >= 500:

            add_coin("500e",coins)
            creditos -= 500

        elif creditos >= 200:

            add_coin("200e",coins)
            creditos -= 200   

        elif creditos >= 100:

            add_coin("100e",coins)
            creditos -= 100

        elif creditos >= 50:

            add_coin("50e",coins)
            creditos -= 50

        elif creditos >= 20:

            add_coin("20e",coins)
            creditos -= 20

        elif creditos >= 10:

            add_coin("10e",coins)
            creditos -= 10

        elif creditos >= 5:

            add_coin("5e",coins)
            creditos -= 5

        elif creditos >= 2:

            add_coin("2e",coins)
            creditos -= 2

        elif creditos >= 1:

            add_coin("1e",coins)
            creditos -= 1

        elif creditos >= 0.5:

            add_coin("50c",coins)
            creditos -= 0.5

        elif creditos >= 0.2:

            add_coin("20c",coins)
            creditos -= 0.2

        elif creditos >= 0.1:

            add_coin("10c",coins)
            creditos -= 0.1

        elif creditos >= 0.05:

            add_coin("5c",coins)
            creditos -= 0.05

        elif creditos >= 0.02:

            add_coin("2c",coins)
            creditos -= 0.02

        elif creditos >= 0.01:

            add_coin("1c",coins)
            creditos -= 0.01

        else:

            break;              

    res = ""

    for key in coins:

        res += f"{coins[key]}x{key}, "

    if (res == ""): return "[Sem troco]"
    else: return res[:-2]

def coin_valida(coin):

    return int(re.search(r"\d+", coin).group()) in [1,2,5,10,20,50,100,200,500]

def print_creditos():

    euros = int(creditos)

    centimos = int((creditos - euros) * 100)

    print(f"saldo = {euros}e{centimos}c")

def coins_to_creditos(coins):

    res = 0.0

    for coin in coins:

        valor = float(re.search(r"\d+", coin).group())

        if not coin_valida(coin):

            print(f"{coin} - moeda inválida; ", end="")
            continue

        if coin[-1] == "c":

            valor /= 100

        res += valor

    return res

creditos = 0.0
levantado = False

for line in stdin:

    print("maq: ", end="")

    line = line[:-1]

    if line == "LEVANTAR":

        levantado = True

        print("Introduza moedas.")

    elif line == "POUSAR":

        if levantado:

            print(f"Troco = {creditos_to_coins(creditos)}; Volte sempre!")
            levantado = False
            break

        else:

            print("Para POUSAR é necessário LEVANTAR...")

    elif re.fullmatch(r"MOEDA [\d+(c|e)(, |.)]+", line):

        if not levantado:

            print("Precisa de LEVANTAR para usar o comando MOEDA")
            continue

        coins = re.findall(r"(\d+[c|e])", line)

        creditos += coins_to_creditos(coins)

        print_creditos()
    
    elif re.fullmatch(r"T=((00\d+)|(\d{9}))", line):

        if not levantado:

            print("Precisa de LEVANTAR para usar o comando T=<número>")
            continue
        
        if re.match(r"T=6(0|4)1", line):

            print("Esse número não é permitido neste telefone. Queira discar novo número!")
            continue
        
        custo = 0.0

        if re.match("T=00", line):

            custo = 1.5

        elif re.match("T=2", line):

            custo = 0.25

        elif re.match("T=808", line):

            custo = 0.1

        if custo > creditos:

            print(f"Insira mais {int((custo - creditos)*100)/100} euros para efetuar essa chamada.")

        else:

            creditos -= custo

        print_creditos()

    elif line == "ABORTAR":

        print(f"Troco = {creditos_to_coins(creditos)}; Abortado!")
        creditos = 0.0

    else:

        print("Comando inválido")

        

