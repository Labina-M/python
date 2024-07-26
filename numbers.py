#for finding the greatest of three numbers

n1=int(input("enter values"))
n2=int(input("enter values"))
n3=int(input("enter values"))

def greatest(n1,n2,n3):
    if(n1>n2 and n1>n3):
     return n1
    elif(n2>n1 and n2>n3):
     return n2
    else:
     return n3
print(greatest(n1,n2,n3))
          