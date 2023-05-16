lista = [8, 90, 1, 5, 44, 132, 600, 3, 4]

lista.sort() # sort() ordena los elementos de la lista de menor a mayor
print(lista)

lista.sort(reverse=True) # sort(reverse=True) ordena los elementos de la lista de mayor a menor
print(lista)

# min - max
print(min(lista)) # min() devuelve el elemento de menor valor de la lista
print(max(lista)) # max() devuelve el elemento de mayor valor de la lista

# in
print(5 in lista) # in devuelve True si el elemento indicado está en la lista, de lo contrario devuelve False

print(11 not in lista) # not in devuelve True si el elemento indicado no está en la lista, de lo contrario devuelve False

# index
print(lista.index(44)) # index() devuelve el índice del elemento indicado de la lista