from survey import AnonymousSurvey

# Define uma pergunta e cria uma pesquisa
question = "Qual foi a primeira língua que você aprendeu a falar?"
my_survey = AnonymousSurvey(question)

# Mostra a pergunta e armazena as respostas à pergunta
my_survey.show_question()
print("Pressione 'p' a qualquer momento para sair.\n")
while True:
    response = input("Língua: ")
    if response == 'p':
        break
    my_survey.store_response(response)

# Exibe os resultados da pesquisa
print("\nObrigado a todos por participarem da pesquisa!")
my_survey.show_results()