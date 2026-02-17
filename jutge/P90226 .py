a, b = input("introduce dos palabras separadas por un espacio: ").split() 
if a < b: 
    print(f"{a} < {b}") 
elif a > b: 
    print(f"{a} > {b}") 
else: 
    print(f"{a} = {b}")