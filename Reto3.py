#Camilo y un nuevo juego
#Autor: Natalia Giraldo
#Fecha creación: 24/06/2021
#Ultima fecha de modificación: 26/06/2021

lista = input().split(" ")

#Definición de variables

pr = lista[0] #se inicializa con el primer elemento
c1 = 0 #Contador anterior
letras = "" #Lista de caracteres
cantidad_letras = "" #Lista de contadores
contador = 0

#Iteración

for i in lista:
    if i  == pr:
        c1 += 1
    else:
        letras += pr + " "
        cantidad_letras += str(c1) + " "
        pr = i #anterior es igual a la letra
        c1 = 1 #cantidad anterior se reinicia con valor 1
    if contador ==len(lista)-1: #pregunta si llego al final
        letras += pr + " "
        cantidad_letras += str(c1) + " "
    contador += 1

#Pruebas
print(letras)
print(cantidad_letras)










    
        
    
