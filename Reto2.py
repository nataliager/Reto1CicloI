#Cadenas de caracteres que ingresan los dos jugadores
juan = input("Digite la cadena del jugador1 = Juan: ")
camilo = input("Digite la cadena del jugador2 = Camilo: ")
caracteres = input("Ingrese la cadena de caracteres y simbolos: ")

#Función qu se encarga de buscar el ganador del juego o si hay empate
def resultado(juan,camilo,caracteres):

    if len(juan) == len(camilo):
        cadena = ""
        c1 = 0 #contador de juan
        c2 = 0 #contador de camilo
        for i in caracteres:
            if i in juan:
                c1 += 1
            if i in camilo:
                c2 += 1
            if c1 == c2:
                cadena += "T"
            elif c1 > c2:
                cadena += "J"
            elif c2 > c1:
                cadena += "C"
    else:
        ("Las cadenas no tienen el mismo tamaño...")

    return cadena

#Llamado de la función con los parametros que ingresaron los dos jugadores
print(resultado(juan,camilo,caracteres))

