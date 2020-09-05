student_records = {}

def printmenu():
	print('''\n\n
		
		Student Management:   
		1. Add Record         
		2. View Record        
		3. Exit               
		\n\n''')


def menu():
	
    choice = int(input("Enter your choice : "))
    if choice==1:
        addrec()
    elif choice==2:
        viewrec()
    elif choice==3:
        print('Thank You')
    else:
        print("Enter valid character")
        menu()
		
def addrec():
	adm_no = int(input("\nEnter admission number "))
	name = input("\nEnter student's full name ")
	roll_no = int(input("\nEnter roll number "))
	sub = int(input("\nEnter number of subjects taken "))
	subjects={}
	for i in range(sub):
		s=input("\nEnter subject ")
		m=input("\nEnter marks in {0} ".format(s))
		subjects[s]=m
	student_records[adm_no]=(name,roll_no,subjects)

	printmenu()
	menu()

def viewrec():
	query=int(input("\nEnter admission number of student "))
	isin = False
	for i in student_records.keys():
		if i==query:
			isin = True
			break

	if isin:
		dicth = student_records[query]
		print("\n\nName:{0}\nRoll No.:{1}".format(dicth[0],dicth[1]))
		subs = dicth[2]
		for i in subs.keys():
			print("{0}:{1}".format(i,subs[i]),end="\n")
	else:
		print("Admission Number not found")

	printmenu()
	menu()


printmenu()
menu()








