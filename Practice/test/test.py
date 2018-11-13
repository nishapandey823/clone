'''import sys
a =  sys.version
print(a)
b =  sys.version_info
print(b)

import datetime
a = datetime.datetime.now()
print(a)

a = input("enter firstname")
b = input("enter lastname")
print("hello"+ " " + a + " " + b)

a = input("enter comma separated values:")
list = a.split(",")
tuple = tuple(list)
print(list)
print(tuple)

filename = input("Input the Filename: ")
f_extns = filename.split(".")
#print ("The extension of the file is : " + repr(f_extns[-1]))
print(f_extns[0])
print(f_extns)



color_list = ["Red","Green","White" ,"Black"]
print(color_list[0])
print(color_list[1])


exam_st_date = (11, 12, 2014)

print("exam will start from: %i /%i/%i" %(exam_st_date))

print (abs.__doc__)
from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)

from datetime import date

start = date(2014, 7, 2)
end = date(2014, 7, 11)
print(start-end)
a = int(input("enter a number"))

b = 17
print(abs(a-b))

def near_thousands(a):
    return (abs(1000-a) <=100) or (abs(2000-a)<=1000)

print(near_thousands(1000))   

a = int(input("enter 1st number"))
b = int(input("enter 2nd  number"))
c = int(input("enter 3rd number"))

if a==b==c:
    print(3*(a+b+c))
else:
    print(a+b+c)    

def new_str(str , n):
    result = " "
    for x in range(n):
        result = result + str
    return result

print(new_str("abc" , 2))   

def count(nums):
    count = 0
    for x in nums:
        if x== 4:
            count = count+1
    return count

print(count((1,2,3,4,5,4,4)))    

def is_vowel(alphabets):
    alpha = "aeiou"
    return alphabets in alpha

print(is_vowel("c"))  

for x in range(1,237):
    if x%2 == 0:  
        #list.append(x)
        print(list(x))

color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])           
print(color_list_1.difference(color_list_2))

a = int(input("enter a number"))
b =  int(input("enter other number"))
sum = a+b

if sum in range(15,20):
    print("sum is 20")
else:
    print (sum)   

import math

a =  [1,2]
b =  [3,4]
distance = math.sqrt(b[0]-a[0**2] + b[1]-a[1**2])
print(distance)

import struct
print(struct.calcsize("P")* 8)
x = set()
print (x)

x = set([1,2,3,4])
print(x)

n = set([1,2,3,4,5,6,7,8,9,10])
for x in n:
    print(x)

a = set()
a.add("red")
print(a)   
a.update(["green","blue", "orange"])
print(a)
a.pop()# removes from starting
print(a)
a.discard("blue")
print(a)
x = set([1,2,3,4,5])
y = set([3,4,6,7,8]) 
print(x & y)# intersection of sets(gives common values between two sets)
print(x.difference(y))# set differencing(gives values present in x only)
print(y.difference(x))# set differencing(gives values present in y only)
print(x|y)#union of two sets
print(x.union(y))

z = x.copy()
print(z)
x.clear()
print(x)# set x is empty now
p = set([10,20,30,40,50,60,70,80,90,100])
print(p)
print(max(p))#maximum value of a set
print(min(p))#minimum value of a set
print(len(p))#length of a set
q = set([10,20,20,30,30,30,30,30,30])
print(q)# do not contain duplicates
print("a")
print("hello world")

x = ()
print(x)
y = tuple()
print(y)
a = tuple(["a", 1, "b", 3 , 4.5])
print(a)
b= ([1,2,3,4,5])
print(b[3])
print(a + (9,))
l= [10,20,30,40]
print(a + tuple(l))# tuples are immutable 
m = ('a','b','c','d','e','f')
str= ','.join(m)
print(str)
n = ('e','x','e','r','c','i','e','s')
str = ''.join(n)
print(str)
tuplex = (1,2,3,5,4,3,2,1,5,5,4,5,6,1,6)
print(tuplex.count(5))# to count a particular number n a tuple
print(5 in tuplex)#tp check wether an element exixt in tuple or not
print(10 in tuplex)
# tuples are immutable, so cannot remove any elemnt from a tuple
tuplexx = (1,2,3,4,5)
tuplex1 =  list(tuplexx)# convert a tuple in a list
print(tuplex1)
tuplex1.remove(5)
print(tuplex1)
tuplex2 = tuple(tuplex1)
print(tuplex2)
print(tuplex2.index(3))# to find index of an element
print(len(tuplex2))
# convert tuple to a dictionary

a = ((1,2),(3,4),(5,6),(7,8))
print(dict((x,y) for x,y in a))

l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print([t[:-1] + (100,) for t in l])
# to count numbers in  list until element is a tuple
num = [10,20,30,40,(10,20),40]
count =  0
for x in num:
    if isinstance(x , tuple):
        break
    count = count+1
print(count)           
#sort a tuple
price = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print(sorted(price, reverse= True))
def sum_list(a):
    count = 0
    for x in a:
        count = count+x
    return count

print(sum_list([1,2,4]))           

x = [4, 2,1]
largest = x[0]
for i in x:
    if i > largest:
        largest = i
print(largest)        

smallest = x[0]
for i in x:
    if i < smallest:
        smallest = i
print(smallest)        

word_length = 3'''

ints = [1,2,3,4]
ints.append(4)
print(ints.count(4))
ints.extend([6,7,8])
ints.sort(reverse= True)
print(ints)
 
d = {"name":"nisha", "age":12, "sex": "female"} 
print(d)
#for x in d:
    #print (x , "corresponds to" , d[x])
for key, value in d.items():
    print(key,value)
