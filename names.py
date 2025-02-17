from name_function import get_formatted_name

print("Digite 'e' a qualquer momento para encerrar.")
while True:
    first = input("\nPor favor informe seu primeiro: ")
    if first == 'e':
        print("Programa encerrado.")
        break
    last = input("Por favor informe seu sobrenome: ")
    if last == 'e':
        print("Programa encerrado.")
        break

    formatted_name = get_formatted_name(first, last)
    print("\tSeu nome formatado: " + formatted_name + '.')