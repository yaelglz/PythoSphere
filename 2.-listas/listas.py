lista_cursos = ['Python', 'Django', 'C#', 'Java', 'PHP', 'Ruby']

# print(lista_cursos[0])
primer_curso = lista_cursos[0] # Acceder a un elemento de la lista
print(primer_curso)

segundo_curso = lista_cursos[1]
print(segundo_curso)

ultimo_curso = lista_cursos[-1]
print(ultimo_curso)

lista_cursos[2] = 'Rust' # Modificar un elemento de la lista
print(lista_cursos)

# [start:end]
# [start] -> Obtiene los elementos desde el indice start hasta el final
# [end] -> Obtiene los primeros elementos de una lista hasta el indice end
# [start:end:skip] -> Obtiene los elementos desde el indice start hasta el indice end, saltando de skip en skip

sub_lista = lista_cursos[0:3] # Sublista se crea desde el indice 0 hasta el 2
print(sub_lista)

sub_lista = lista_cursos[1:4] # Sublista se crea desde el indice 1 hasta el 3
print(sub_lista)

sub_lista = lista_cursos[1:] # Sublista se crea desde el indice 0 hasta el final
print(sub_lista)

sub_lista = lista_cursos[:4] # Sublista se crea desde el indice 0 hasta el 3
print(sub_lista)

sub_lista = lista_cursos[1:5:2] # Sublista se crea desde el indice 1 hasta el 4, saltando de 2 en 2
print(sub_lista)