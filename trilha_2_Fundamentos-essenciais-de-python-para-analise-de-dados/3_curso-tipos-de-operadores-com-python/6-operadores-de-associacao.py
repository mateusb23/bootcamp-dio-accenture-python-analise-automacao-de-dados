# OPERADORES DE ASSOCIAÇÃO

# Operadores de associação são usados para verificar se um valor está presente em uma sequência (como listas, tuplas, strings) ou em um dicionário. Eles incluem:
# - in --> Retorna True se o valor estiver presente na sequência ou dicionário
# - not in --> Retorna True se o valor não estiver presente na sequência ou dicionário

# Exemplo de uso dos operadores de associação
# Usando in com listas
frutas = ["maçã", "banana", "laranja"]
print("banana in frutas:", "banana" in frutas)  # True
print("uva in frutas:", "uva" in frutas)        # False

# Usando not in com listas
print("uva not in frutas:", "uva" not in frutas)  # True

# Usando in com strings
texto = "Olá, mundo!"
print("mundo in texto:", "mundo" in texto)  # True
print("Python in texto:", "Python" in texto)  # False

# Usando not in com strings
print("Python not in texto:", "Python" not in texto)  # True

# Usando in com dicionários (verifica as chaves)
pessoa = {"nome": "Alice", "idade": 30, "cidade": "São Paulo"}
print("nome in pessoa:", "nome" in pessoa)  # True
print("sobrenome in pessoa:", "sobrenome" in pessoa)  # False

# Usando not in com dicionários
print("sobrenome not in pessoa:", "sobrenome" not in pessoa)  # True
# Operadores de associação também podem ser usados para verificar a presença de valores em conjuntos (sets)
numeros = {1, 2, 3, 4, 5}
print("3 in numeros:", 3 in numeros)  # True
print("6 in numeros:", 6 in numeros)  # False
print("6 not in numeros:", 6 not in numeros)  # True

# Operadores de associação também podem ser usados para verificar a presença de caracteres em strings
palavra = "Python"
print("P in palavra:", "P" in palavra)  # True
print("y in palavra:", "y" in palavra)  # True
print("z in palavra:", "z" in palavra)  # False
print("z not in palavra:", "z" not in palavra)  # True

# Operadores de associação também podem ser usados para verificar a presença de elementos em tuplas
cores = ("vermelho", "verde", "azul")
print("verde in cores:", "verde" in cores)  # True
print("amarelo in cores:", "amarelo" in cores)  # False
print("amarelo not in cores:", "amarelo" not in cores)  # True

# Operadores de associação também podem ser usados para verificar a presença de chaves em dicionários
carro = {"marca": "Toyota", "modelo": "Corolla", "ano": 2020}
print("marca in carro:", "marca" in carro)  # True
print("cor in carro:", "cor" in carro)      # False
print("cor not in carro:", "cor" not in carro)  # True  

# Operadores de associação também podem ser usados para verificar a presença de valores em dicionários usando o método values()
print("Toyota in carro.values():", "Toyota" in carro.values())  # True
print("Honda in carro.values():", "Honda" in carro.values())    # False 
print("Honda not in carro.values():", "Honda" not in carro.values())  # True

