d=input("Enter date in format MMDDYYYY : ")
a=d[0:2]
date=d[2:4]
year=d[4:]
months=('January','February','March','April','May','June','July','August','September','October','November','December')
month=months[int(a)-1]
print("The date enterred is ")
aa=str(month)
bb=str(date)
cc=str(year)
final= aa+' '+bb+' ,'+cc
print(final)






