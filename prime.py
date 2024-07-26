#PRIME NUMBERS

#z=int(input("enter a number"))
#for i in range (2,z):
#    if z % i == 0:
#        print("not prime")
#        break
#else:
#    print("prime")




#prime numbers using def func
def check_prime(n):
    for i in range (2,n//2+1):
        if n%i==0:
            return False
        else :
            return True
print(check_prime(101))