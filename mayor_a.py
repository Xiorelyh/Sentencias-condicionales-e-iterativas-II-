#Se solicita devolver un informe resumido que exponga los meses que superan un cierto
#umbral. El programa mayor_a.py debe retornar un diccionario con el mes y el valor
#asociado siempre y cuando superen el umbral especificado.


# Importacion Sys
import sys

# Diccionario Ventas
ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}

# Verificar que se proporcione un argumento para el umbral
if len(sys.argv) != 2:
    print("Uso: python mayor_a.py <umbral>")
    sys.exit(1)

# Ingrese valor a filtrar
try:
    valor = float(sys.argv[1])
except ValueError:
    print("Por favor, ingrese un número válido para el umbral.")
    sys.exit(1)

# Resultado del filtrado
resultado = dict()

# Filtrado por formula
for mes, value in ventas.items():
    if value >= valor:
        resultado[mes] = value

print(resultado)