users = {
    'est': {
        'nome': 'estefania',
        'sobrenome': 'tumena',
    },
    'vini': {
        'nome': 'vinicius',
        'sobrenome': 'silva',
    },
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['nome'] + " " + user_info['sobrenome']

    print("\tNome completo: " + full_name.title())