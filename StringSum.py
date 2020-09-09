total=0
while True:
	a = input("Enter a number or type 'Done' : ")
	if a.isnumeric():
		total+=int(a)
	else:
		if a.upper()=='DONE':
			break
		else:
			print("**invalid character**")

print(total)



