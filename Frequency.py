a = input("Enter comma seperated values : ")
c =''
b = []

for i in a:
	if not i==',':
		c += i
	if i==',':
		b.append(c)
		c=''
b.append(c)


print(b)

x = input("Enter element to be searched ")
c=0
for i in b:
	if i==x:
		c+=1
print(x," occurs",c ,"times in the list")





