import  sys

def prime(n):

    flag=0

    for i in range(2,n//2):
        if n%i==0:
            flag=1
        else:
            pass
    if flag==0:
        return True
    else:
        return False

def palindrome(n):
    a=n
    i=0
    num=0
    while(n!=0):
        rem=n%10
        num=num+rem*(10**i)
        i+=1
        n=n//10

    if a==num:
        return True
    else:
        return False






for i in range(999,99,-1):
    for j in range(999, 99, -1):
        k=palindrome(i*j)
        if k==True:

            print(f"{i}*{j}={i*j}")
            sys.exit()
        else:
            print(f"{i}*{j}={i*j}")