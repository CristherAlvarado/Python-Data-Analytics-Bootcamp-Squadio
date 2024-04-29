nome =  "CriStHer"

print(nome.upper()) #Maiuscula  
print(nome.lower()) #Minuscula
print(nome.title()) #Titulo (Primeira letra maiuscula)

texto = "                            asdasd cuca "
print(texto)
print(texto.strip() + ".") #remove espaços
print(texto.rstrip() + ".") #Remove espaços da direita
print(texto.lstrip() + ".") #Remove espaços da esquerda

menu = "Python"
print(menu.center(14)) #Centraliza uma String
print(menu.center(14, "#"))
print("-".join(menu)) #Inclui caracteres entre outros caracteres de uma string