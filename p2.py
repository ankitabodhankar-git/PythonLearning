# String 
# string silicing
name =  "Youcandoit"
print(name [0:4])   #reapet practise
print(name [:-5])

# str without character
a = "helloworld"
print(a[1:])

# reverse string
s = "Hello world"
print (s[::-1])  # imp 

#  print every 2nd char
a = "pythonpractise" 
print(a[::2])

# upper lower case str
a = input("enter the string:")
print(a.upper())
print(a.lower())
print(a.strip ()) #remove space  use in login cleanup
print(a.isdigit())  # chk digit ahe ki ny
print(a.startswith())

# practise  Q.
sentence = input("enter your sentence:")
clean_sentence = sentence.strip()  #removes start/end space 0nly
clean_sentence = " ".join(sentence.split()) # join spilt sentence together #method 1st,then print 
print(clean_sentence)


# Q.
word = input("enter ur word:")
print("first character:", word[0]) #imp solve reapeat
print("last character:", word[-1])


# chk char exsist in string or not
string = input("enter ur string:")
char = input("enter ur char:")
if char in string:
    print("character found")
else:
    print("character not found")

#   Q.
a = input(("enter the string:"))
print (a[:5]) #1st  5char only

print(a[-5:]) #last 5char only

print(a[2:])  # without 1st char

print(a[:-1]) #without last char

print(a[2:7]) #index 2-6 print

print(a[::2]) #every 2 char hide/not print 




# q

#  loops 
# for i in range (1,11):
#     # print(i)


# reverse loop
"""for i in range (10,0,-1):
    print(i)"""
# print even numbers from 1 to n
"""n = int(input("enter the number:"))
for i in range(1, n+1):
   if i  % 2 == 0:   #contitional loop
     print (i)

#odd numbers 1- n
n = int(input("enter the number:"))
for i in range(1,n+1):
   if i % 2 == 1:
      print (i)"""

# sum of numbers { Sum = n × (n + 1) / 2}
"""n = int(input("enter the number:"))
total = 0  #bcoz ur box is now empty and u hve to fill box one by one until..
for i in range (1, n+1):
  total = total + i   # now u can add one by one items in box so why this use
  print("sum is:",total ) # use total bcoz new total pahije so

n = int(input("enter the number: "))
total = 0   # box is empty

for i in range(1, n + 1):
    total = total + i   # keep adding

print("sum is:", total)   # ✅ outside loop"""

 

