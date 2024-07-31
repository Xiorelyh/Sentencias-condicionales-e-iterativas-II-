#Se requiere la construcción de una aplicación interactiva primeros_auxilios.py que
#entregue los distintos pasos a seguir dependiendo de las respuestas que el usuario entrega
#en tiempo real.



#Definicion de funciones

def evaluar_respuesta():
    respuesta = input("¿Responde a Estímulos? [Y/N] : \n")
    if respuesta.lower() == "y":
        valorar_necesidad_hospital()
    else:
        abrir_via_aerea()

def valorar_necesidad_hospital():
    necesidad_hospital = print("Valorar la necesidad de llevar al hospital más cercano \n")

def abrir_via_aerea():
    print("Abrir la vía aérea.")
    evaluar_respiracion()

def evaluar_respiracion():
    respira = input("¿Respira? [Y/N] : \n")
    if respira.lower() == "y":
        print("Permitir posición de suficiente ventilación.")
    else:
        administrar_ventilaciones()

def evaluar_signos_vida():
    signos_vida = input("¿Signos de Vida? [Y/N] : \n")
    if signos_vida.lower() == "y":
        print("Esperar a la ambulancia y reevaluar.")     
    else:
        administrar_compresiones_toracicas()
        
def evaluar_ambulancia():
    ambulancia = input("¿Llegó la ambulancia? [Y/N] : \n")
    if ambulancia.lower() == "y":
        print("Paciente camino a urgencias en la ambulancia.")
    else:
        evaluar_signos_vida()

def administrar_ventilaciones():
    print("Administrar 5 ventilaciones y llamar a la ambulancia.")
    evaluar_signos_vida()

def administrar_compresiones_toracicas():
    print("Administrar compresiones torácicas hasta que llegue la ambulancia.")
    evaluar_ambulancia()
    
