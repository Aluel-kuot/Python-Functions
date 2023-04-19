
def even_numbers():
 x=range(10)
 for i in x:
    if i%2==0:
        print(i)

def odd_numbers():
 b=range(10)
 for i in b:
    if i%2!=0:
        print(i)     

def divisible_by_five():
    x=range(50)
    for i in x:
        if i%5==0:
            print(f"{i} is divisible by 5")
        else:
            print(f"{i} is not divisible by 5")     
def multiple_numbers():
    x=range(50) 
    for i in x:
        if i %5==0:
            print(f"{i} is divisible by 5")       
        elif i %7==0:
             print(f"{i} is divisible by 7")   
        elif i %9==0:
             print(f"{i} is divisible by 9")   
        else:
             print(f"{i} is divisible not by 5,7 and 9")  
def odd_even():
    x=range(20)
    for i in x:
         if i %2==0 and i%3==0:
            print(f"{i} is divisible by 2 and 3")       
         elif i %2==0 or i %3==0:
             print(f"{i} is divisible by 2 or 3")   
         else:
             print(f"{i} is divisible not by 2 and 3")  

def while_loop():
    x=1
    while x<10:
        print("Hello")            
        x+=1

def break_statement():
    x=1
    while x<10:
        print("Hello")            
        x+=1
        if x==5:
            break

def continue_statement():
    x=0
    while x<=20:           
        x+=1
        if x%3==0:
            continue
        print(x)

        # //Assignment
# //quiz1
def even_numb():
    a=0
    while a<=50:
        a+=1
        if a %2!=0:
            continue
        print(a)  

  # //quiz2  
#   for i in range(2,int(n/2)):
#     if (n%i) == 0:
def prime_number(num):
 if num==1:
        print("Not prime")
 elif num==2:
         print(" Prime")
 else:
        for x in range(2,num):
            if num % x==0:
                 print("Not prime")
            print(" Prime")  
            break  
#  //quiz3
def sum_integers(*numbers):
    sum=0
    for number in numbers:
        sum+=number
    print(sum)          

#  //quiz4
def divisible_by_three(a,b):
    x= range(a,b)
    sum=0
    for i in x:
     if i % 3==0:
      sum += i
    print(sum)


