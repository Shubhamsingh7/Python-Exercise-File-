# Program for calculating Income Tax Return

slab1=250000
slab2=500000
slab3=1000000
slab4=2000000

def lessThenSixty(income):

    if income <=slab1:
        return 0
    elif income <=slab2:
        itr=((income-slab1)*5)/100
        itr=itr+(itr*4)/100
        return itr
    elif income <=slab3:
        itr=((slab1*5)/100) + (((income-slab2)*20)/100)
        itr = itr + (itr * 4) / 100
        return  itr
    else:
        itr = ((slab1 * 5) / 100) + ((slab2 * 20) / 100) + (((income-slab3)*30)/100)
        itr = itr + (itr * 4) / 100
        return itr


def seniorCitizon(income):
    if income <=300000:
        return 0
    elif income <=500000:
        itr=((income-300000)*5)/100
        itr=itr+(itr*4)/100
        return itr
    elif income <=1000000:
        itr=((300000*5)/100) + (((income-slab2)*20)/100)
        itr = itr + (itr * 4) / 100
        return  itr
    else:
        itr = ((300000 * 5) / 100) + ((slab2 * 20) / 100) + (((income-slab3)*30)/100)
        itr = itr + (itr * 4) / 100
        return itr


def seniorCitizon80(income):
    if income <= 500000:
        return 0
    elif income <= 1000000:
        itr = ((income - 500000) * 20) / 100
        itr = itr + (itr * 4) / 100
        return itr

    else:
        itr = ((500000 * 20) / 100) + (((income - slab3) * 30) / 100)
        itr = itr + (itr * 4) / 100
        return itr



def display(itr,income,age):
    print()
    print(f"Income Tax Return for Salary {income} in  financial Year 2018-2019 of age {age} is  Rupee {itr} Only !!! ")




income=int(input("Please Enter Total Income of Current  Financial Year:"))
age=int(input("Please Enter your age:"))
if age<60:
    itr=lessThenSixty(income)
    display(itr,income,age)
elif (age>60) and (age<80):
    itr=seniorCitizon(income)
    display(itr, income,age)
else:
    itr=seniorCitizon80(income)
    display(itr, income,age)

