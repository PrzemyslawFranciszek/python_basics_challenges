class Animal:
    exhaustion = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self, sound):
        return f"The {self.name} says {sound}"
    def walk(self, distance):
        try:
            if distance >= 0:
                if self.exhaustion + distance < 11:
                    self.exhaustion = self.exhaustion + distance
                    return f"{self.name} walk for {distance}, and its exhaustion raised to {self.exhaustion}!"
                else:
                    return "Distance or animal exhaustion is too big"
            else:
                return "You must enter value in positive number!"                    
        except TypeError:
            return "You must enter distance in numbers!"
    def sleep(self):
        if self.exhaustion > 0:
            self.exhaustion = self.exhaustion - 1
            return f"{self.name} is sleeping."
        else:
            return f"{self.name} can't sleep."
        
class Cow(Animal): 
    def speak(self, sound = "MUU"):
        return super().speak(sound)

class Duck(Animal):
    def speak(self, sound = "KWAA"):
        return super().speak(sound)

class Pig(Animal):
    def speak(self,sound = "OINKK"):
        return super().speak(sound)
bessie = Cow("Bessie", 5)
babe = Pig("Babe", 1)
