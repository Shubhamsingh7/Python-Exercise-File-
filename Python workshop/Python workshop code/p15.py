print "Choice"
print "1 for doller"
print "2 for rupee"
choice=input("Enter choice")
if choice==1:
    doller=input("Enter doller amount")
    print "Equivalent rupee=",doller*65
elif choice==2:
    rupee=input("Enter rupee amount")
    print "Equivalent doller=",rupee/65.00
else:
    print "Invalid input"
