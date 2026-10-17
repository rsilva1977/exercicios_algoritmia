# Pede ao utilizador uma string e guarda o texto introduzido na variável `texto`.
texto = input("Introduza uma string: ")
# Define as vogais que serão contadas, incluindo versões acentuadas em português.
vogais = "aeiouáàâãéêíóôõú"
# Converte o texto para minúsculas e soma 1 por cada caractere que seja uma vogal.
quantidade = sum(1 for caractere in texto.lower() if caractere in vogais)

# Apresenta ao utilizador o total de vogais encontrado na string.
print(f"Quantidade de vogais: {quantidade}")

