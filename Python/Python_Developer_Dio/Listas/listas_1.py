frutas = ["Laranja", "maca", "uva"]
print(frutas)


letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 420000, 2020, 2900, "São Paulo", True]
print(carro)

# Acesso direto ao elemento
print(frutas[0])

# Indice negativo
frutas = ["Laranja", "maca", "uva"]
print(frutas[-1])  # UVA
print(frutas[-3])  # Laranja

# Listas Aninhadas
matriz = [[1, "a", 2], ["b", 3, 4], [6, 5, "c"]]

print(matriz[0])  # [1,"a",2]
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"

# Fatiamento
lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])
print(lista[:2])
print(lista[1:3])
print(lista[0:3:2])
print(lista[::])
print(lista[::-1])

# Iterar lista

carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

# Função enumerete

carros = ["gol", "celta", "palio"]
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# Compreensão de lista
# Filtro 1
numero = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
]
pares = []

for num in numero:
    if num % 2 == 0:
        pares.append(num)

print(pares)

# Filtro 2
numero = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
]
pares = [num for num in numero if num % 2 == 0]

print(pares)

# Modificando valores versão 1

numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrado = []


for num in numeros:
    quadrado.append(num**2)
print(quadrado)

# Modificando valores versão 2
numero = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrado = [num**2 for num in numeros]

print(quadrado)

# Metodos da classe list
# [].append
lista = []
lista.append(1)
lista.append("python")
lista.append([40, 30, 20])

print(lista)
