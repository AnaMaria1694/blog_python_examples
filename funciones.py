def saludar(nombre):
    mensaje = "¡Hola, " + nombre + "! ¡Bienvenido!"
    return mensaje


def mostrar_informacion(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")


def sumar(a, b):
    return a + b

def mostrar_informacion1(nombre, edad):
    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")


def sumar(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    return resultado


nombre_del_usuario = "Carlos"
resultado = saludar(nombre_del_usuario)
print(resultado)

total = sumar(1, 2, 3, 4, 5)
print(total)  # Esto imprimirá 15, que es la suma de los números pasados.

mostrar_informacion(nombre="Juan", edad=30, ciudad="Ejemploville")

numeros = (2, 3)  # Creamos una tupla con dos números.
resultado = sumar(*numeros)  # Desempaquetamos la tupla y llamamos a la función sumar.
print(resultado)  # Esto imprimirá 5, que es la suma de 2 y 3.

datos = {"nombre": "Juan", "edad": 30}  # Creamos un diccionario con datos.
mostrar_informacion1(**datos)  # Desempaquetamos el diccionario y llamamos a la función mostrar_informacion.