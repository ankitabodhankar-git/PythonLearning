# calculator using operations +,-,*,/

"""a = float(input("Enter first number"))
b = float(input("Enter second number"))

op = input("Enter operation (+, -, *, /, %, //):")

if op == "+":
    print("Result =", a + b)
elif op == "-":
    print("Result =". a - b)
elif op == "*":
    print("Result =", a * b)
elif op == "/":
    print("Result =",a / b)
elif op == "%":
    print("Result =", a % b)
elif op == "//":
    print("Result =", a // b)
else:
    print("Invalid operation")"""


# misecellion operator 
# identity = types is, is not
"""a=0
b=1              # note= {0 = FALSE , 1 = TRUE}
print (a is b)
print(a is not b)"""


# membership operator 
# in operator =  this value present inside a sequence
"""fruits = ["apple", "banana", "mango"]
print("apple" in fruits)   # True
print("grapes" in fruits)  # False

name = "ankita"
print("a" in name)     # True
print("z" in name)     # False

num = 7
print(num in range(1, 10))   # True

# not in = Is this value NOT present inside?
print("z" not in "ankita")   # True"""


# usernm validation using membership operator
"""user=['ankita', 'archana','asmita','priyanka']
username = (input("enter ur username:"))
if username in user:
    print("login")
else:
    print("invalid")"""

# marks validation
"""marks = int(input("enter marks: "))

if marks in range(0, 101):
    print("valid marks")
else:
    print("invalid marks")"""

# lies between 10-50
"""num = int(input("enter ur number:"))
if num in range(10,50):
    print("valid")
else:
    print("invalid")"""

"""marks = int(input("enter marks:"))
if marks <0  or marks >100:   #logical operator use
    print("invalid")
else:
    print("valid")


# practise mix questions
n= int(input())
if n in range(0,99):
  print("inside values")
else:
  print("outside")

num = int(input())

if num % 3 == 0 or num % 5 == 0:  # for chk only for dvisible ahe ki ny not divide
    print("special number")
else:
    print("not special")

# calculatorhumansimple
a= int(input("enter 1st number:"))
b= int(input("enter 2nd number:"))
print("Addition, Substraction, Multiplication, Division")
op= input ("enter operstion to perform:")
if (op=="Addition"):
    print("Addition of a:","and b",b,"is:",a+b)
elif(op=="Substraction"):
    print("Substraction of a:","and b",b,"is:",a-b)
elif(op=="Multiplication"):
    print("Multiplication of a:","and b",b,"is:",a*b)
elif(op=="Division"):
    print("Division of a:","and b",b,"is:",a/b)
else:
    print("invalid operation")"""

# vowel and consonant checking

ch = input("enter character to check");
if (ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u',
    ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U'):
    print(ch,"is vowel")
else:
    print(ch, "is consonant")









