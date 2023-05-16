lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java', 'Rust']
lista_cursos_2 = ['C', 'C++', 'Docker']

print(len(lista_cursos)) # len() devuelve la cantidad de elementos de la lista

lista_cursos.append('MongoDB') # append() agrega un elemento al final de la lista
lista_cursos.append('C#')
lista_cursos.append('JavaScript')

lista_cursos.insert(1, 'Rails') # insert() agrega un elemento en la posición indicada de la lista (posición, elemento) 
lista_cursos.insert(0, 'PyGame')

lista_cursos.extend(lista_cursos_2) # extend() agrega los elementos de una lista a otra lista al final

print(lista_cursos)
print(len(lista_cursos))

lista_cursos.remove('MongoDB') # remove() elimina el elemento indicado de la lista
print(lista_cursos)

del lista_cursos[0] # del elimina el elemento de la posición indicada de la lista
print(lista_cursos)

lista_cursos.pop() # pop() elimina el último elemento de la lista
print(lista_cursos)

lista_cursos.pop(0) # pop() elimina el elemento de la posición indicada de la lista
print(lista_cursos)

lista_cursos.clear() # clear() elimina todos los elementos de la lista
print(lista_cursos)
print(len(lista_cursos))