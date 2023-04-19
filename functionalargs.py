
# positional,default and keyword arguments
def yearOfBirth(name,age):
    print(f"Hello{name}you were born in{age}")

def my_country(country="Kenya"):  
    print(f"hello you are from {country}")

# //forms a list
def   write(*names):
    nam=''
    for name in names:
        return(f"Hello {name}")

        
        
#  adds many numbers
def add(*nums):
    sum=0
    for num in nums:
        sum += num
    return sum
    
def multiply(**kwargs):
    answer=1
    for number in kwargs.values():
       answer *=number
    return answer

# Assignment
def concatenate_args(*peoples):
    word=""
    for people in peoples:
        word+=people
    return word

def concatenate_kwargs(**words):
    city=""
    for word in words.values():
        city +=word
    return city



