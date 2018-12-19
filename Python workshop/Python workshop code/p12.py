days=input("Enter number of days:")
year=days/365
remainder=days%365
weak=remainder/7
days=remainder%7

print "Year=",year," weak=",weak," days=",days
