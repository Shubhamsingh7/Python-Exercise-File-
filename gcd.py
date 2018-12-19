def gcd(a,b):
    if a%b==0:
        return b
    else:
        return gcd(a,b%a)


num1=int(input("Enter 1st number"))
num2=int(input("Enter 2nd number"))
print(gcd(num1,num2))