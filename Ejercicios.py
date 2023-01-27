#Ejercicio 1:
"""Escribir una función que determine si una cadena es un 
palíndromo (se lee igual en ambos sentidos) o no:""" 
print("\tEjercicio 1")
#Funcion
def determinar_palindromo(cadena):
    inicio = 0
    final = len(cadena) - 1
    while cadena[inicio] == cadena[final]:
        if inicio >= final:
            return True
        inicio += 1
        final -= 1
    return False
#Datos de entrada
Cadena1 = "RECONOCER"
resultado1 = determinar_palindromo(Cadena1)
Cadena2 = "ALTAMENTE"
resultado2 = determinar_palindromo(Cadena2)
#Datos de salida
print(f"Cadena {Cadena1} es palindromo :",resultado1)
print(f"Cadena {Cadena2} es palindromo :",resultado2)



#Ejercicio 2:      
"""Escribir una función que determine la longitud de la 
subcadena más larga que no contiene ninguna letra repetida.""" 
print("\n\tEjercicio 2")
#Funcion
def longitud_cadena(cadenalarga):
    subcadena = ""
    for i in range (len(cadenalarga)):
        if cadenalarga[i] not in subcadena:
            subcadena+=cadenalarga[i]
    return subcadena
#Datos de entrada
Cadena_Larga = "Escribir una función que determine la longitud"
Subcadena = longitud_cadena(Cadena_Larga)
#Datos de salida
print("Cadena Larga: ", Cadena_Larga)
print("Subcadena: ",Subcadena)
print("La longitud de cadena larga es: ", len(Cadena_Larga))
print("La longitud de la Subcadena es: ",len(Subcadena))



#Ejercicio 3:
"""Escribir una función que divida una cadena dada en una lista
de subcadenas cada vez que aparezca un carácter específico.""" 
print("\n\tEjercicio 3")
#Funcion
def DividirCadena(cadenalarga):
    if len(cadenalarga)>0:
        dato = cadenalarga.split(sep =" ")
    else:
        print()
    return dato    
#Datos de entrada
cadena = "Escribir una función que divida una cadena dada en una lista de subcadenas cada vez que aparezca un carácter específico"
lista = DividirCadena(cadena)
#Datos de salida
print("Este es la cadena larga: \n",cadena)
print("\nLista de una cadena separado por espacio:\n",lista)



#Ejercicio 4:
"""Escribir una función que determine la frecuencia de cada 
carácter en una cadena dada y devuelva un diccionario.""" 
print("\n\tEjercicio 4")
#Funcion
def determinar_frencuencia(cadena):
    subcadena = cadena.split()
    diccionario = {}
    for i in subcadena:
        if i in diccionario:
            diccionario[i] += 1
        else:
            diccionario[i] = 1
    return diccionario
#Datos de salida
CADINA = "Escribir una que determine la de cada carácter  que una la dada dada un diccionario"
RESPUESTA = determinar_frencuencia(CADINA)
#Datos de salida
print("Este es una cadena larga: \n",CADINA)
print("Este es un diccionario hecho aparti de una cadena: \n", RESPUESTA)



#Ejercicio 5:
"""Escribir una función que determine la longitud de la 
subcadena más larga que contiene solo dígitos.""" 
print("\n\tEjercicio 5")
#Funcion 
def determine_longitud(cadenalarga):
    subcadena = ""
    for i in range (len(cadenalarga)):
        try:
            cadenalarga[i] == int(cadenalarga[i])
            subcadena+=cadenalarga[i]
        except:
            continue
    return subcadena
#Datos de entrada
cadena_digitos = "HOLA j12D0 12344 FUNCION TH44IASN 4800SIII21999"
respuestadigitos = determine_longitud(cadena_digitos)
#Datos de salida
print("La cadena es: ",cadena_digitos)
print("La subcadena de digitos es: ",respuestadigitos)
print("La longitud de la subcadena solo digitos es: ",len(respuestadigitos))



#Ejercicio 6:
"""Escribir una función que reemplace todas las apariciones de
una subcadena en una cadena dada con otra subcadena dada."""
print("\n\tEjercicio 6")
#funcion
def Remplazar(cadena1,subcadena,subcadena1):
    if subcadena in cadenaA:
        dato = cadena1.replace(subcadena,subcadena1)
    return dato       
#Datos de entrada
cadenaA = "Escribir una función que reemplace función todas función las función apariciones de"
subcadena0 = "función"
subcadenax = "subcadena"
res = Remplazar(cadenaA,subcadena0,subcadenax)
#Datos de salida
print("La cadena A: ",cadenaA)
print("La subcadena A: ",subcadena0)
print("La subcadena B: ",subcadenax)
print("La cadena reemplazada es es: ",res)
