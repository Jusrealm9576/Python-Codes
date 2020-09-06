lista = [3,25,13,6,35,8,14,45]
newlist = []
index=0
for i in lista:
	if i%5==0:
		newlist.insert(index-1,i)
		index+=1
		continue
	else:
	    newlist.append(i)
	    index+=1

print(lista)
print(newlist)




