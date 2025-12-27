# decision statements

a = int(input("enter a value:"))
if a%2==0:
    print("even")
else: 
    print("odd")


a = int(input("enter value:"))
if a>0:
    print("positive")
elif a>=0:
 print("negative")
else:
    print("neutral")


a= int(input("enter number:"))
if a>=18:
    print("eligible")
else:
    print("not eligible")

# grading system
a = int(input("enter ur marks"))
if a>=90:
    print("very good")
elif a>=50:
    print(" average")
elif a<= 35:
    print("poor")
else:
    print("invalid")


# nested if 
pin = input("enter ur pin: ")
if len(pin) == 4:
    if pin == "1234":
        print("Access granted")
    else:
        print("Wrong pin")
else:
    print("Invalid pin format") 

    

# FOR loop
name ="ankita"
for ch in name :
    print(ch, end=" ")

# print numbers from 1-10
num = 10
for num in range(1,11):
    print(num)  #one by one line print
    print(num, end=" ") # in one-line print

#print even num between 1-30
for num in range(1,31):
    if num %2==0 :  #Print only some values use if
     print (num, end=" ")

# odd numbers
for i in range (1,21):
    if i %2==1 :
       print(i)

# while loop
i=1
while i<=5:
    print(i)
    i += 1 #always use  to avoid infinte loop

# jump/control statements 
# break statement  - use stop loop whenever
for i in range(1,10):
    if i == 6:
        break
    print(i)

# continue statement - skip current step
for i in range(1,11):
    if i == 5:
        continue
    print(i, end=" ")
       
# pass statement - means its a placeholder can hold errors
age = int(input())
if age > 18:
    pass
else:
    print("Minor")


# print number from 1-n
n = int(input("enter number:"))
for n in range (1, n+1):
     if n%2 !=0:
          print("odd number is:", n)

#  reverse string
n = int(input())
for i in  range(10,0,-1):
    print(i)
    
#table of numbers
n = int(input())
for i in range(1,11):
    print(n, "x", i, "=", n * i)
    
    
