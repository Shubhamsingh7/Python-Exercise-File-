from functools import lru_cache


def findnine(a):
    flag=0
    while a!=0:
        rem=a%10
        a=a//10
        if rem==9:
            flag=1
            return 1
    return 0


@lru_cache(max==1000000000000000000)
def nine(n):
    if j % 9 == 0:
        return False
    elif findnine(j) == 1:
        return False
    else:
        return True




t=int(input("Enter Test Case:"))

for i in range(t):
    f,l=(input("Enter f and l:")).split()
    f=int(f)
    l=int(l)
    count=0
    for j in range(f,l+1):

      if nine(j)==True:
          count+=1

    print(f"case #{i+1}: {count}")