class Car:
    fuel_type="Diesel"
    def __init__(self,make,model,color):
        self.hooting=False
        self.make=make
        self.model=model
        self.color=color
    def hoot(self):
        return self.hooting
         # return f"The {self.color} {self.make}  peeeppeeeeps"    
    def start(self):
        return f"The {self.make} produces a vuur sound before moving"  
    def  pack(self):
        return f"The {self.color} {self.model} is packed in the garage"

