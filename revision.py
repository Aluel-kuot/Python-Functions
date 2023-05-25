# def   greet(*names):
#     for name in names:
#         print(f"welcome{name}")

# def  greets(**words):
#     result =""
#     for word in words.values():
#         result+=word
#         return result

# def call(you):
#     if you=="Alice":
#         return"How have you been?"+you
# age=10
# print(age)
# name=input("Come here")
# print("hello"+name)

def sum_multiplication(sum,multiplication):
     return(f"The sum  is{sum} and the product  is{multiplication}")
print(sum_multiplication(6+2+3,6*2*2                                                                                                                                                                                                                                                                                                                                                                                                                                                                ))

def peeps(**pples):
    for pple in pples.values():
      print(f"My name is {pple}")   
peeps(a="Aluel",b="Kuot",c="Mary")

# //Palindrome
# strings that do not change even when reversed
# write a function that detects whether something is a palindrome or not. 
# Returns true if the word is a palindrome and false if it is not a palindrome.
# Words:
# Noon
# Madam
# Radar
# Civic
# Racecar

def word(w):
     name="Noon"
     name==name[::-1]
     print(name)
word("noon")

def words(r):
     names="Madam"
     print(names[::-1])
words("madam")    

def write(b):
     writer="Radar"
     writer==writer[::-1]
     print(writer)
write("radar")

def civic(c):
     civ="Civic"
     civ==civ[::-1]
     print(civ)
civic("civic")     

def racecar(t):
     race="Racecar"
     race==race[::-1]
     print(race)
racecar("racecar")     


# Membership
def word(*words):
     c="Regina" in words
     print(c)
word("Regina","Aluel","Vero")


# //sum of numbers
def num(*nums):
     total=0
     for num in nums:
      total+=1
      return total
print(num(2,3,56,7,8))

def  date_of_birth(now,then) :   
     age=now-then
     return age
print(date_of_birth(2023,1999))

# //even or not even
def is_even(n):
     if n %2==0:
          print('even')
          return True
     return False     
print(is_even(10)) 
print(is_even(5))  

# //find even numbers
def find_even_numbers(n):
     evens=[]
     for i in  range(n+1):
          if i % 2 ==0:
               evens.append(i)
     return evens
print(find_even_numbers(20))               

    # square of numbers
def square_numbers():
     nums=[2,4,5,6]
     for i in nums: 
          print (i**2)
square_numbers()
         

def set_numbers():
     a={1,2,3,4}
     b={2,5,3,1}
     print (a.difference(b))  
set_numbers()

def smallest():
     c=[3,5,7,8,9]
     print(min(c))
smallest()    
def occurrence():
     days=["Monday","Tuesday","Monday"]
     v=days.count("Monday")
     print(v)
occurrence()     
     
def smallest():  
     small=[3,6,2,4,1,5,7]  
     print(min(small))
smallest()     