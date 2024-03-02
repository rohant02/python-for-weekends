class Animal():
    
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def sing(self):
        print(f"The {self.name} goes '{self.sound}'")


dog = Animal("dog", "woof")
cat = Animal("cat", "meow")
bird = Animal("bird", "tweet")


animals = [dog, cat, bird]
for animal in dog,cat,bird:
    animal.sing()
