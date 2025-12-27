 # take age and print how old r u after 10 days
age = int(input("enter ur age:"))
new_age = age + 10   
# when in que. ask find out new no. then use new operatore like this 
print("after 10 yr ur age will be", new_age)

# take 2 no. and print product, diff, sum
a = int(input())
b = int(input())
print("product of:", a * b)
print("difference of:", a - b)
print("sum of:", a + b)

# take int and print remainder when divide by 7
a = int(input())
rem = a % 7
print("remainder is:", rem )

# take no. even / odd
n = int(input())
if n % 2 == 0:
    print("even")
else:
    print("odd")

#find lagest no.
a = int(input())
b = int(input())
c = int(input())

print("largest num is:" , max (a, b, c ))


# grade system
marks = int(input("enter your marks: "))

if marks >= 90:
    print("A") # print krtana "" lavaych mhnje te str mdhi ans. yein without error 
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("Fail")

# /chk no. is in range
num = int(input("enter ur number: "))

if 1<= num <= 100 :   # never use range of this Q. we also use comparison operator <=
    
    print("valid")
else:
    print("invalid")

# chk temperature
temp = int(input("enter the temperature"))
if  temp > 30:
    print("hot")
elif  20 <= temp <= 30 :
    print("warm")
elif temp < 20 :
    print("cold")

#  leap yr chk
a = int(input())
if a / 400 :  # divisable sathi % this use
    print("leap")
elif a / 4 and a != 100:
    print (" leap")
else:
    print("not leap")
#  or

 
a = int(input())

if a % 400 == 0:
    print("leap")
elif a % 4 == 0 and a % 100 != 0:
    print("leap")
else:
    print("not leap")


# salary  = bonus
salary = int(input("enter ur salary"))
if salary < 10000:
    bonus = salary * 20
else:
    bonus = salary * 10 
total_salary = salary + bonus 
print("bonus=",bonus)
print("total salary=", total_salary)  # practise this reapet 

# login system
username = "ankita"
password = "ankita123 "  #stored data like this
                       
unm  = (input("enter ur username: "))
pwd = (input("enter ur password :")) # its just chk if correct or not
if username == correct_username and password == correct_password :
    print (" login successful")
else:
    print ("invalid")

# user validation
username = input("enter username").strip()
if username == " ":
   print("username cannot be empty")
else:
   print("username accepted")


# mob.no length chk
mobile = input("enter ur mobile number:").strip()

if mobile == "":
    print("error")
elif len(mobile) != 10:
    print("mobile must be 10 digit")
elif  not mobile.isdigit():
    print("mobile contain only digits")
else: 
    print("mobile accepted")

# pwd strength
password = input("enter ur password:")
if len(password) < 6:
    print("weak password")
else:
    print("strong password")

# marks validation
marks = int(input('enter ur marks:'))
if marks < 0 or marks > 100:
    print ("invalid marks")
else:
    print("accepted marks")

# imp EMAIL validation
email = input("enter ur email:")
if "@" in email: 
    print("valid email")   #imp
else:
    print("invalid email")     # inside/present ahe ki ny te chk use this;







