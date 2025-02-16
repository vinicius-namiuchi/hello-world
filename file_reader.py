filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

    pi_string = ''
    for line in lines:
        pi_string += line.rstrip()
    
    birthday = input("Digite seu aniversário, no formato (ddmmaa): ")
    if birthday in pi_string:
        print("Seu aniversário aparece nos primeiros milhões de digitos do pi!")
    else:
        print("Seu aniversário não aparece nos primeiros milhões de digitos do pi.")