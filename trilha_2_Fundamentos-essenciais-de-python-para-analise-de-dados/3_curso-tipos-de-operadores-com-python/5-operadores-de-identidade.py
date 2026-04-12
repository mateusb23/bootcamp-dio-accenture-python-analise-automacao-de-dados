## OPERADORES DE IDENTIDADE
# Operadores de identidade são usados para comparar a identidade de objetos, ou seja, se eles são o mesmo objeto na memória. Eles incluem:
# - is --> Retorna True se ambos os operandos referirem-se ao mesmo objeto
# - is not --> Retorna True se ambos os operandos não referirem-se ao mesmo objeto
# Exemplo de uso dos operadores de identidade
a = [1, 2, 3]
b = a  # b é uma referência ao mesmo objeto que a
c = [1, 2, 3]  # c é um novo objeto com o mesmo conteúdo de a
print("a is b:", a is b)  # True, pois a e b referem-se ao mesmo objeto
print("a is c:", a is c)  # False, pois a e c são objetos diferentes na memória
print("a is not c:", a is not c)  # True, pois a e c são objetos diferentes na memória
# Operadores de identidade também podem ser usados para comparar objetos imutáveis, como strings e números
x = 10
y = 10
print("x is y:", x is y)  # True, pois pequenos inteiros são internados pelo Python e referenciam o mesmo objeto
s1 = "Hello"
s2 = "Hello"
print("s1 is s2:", s1 is s2)  # True, pois strings literais são internadas pelo Python e referenciam o mesmo objeto
s3 = "Hello World"
print("s1 is s3:", s1 is s3)  # False, pois s1 e s3 são objetos diferentes na memória, mesmo que tenham o mesmo conteúdo
