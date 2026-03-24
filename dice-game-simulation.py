from random import randint
for i in range(10):
    x=randint(1,6)
    if x==2 or x==5:
        print("ganier")
    else:
        print("perdant")
ganier=0
perdant=0 
for i in range(0,1000):
    x=randint(1,6)  
    if x==2 or x==5:
        ganier+=1
    else:
        perdant+=1
print("Nombre de ganiers : ", ganier)
print("Nombre de perdants : ", perdant)