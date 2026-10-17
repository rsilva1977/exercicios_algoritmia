# Define as vogais que serão contadas, incluindo versões acentuadas em português.
vogais = "aeiouáàâãéêíóôõú"

# Repete a leitura e a contagem até o utilizador escolher terminar.
while True:
	# Pede uma string ou a palavra "sair" para terminar o programa.
	texto = input("Introduza uma string (ou 'sair' para terminar): ")

	# Ignora espaços exteriores e maiúsculas ao verificar a palavra de término.
	if texto.strip().lower() == "sair":
		# Interrompe o ciclo e termina o programa.
		break

	# Converte o texto para minúsculas e soma 1 por cada caractere que seja uma vogal.
	quantidade = sum(1 for caractere in texto.lower() if caractere in vogais)

	# Apresenta o total de vogais encontrado nesta string.
	print(f"Quantidade de vogais: {quantidade}")

