#Strings

my_string = "Mi String"
my_other_string = 'Mi String'

print(len(my_string))

print(len(my_other_string))

print (my_string, my_other_string)

my_new_line_string = "Este es un nuevo String "

#Formateo de Strings
print("--------------------------Formateo Edad------------------------------------")
name ,surname, edad = "Andres" , "alfonso", 34
print("Mi nombre es: {} {} y mi edad es {}".format(name,surname,edad))
print("Mi nombre es: %s %s y mi edad es %d" %(name,surname,edad))
print("Mejor opción-")
print(f"Mi nombre es: {name} {surname} y mi edad es: {edad}")

#Desempaquetado de variables
print("--------------------------Desempaquetado variables------------------------------------")
lenguaje = "pyhton"
a,b,c,d,e,f = lenguaje
print(a)
print(b)

#Division
print("--------------------------Division------------------------------------")
lenguaje_slice =lenguaje[1:3]
print(lenguaje_slice)
lenguaje_slice =lenguaje[1:]
print(lenguaje_slice)

#reverse
print("--------------------------Reverse------------------------------------")
reversed_lenguaje =lenguaje[::-1]
print(reversed_lenguaje)

#Funciones del sistema
print("--------------------------Funciones del sistema------------------------------------")
print(lenguaje.capitalize())
print(lenguaje.upper())
print(lenguaje.count("t"))
print(lenguaje.isnumeric())
print(lenguaje.lower())
print(lenguaje.upper().isupper())
print(lenguaje.startswith("py"))