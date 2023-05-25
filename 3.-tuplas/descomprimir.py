numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)  # Tupla de 6 valores
# Descomprimimos la tupla en 6 variables
# y el resto en una lista llamada resto_valores
uno, _, tres, cuatro, *_, nueve, diez = numeros

# * -> Se crea una lista con el resto de valores
# _ -> Se ignora el valor

print(uno)
# print(dos)
print(tres)
print(cuatro)
# print(resto_valores) # Imprimimos la lista con el resto de valores
print(nueve)
print(diez)
