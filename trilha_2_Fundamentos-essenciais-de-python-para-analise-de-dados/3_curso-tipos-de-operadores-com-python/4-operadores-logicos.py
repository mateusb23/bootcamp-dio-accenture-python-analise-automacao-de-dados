## OPERADORES LÓGICOS
# Operadores lógicos são usados para combinar expressões booleanas e retornar um resultado booleano. Eles incluem:
# - AND (and) --> Retorna True se ambas as expressões forem verdadeiras
# - OR (or) --> Retorna True se pelo menos uma das expressões for verdadeira
# - NOT (not) --> Retorna o oposto do valor booleano da expressão
# Exemplo de uso dos operadores lógicos
a = True
b = False
print("a AND b:", a and b)  # False
print("a OR b:", a or b)    # True
print("NOT a:", not a)      # False
print("NOT b:", not b)      # True
# Combinação de operadores lógicos
x = 5
y = 10
print("x é maior que 3 AND y é menor que 15:", (x > 3) and (y < 15))  # True
print("x é menor que 3 OR y é menor que 15:", (x < 3) or (y < 15))    # True
print("NOT (x é maior que 3 AND y é menor que 15):", not ((x > 3) and (y < 15)))  # False

# Operadores lógicos também podem ser usados para encadear expressões booleanas
print("x é maior que 3 AND y é menor que 15 OR x é igual a 5:", (x > 3) and (y < 15) or (x == 5))  # True
print("x é menor que 3 OR y é menor que 15 AND x é igual a 5:", (x < 3) or (y < 15) and (x == 5))    # True
print("NOT (x é maior que 3 AND y é menor que 15) OR x é igual a 5:", not ((x > 3) and (y < 15)) or (x == 5))  # True

