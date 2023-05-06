
class Fruit:
    category="Fresh natural fruit"
    def __init__(self,color,taste,name):
        self.color=color
        self.taste=taste
        self.name=name

    def wash(self):
        return f"The {self.name} has been washed "   

    def store(self):
        return f"The {self.color} {self.taste} {self.name} has been eaten  "  
    def pill(self):
        return f"The {self.color}  {self.name} has been pilled "    
     
     
