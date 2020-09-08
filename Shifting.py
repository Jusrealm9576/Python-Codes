lista = input("Enter comma seperated values : ")
c =''
a = []
for i in lista:
	if not i==',':
		c += i
	if i==',':
		a.append(c)
		c=''
a.append(c)

newlist=[]
for i in range(0,len(a)):
	newlist.insert(i,a[i-1])
print(lista)
print(a)
print(newlist)


