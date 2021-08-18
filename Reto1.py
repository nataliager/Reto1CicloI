
#Nombre: Natalia Andrea Giraldo Erazo
#Correo: nathalia2001ge09@gmail.com

h1 = int(input("Ingrese la primera altura: "))
h2 = h1 + h1 + 4
h3 = (h1 + h2)  //  5
print(h1, h2, h3)

def zona(h3):
    zona = ""
    #Condicionales
    if h3 >= 0 and h3 <= 20:
        zona = "uno"
    elif h3 >= 21 and h3 <= 30:
        zona = "dos"
    elif h3 >= 31 and h3 <= 50:
        zona = "tres"
    else: 
        zona = "cuatro"   
    return zona

print(zona(h3))
    


