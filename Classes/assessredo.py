

# quiz4
empty_list =[]
class Possible_Fruit:
    def __init__(self,powers,effect,season,name):
        self.powers=powers
        self.effect=effect
        self.season=season
        self.name=name
    def __repr__(self):
         return f"{self.name} {self.effect} {self.powers} {self.season}"
fruits = Possible_Fruit(powers="changecolor",effect="gives energy",season="wet",name="big baobab")
empty_list.append(fruits)
print(fruits)
print(empty_list)
class Seasons:
    def __init__(self,seasons):
        self.seasons = seasons
    def __str__(self):
            return f"{self.seasons}"
    def predict_fruit(self):
        for item in empty_list:
            if self.seasons == item.season:
                print( f"{item.name} was produced in this {self.seasons} season")
s = Seasons(seasons="wet")
s.predict_fruit()



# quiz5
class Drum :
    def __init__(self,material,size):
        self.material=material
        self.size=size

    def  predict_sound(self):
        print (f"{self.__class__.__name__};{self.sound}")
class Djembe(Drum):
    sound=("Wide range of tones")  

class Talking_drum(Drum):
    sound=("Mimic human speech") 

class Bougarabou(Drum):
    sound=("Rich base tones")  
    
    drum1=Djembe(material="wood",size="small")
    drum1.predict_sound()
    drum2=Talking_drum(material="leather",size="medium")
    drum2.predict_sound()
    drum3=Bougarabou(material="cotton",size="big")
    drum3.predict_sound()
    
    