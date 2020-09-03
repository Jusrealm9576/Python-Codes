
def question():
	print("\n\n \t1. Calculate the factorial of number N\n \
	2. Display fibbonacci sequence (0 to N)\n \
	3. Check wether the number is armstrong or not\n\
	4. Check wether the number is palindrome or not\n\
	5. Display table of number N\n\
	6. Exit\n ")
def menu():
    a = int(input("Enter number [1-6]: "))
    if a == 1:
        fact()
    elif a == 2:
        fibo()
    elif a == 3:
        arm()
    elif a == 4:
        pal()
    elif a == 5:
        multiples()
    elif a == 6:
        print('Thank You')
    else:
        print("\nENTER A NUMBER FROM 1 TO 6 ")
        question()
        menu()
def fact():
    num = int(input('enter number'))
    factorial = 1
    if num < 0:
       print("Sorry, factorial does not exist for negative numbers")
    elif num == 0:
       print("The factorial of 0 is 1")
    else:
       for i in range(1,num + 1):
           factorial = factorial*i
       print("The factorial of",num,"is",factorial)
       question()
       menu()
def fibo():
    nterms = int(input("How many terms? "))
    n1, n2 = 0, 1
    count = 0
    if nterms <= 0:
       print("Please enter a positive integer")
    elif nterms == 1:
       print("Fibonacci sequence upto",nterms,":")
       print(n1)
    else:
       print("Fibonacci sequence:")
       while count < nterms:
           print(n1)
           nth = n1 + n2
           n1 = n2
           n2 = nth
           count += 1
       question()
       menu()
def arm():
    num = int(input("Enter a number: "))
    sum = 0
    temp = num
    while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10
    if num == sum:
       print(num,"is an Armstrong number")
    else:
       print(num,"is not an Armstrong number")
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
def multiples():
    num = int(input('enter number'))
    for i in range(1, 11):
       print(num, 'x', i, '=', num*i)
    question()
    menu()
question()
menu()
