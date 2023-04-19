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



