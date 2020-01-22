print ("01 Jan 2020")
print ("Test Hello World1")
print ("Test Hello World2")
print ("Test Hello World3")
print ("Test Hello World4")

"""
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


print ("# Prime Number using for loop and range : ================================")

for num in range(2, 10):
...     if num % 2 == 0:
...         print("Found an even number", num)
...         continue
...     print("Found a number", num)


# write Fibonacci series up to n
def fib(n):    
#Print a Fibonacci series up to n.
 a, b = 0, 1
 while a < n:
     print(a, end=' ')
     a, b = b, a+b
 print()
fib(1000)

fib
f=fib
f(100)


def fib2(n):  # return Fibonacci series up to n
#Return a list containing the Fibonacci series up to n
 result = []
 a, b = 0, 1
 while a < n:
    result.append(a)    # see below
    a, b = b, a+b
 return result

f100 = fib2(100) 
f100


def ask_ok(prompt, retries=4, reminder='Please try again!'):
 while True:
  ok = input(prompt)
  if ok in ('y', 'ye', 'yes'):
      return True
  if ok in ('n', 'no', 'nop', 'nope'):
      return False
  retries = retries - 1
  if retries < 0:
     raise ValueError('invalid user response')
  print(reminder)

ask_ok('Do you really want to quit?',4,'Try Again')


i = 5
def f(arg=i):
    print(arg)
f() 


def f(a, L=[]):
    L.append(a)
    return L

print(f("Basharat"))
print(f("Wani"))
print(f("Bothell")) 

print ('                 ')
print ('Start of new Task')

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword 


print (' ')
print ('5. Data Structures')

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana', 'Basharat Wani']

print ('' + str(fruits.count('apple')) + '')
print ('' + str(fruits.count('tangerine')) + '')
print ('' + str(fruits.index('banana')) + '')
print ('' + str(fruits.index('banana', 4)) + '') # Find next banana starting a position 4
fruits.reverse()
print ('' + str(fruits) + '')
fruits.append('grape')
print ('' + str(fruits) + '')
fruits.sort()
print ('' + str(fruits) + '')
fruits.pop()
print ('' + str(fruits) + '')


from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives

print ('' + str(queue) + '')


queue.popleft()                 # The first to arrive now leaves
print ('' + str(queue) + '')


squares = []
for x in range(9):
    squares.append(x**2)
print ('' + str(squares) + '')
"""


print ('5. Dictionaries ')
# Tel is Dictionaries 
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print ('' + str(tel) + '')
print ('' + str(tel['jack']) + '')

tel['irv'] = 4127  # Add more to dict
list(tel)
print ('' + str(tel) + '')

print ('' + str(sorted(tel)) + '')

'jack' in tel
