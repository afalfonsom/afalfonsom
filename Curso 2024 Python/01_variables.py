# Variables
#variable cadena de caracteres.
my_variable = "My Srting Variable"
print (my_variable)
#Variable entero
my_int_variable =5
print(my_int_variable)
#Variable Booleana
my_bool_variable = True
print(my_bool_variable)

#Conversión de  un entero a un string
my_str_variable = str(my_int_variable)
print(my_str_variable)
print(type((my_str_variable)))

#Concatenación de palabras en un print
print(my_variable,str(my_int_variable), my_bool_variable)
print("Estes es el valor de:",my_bool_variable)

#Algunas funciones del sistema
print(len(my_variable))

#Declaración de multiples variables !No es recomendable por mantenimiento de codigo!
name,surname, alias, age = "Andres", "Alfonso", "Pipe", 34
print("Me llamo", name,surname,". My edad es:",age,"Y mi alias es:",alias)

#Forzar tipo
addres: str ="Mi dirección"
addres = 32
print(addres)