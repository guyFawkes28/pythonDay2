# Menor de tres números

n1=int(input("Enter number 1--->"))
n2=int(input("Enter numer 2--->"))
n3=int(input("Enter number 3--->"))

if n1>n2 and n1>n3:
    print("El numero mayor es-->",n1)

elif n2>n1 and n2>n3:
    print("El numero mayor es-->" ,n2)

else:
    print("El numero mayor es-->",n3)