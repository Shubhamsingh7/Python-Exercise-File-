a=input("Enter unit consumption")

if a<=150:
 print "Price is ",a*2.40

elif a>150 and a<300:
 print "price is ",((150*2.40)+(3*(a-150)))
else:
 print "price is",((150*2.40)+(3*(a-150))+(3.20*(a-300)))