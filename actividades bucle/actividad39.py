#39. Programa que pida n números y que, tras introducir el último número, debe aparecer por pantalla el número total de positivos, negativos y número de 0
número=int(input("¿Cuántos números quieres introducir? ")) 
positivos=negativos=ceros=0 
for i in range(número): 
    num=int(input("Introduce un número: ")) 
    if num > 0: 
        positivos+=1 
    elif num<0: 
        negativos+=1 
    else: 
        ceros+=1 
print("Positivos:", positivos)
print("Negativos:", negativos)
print("Ceros:", ceros)