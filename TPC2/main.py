
def on_sequence(command):

    return command[:2] == "ON"

def off_sequence(command):

    return command[:3] == "OFF"

# Return (number, number of digits)
def pop_number(command):

    if (not command[0].isdigit()): return None

    seq = ""

    index = 0

    while (index < len(command) and command[index].isdigit()):

        seq += command[index]

        index += 1

    return (int(seq),index)

def main():

    command = input("Informe o texto: ")

    command = command.upper()

    is_on = True

    res = 0

    while (len(command) > 0):

        if (on_sequence(command)):

            is_on = True
            command = command[2:]

        elif (off_sequence(command)):

            is_on = False
            command = command[3:]

        elif (command[0] == "="):

            print(res)
            command = command[1:]

        elif (command[0].isdigit() and is_on):

            number,len_dig = pop_number(command)

            command = command[len_dig:]

            res += number

        else: command = command[1:]

    print(f"O resultado é: {res}!")

main()