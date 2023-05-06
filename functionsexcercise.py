# //two parameters

from ast import Num


def student_record(name,age):
    print(name,age)
student_record("Alice",20)

# //multiple numbers
def numbs(*nums):
    print(nums)
numbs(23,56,8,9,3)    

# for i in nums:
#     print(i)

# add and subtract
def add_sub(a,b):
    return a+b,a-b
add,sub=add_sub(23,4)   
print(add,sub) 

def show_employee(name,salary):
    print("name:",name,"salary:",salary)
show_employee("Peter",700)

# finding max n min
x = [4, 6, 8, 24, 12, 2]
def maximum(*num):
  return max(num)
maximum((4,6,8,24,2))  


# whileloop
def printnums():
    i=1
    while i<=10:
        print(i)
        i+=1
printnums()    

# nested loop
# outer loop
for i in range(1, 11):
    # nested loop
    # to iterate from 1 to 10
    for j in range(1, 11):
        # print multiplication
        print(i * j, end=' ')
    print()

# reverse 
# Write a function to reverse a string in Python without using any built-in functions.
def words():
    w="happy"
    print(w[::-1])
words()    

# Write a function that takes an array of integers and returns the sum of all the 
# even numbers in the array.
def sumnumbers(*numss):
    sum=0
    for num in numss:
        sum+=num
    print(sum)
sumnumbers(2,4,6,8,3)        

# Write a function that takes an array of integers and returns the sum of all the 
# odd numbers in the array.
def sumodd(*oddnums):
    sum=0
    for i in oddnums:
        if i %2!=0:
            sum+=i
    print(sum)
sumodd(3,6,7,1,2,5)            

# Write a function that takes an array of integers and returns the largest number 
# in the array.
def largestnumb(*largest):
     print(max(largest))
largestnumb(2,45,7,32,5)  
      
# Write a function that takes an array of integers and returns the smallest number
#  in the array.
def smallestnumb(*smallest):
        print(min(smallest))
smallestnumb(2,3,4,5,23)        
# Write a function that takes an array of integers and returns a new array with all 
# the even numbers removed.
def remove_even(*even_numbers):
    new_array=[]
    for e in even_numbers:
        if e %2!=0:
            new_array.append(e)
            print(new_array)  
remove_even(5,6,3,4,5,8)              
# Write a function that takes an array of integers and returns a new array with all 
# the odd numbers removed.
def remove_even(*even_numbers):
    new_array=[]
    for e in even_numbers:
        if e %2==0:
            new_array.append(e)
            print(new_array)  
remove_even(5,6,3,4,5,8)              
# Write a function that takes an array of integers and returns a new array with all 
# the duplicates removed.
def duplicates(*duplic):
    empty=[]
    for t in duplic:
        if t not in empty:
            empty.append(t)
            print(empty)
duplicates(3,5,4,8,3,7,5)          

# Write a function that takes an array of integers and returns the second largest 
# number in the array.
def second_largest(*large):
    list2=list(set(large))
    list2.sort()
    print(list2[-2])    
second_largest(3,5,4,7,8)    
# Write a function that takes an array of integers and returns the second smallest
#  number in the array.
def second_smallest(*large):
    list2=list(set(large))
    list2.sort()
    print(list2[1])    
second_smallest(3,5,4,7,8)    



# factorial
def factorial(n):
  return 1 if (n==1 or n==0) else n * factorial(n - 1)
num = 5
print ("Factorial of",num,"is",
      factorial(num))


# Write a function that takes two arrays of integers and returns a new array 
# containing the elements that appear in both arrays.
def  two_arrays():
    a={3,4,6,7,5,8}
    b={3,6,7,4,9}
    c=a.intersection(b)
    print(c)
two_arrays()    

# Write a function that takes an array of integers and returns a new array containing
#  only the prime numbers.
# def prime(*numbers):
#     new_list=[]
#     if numbers<2:
#      for i in range(2,int(numbers**0.5)+1):
#          if numbers%i ==0:
#             new_list.append(i)
# prime(6,1,2,3,4,7,9)             


# prime or not 
def prime_num(n):
    if n <2:
        return False
    for i in range(2,int(n**0.5)+1):

         if n%i==0:
             return False
    return True  
print(prime_num(3))   

# Write a function that takes an array of integers and returns the product of all the 
# numbers in the array.
def product_numbers(*product_nums):
    product=1
    for product_num in product_nums:
        product_nums *=product_num
        print()
product_numbers(3,4,2,7,5)        

# Write a function that takes an array of integers and returns the median value.

# Write a function that takes an array of integers and returns the mode value.
# Write a function that takes an array of integers and returns the range of the numbers 
# in the array.
# Write a function that takes an array of integers and returns the average of the numbers 
# in the array.
# Write a function that takes a string and returns the number of words in the string.
# Write a function that takes an array of strings and returns a new array with all the strings
#  capitalized.
# Write a function that takes an array of strings and returns a new array with all the strings 
# sorted alphabetically.
