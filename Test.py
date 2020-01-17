print ("01 Jan 2020")
print ("Test Hello World1")
print ("Test Hello World2")
print ("Test Hello World3")
print ("Test Hello World4")

print  (2+2)
print  (50-5*6)
print  ((50 - 5*6) / 4)

print ("# Division always returns a floating point number")
print  ( 8 / 5)

print (" # classic Division returns a float")
print  (17/3)

print ("# Floor division discards the fractional part")
print  (17//3)

print ("# the % operator returns the Remainder of the division")
print  (17 % 3)

width = "Test"

print ("=" + width + "==") 

width = 1002

print ("=" + str(width) + "==") 


print ("# List like an array")
squares = [1, 4, 9, 16, 25]
test = squares[1]

print ("" + str(test)+"")
test = squares[-1]

print ("" + str(test)+"")
squares = [1, 4, 9, 16, 25]
print ("Concatenation" + str(squares) + "End")

#string are immutable, lists are a mutable type 
squares = squares + [100,200,300]
print ("Mutable Concatenation" + str(squares) + " End")


#Replace
cubes = [1, 8, 27, 65, 125]

print ( "Old Cubes with error for 65 " + str(cubes)+  "")

#Replace 65 with 64 as 65 is not a cube 
cubes[3] = 64  # replace the wrong value

print (cubes)
cubes.append(216)
cubes.append(7**3)
print (cubes)

print ("Letters")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print (letters)

# replace some values
letters[2:5] = ['C', 'D', 'E']

print (letters)

letters[2:5] = []

print (letters)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print (letters)

#len will give you length of string
#letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#len(letters)
#print ("test" + str(letters) + "Test")

# clear the list by replacing all the elements with an empty list
letters[:] = []
print (letters)

print ("#Fibonacci series: ================================")

#Fibonacci series:
# the sum of two elements defines the next
a, b= 0, 1
print (a)
print (b)
print ("Before the while loop print the value of a is  " + str(a) +"")
print ("Before the while loop print the value of b is  " + str(b) +"")

while a < 1000:
 #print("Inside Loop")	
 print (a)
 a, b = b, a+b
# print ("print the value of B is  " + str(b) +"")
print ("# End of Fibonacci series: ================================")



print ("#if and else if or elif: ================================")

#x = int(input("Please enter an integer: "))
#if x < 0:
# x = 0
# print('Negative changed to zero')
#elif x == 0:
# print('Zero')
#elif x == 1:
# print('Single')
#elif x == 2:
# print('double')
#elif x == 3:
# print('tripe')

print ("# For Loop : ================================")
# Measure some strings:
words = ['cat', 'window', 'defenestrate']
for w in words:
 print(w, len(w))



print ("# Prime Number using for loop and range : ================================")

for n in range(2, 100):
 #print ("first for loop value of n range is # " + str(n)+"")
 for x in range(2, n):
  #print (x)
  #print ("Second for loop value of x range is # " + str(x)+"")
  #print ("Second for loop value of n range is # " + str(n)+"")

  #print (n)
  if n % x == 0:
   print(n, 'equals', x, '*', n//x)
   break
 else:
   # loop fell through without finding a factor
   print(n, 'is a prime number')


"""
print ("# Prime Number using for loop and range : ================================")

for num in range(2, 10):
...     if num % 2 == 0:
...         print("Found an even number", num)
...         continue
...     print("Found a number", num)
"""