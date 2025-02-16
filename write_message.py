nome_arquivo = input("Digite o nome do arquivo: ")

while nome_arquivo == '':
    nome_arquivo = input("Nome do arquivo não pode ficar em branco: ")

filename = nome_arquivo + '.txt'

try:
    with open(filename, 'r') as file_object:
        file_object.read()
        if file_object != '':
            print("Arquivo já existe e não está vazio!")
except FileNotFoundError:
    pass

    with open(filename, 'a') as file_object:
        texto = input("Digite alguma coisa: ")
        file_object.write(texto+"\n")

with open(filename, 'r') as file_object:
    print("O conteúdo do arquivo é:\n" + file_object.read())