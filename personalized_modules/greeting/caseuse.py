# Importar el módulo personalizado
import greeting

# Utilizar la función y la variable del módulo
salutation = greeting.greeting("Juan",'es')
print(salutation)
salutation = greeting.greeting("Jhon",'en')
print(salutation)
salutation = greeting.greeting("John",'it')
print(salutation)
salutation = greeting.greeting("John",'jp')
print(salutation)
print(greeting.welcomeMessage)