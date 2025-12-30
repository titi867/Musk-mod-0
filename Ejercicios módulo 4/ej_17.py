def prod(l1, l2):
    
    try:
        for i in range(len(l1)):
            yield l1[i] * l2[i]
    except StopIteration:
        pass
    
    
l1 = [1, 2, 3, 4]
l2 = [10, 20, 30, 40]

resultado = prod(l1, l2)

for valor in resultado:
    print(valor)
    

#versón con zip
""" def prod_zip(l1, l2):
    for a, b in zip(l1, l2):
        yield a * b """