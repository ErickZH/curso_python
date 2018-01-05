# Dado de los valores ingresados por el usuario (base, altura) 
#calcular y mostrar en pantalla el área de un triángulo.

# Pedimos base
print('Ingresa la base del triángulo')
base = float(input());

#Pedimos la altura
print('Ingresa la altura del triángulo')
altura = float(input())

# Sabemos que
# area = base x altura / 2
area = (base * altura) / 2

#mostramos resultado en pantalla
# Ejemplo
# base = 5
# altura = 5
# area = 12.5

print("Área:",area)