#Determinar cuántos intentos son necesarios para encontrar combinaciones numéricas en
#minúscula. El programa fuerza_bruta.py debe intentar todas las combinaciones de letras
#posibles, en orden alfabético, hasta que la combinación de letras sea igual a la de la
#contraseña indicada. Deberá hacer este proceso letra por letra, de izquierda a derecha.


#Librerias
from getpass import getpass
from string import ascii_lowercase

#Definimos variables
intento = 0 # Para el conteo de intentos
posicion_contrasena = 0 # Definimos esta variable para definir la posicion de la contraseña en 0 al acceder a ella en cada ciclo
contrasena_hack = {} #definimos esta variable para almacenar en un diccionario las letras que va encontrando en el ciclo y luego compararlas con el password inicial.
password_list = {} #Definimos esta variable para convertir el password original de string a diccionario y poder compararlo en el que generamos al ejecutar el ciclo.
password_valido = False #Definimos esta variable como false para poder comprobar que lo que se ingrese de contraseña se contenga en la lista de letras, y no sea ni una ñ o un numero.

#ciclo para comprobar que el contenido de la contraseña sea valido antes de realizar el hackeo
while password_valido != True:
    password = getpass("Ingresa tu contraseña:").lower() #solicitamos contraseña
    password_valido = True #se define como True
    for position, elemento in enumerate(password): #Generamos este ciclo para solicitar una nueva contraseña en caso de que los caracteres no coincidan con los exigidos.
        if password[position] not in ascii_lowercase:
            print("Contraseña erronea. Intenta nuevamente")
            password_valido = False #definimos como false para que solicite la contraseña nuevamente

#ciclo para crear un diccionario con cada elemento del password para compararlo posteriormente
for position, elemento in enumerate(password):
    password_list[position] = password[position] #ingresa a cada indice del password ingresado y lo ingresa en la misma posicion en cada ciclo

#ciclo para realizar el hackeo
while contrasena_hack != password_list: #esto se ejecuta mientras la contraseña hackeada no coincida en su totalidad con la contraseña ingresada inicialmente
    for position, elemento in enumerate(ascii_lowercase):
        intento = intento + 1 #sumamos cada intento a medida que se ejecute el ciclo
        if elemento == password[posicion_contrasena]:
            contrasena_hack[posicion_contrasena] = elemento #decimos que ingrese en la posicion indicada en la contraseña hackeada el valor definido en cada ciclo en elemento
            posicion_contrasena = posicion_contrasena + 1 #avanzamos de posicion
            break

    
    
print(f"su contraseña es {contrasena_hack} y se encontro en {intento} de intentos")