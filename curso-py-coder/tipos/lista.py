numeros = [1, 2, 3]
print(type(numeros))

# adiciona ítens na lista
numeros.append(300)
numeros.append(400)
numeros.append(500)

# imprime o tamanho da lista
print(len(numeros))
# substitui um ítem da lista
numeros[3] = 100
numeros.insert(0, -200)

# imprime o 6° ítem da lista
print(numeros[6])
# imprime o 1° ítem da lista de trás para frente 
print(numeros[-1])
# imprime o 2° ítem da lista de trás para frente
print(numeros[-2])
# imprime a lista toda
print(numeros)
