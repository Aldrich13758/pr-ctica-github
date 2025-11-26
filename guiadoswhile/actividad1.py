import random
num_secreto=random.randint(1,20)
numero=int(input("introduce un numero del 1 al 20: "))
while num_secreto!=numero and (numero>0 and numero<20):
    print (f"el Numero que has introducido {numero}, no has acertado")
    numero=int(input("introduce otro numero: "))
print("acertaste")