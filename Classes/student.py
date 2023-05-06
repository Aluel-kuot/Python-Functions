# class Student:
#     name="Marion"
#     age=23
#     school="AkiraChix"
#     country="kenya"

    # instance variables

from datetime import  date   
class Student:
    school="AkiraChix"
    def __init__(self,first_name,last_name,age,country):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.country=country
    # def greet_student(self):
    #         return f"Hello {self.name} from{self.country}.Welcome to {self.school}"
    def full_name(self):
        return f"My name is {self.first_name}  {self.last_name}"

    def year_of_birth(self):
        current_year=date.today().year
        return current_year-self.age

    def show_initials(self):
        return  f"{self.first_name[0]}{self.last_name [0]}"   
         