sal = int(input("Enter annual salary "))
if sal <= 250000:
	print("No tax to be paid")
elif sal <= 500000:
    sav = int(input("Enter investments "))
    if sav >= 150000:
        a=(sal*5/100)-45000
        print("Tax to be paid = ",a)
    else:
        b=(sal*5/100)
        print("Tax to be paid ", b)
elif sal <= 1000000:
    sav = int(input("Enter investments "))
    if sav>=150000:
        c=(sal*20/100)-45000
        print("Tax to be paid = ",c)
else:
    d=sal*20/100
    print("Tax to be paid = ", d)
