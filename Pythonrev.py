

def addition(a,b):
    sum=a+b
    print(sum)
addition(12,21)
# list

# unpacing and packing
def listing(*lists):
   first,second,third,  *rest=lists
   print(first)
   print(second)
   print(third)
   print(*rest)
print (listing(1,3,6,7,8))

# Given two lists, write a function to find the common 
# elements between them and return them in a new list.
# finding duplicates in two lists
def duplicates(a,b):
    result=[i for i in a if i in b]
    return result
a=[1,4,6,7,8]
b=[5,6,9,3,4]
print (duplicates(a,b))

def numbers(c,d):
    result=[i for i in c if i in d]
    return result
c=(2,5,8,9,3,5)
d=(2,3,10,6,7)
print(numbers(c,d))

# Write a function that takes in a list of numbers and returns a new
#  list containing only the prime numbers.
def prime(*number):
    emptyList=[]
    for i in number:
        a=0
        for j in range(1,i):
           if i%j==0:
             a+=1
        if a== 1:
            emptyList.append(i)   
print(prime(1,2,3,4,5,6,13,11,34,56))


def num ():
    sum=1+3
    return sum
print(sum())
num()
print("today")
print("")
