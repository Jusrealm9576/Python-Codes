

def question():
	print("\n\t 1.Check wether string is pallindrome or not\n\
	2. Calculate total characters of string\n\
	3. Calculate total vowels in string\n\
	4. Calculate total spaces in string\n\
	5. Display string in reverse order\n\
	6. Exit\n")

def menu():
    a = int(input("Enter number [1-6]: "))
    if a == 1:
        pal()
    elif a == 2:
        cha()
    elif a == 3:
        vow()
    elif a == 4:
        spac()
    elif a == 5:
        rev()
    elif a == 6:
        print('Thank You')
    else:
        print("\nENTER A NUMBER FROM 1 TO 6 ")
        question()
        menu()

def pal():
    n=int(input("Enter number:"))
    temp=n
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    if(temp==rev):
        print("The number is a palindrome!")
    else:
        print("The number isn't a palindrome!")
    question()
    menu()
def cha():
    inp = str(input("Enter a string "))
    a= len(inp)
    print("Total number of characters in string is " ,a)
    question()
    menu()

def vow():
    string=input("Enter string:")
    vowels=0
    for i in string:
          if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
                vowels=vowels+1
    print("Number of vowels are:", vowels)
    question()
    menu()
def spac():
    string=input("Enter string:")
    spaces=0
    for i in string:
          if(i==' '):
                spaces=spaces+1
    print("Number of spaces are:", spaces)
    question()
    menu()
def rev():
    txt = str(input('enter string'))
    a=txt[::-1]
    print('Reversed string is: ',a)
    question()
    menu()
question()
menu()
