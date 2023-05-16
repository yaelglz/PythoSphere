nombre_completo = input('Ingresa tu nombre completo: ') # String (str)
print('Hola ' + nombre_completo + '!')
print(type(nombre_completo))

edad = int(input('Ingresa tu edad: ')) # Integer (int)
print('Tu edad es: ' + str(edad)) # Convertir a string
print(type(edad))

estatura = float(input('Ingresa tu estatura: ')) # Float (float)
print('Tu estatura es: ' + str(estatura)) # Convertir a string
print(type(estatura))

autorizacion = input('¿Estás autorizado? (si/no): ') == 'si' # Boolean (bool)
print ('Autorización: ' + str(autorizacion)) # Convertir a string
print(type(autorizacion))