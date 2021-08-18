#Camilo y su nueva maquina
#Author: Natalia Giraldo
#creation date: 30/06/2021
#Last modification date: 01/07/2021

import json #Library for json use

available_products = input() #json input
convert = json.loads(available_products) #convert json to python
products_users = input().split(" ") #separator for " "
price = 0 #starting price
available = "" #list of available products

#Iterator
for i in products_users:
    if i in convert:
        price += convert[i]
        available += i + " "
        #print(f"{i} available")
    else:
        #print(f"{i} No available")
        pass

#Outputs
print(price)
print(available)