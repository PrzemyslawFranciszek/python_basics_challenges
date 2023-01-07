class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self, sound):
        return f"The {self.name} says {sound}"

class Cow(Animal): 
    def speak(self, sound = "MUU"):
        return super().speak(sound)
    
bessie = Cow("Bessie", 5)
