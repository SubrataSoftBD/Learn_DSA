class Animal:

    def speak(self):
        print("Animal speak")

class Cat(Animal):
    def speak(self):
        print("Cat speak")


a = Animal()
b = Cat() 

# a.speak()
# b.speak()


class Father:
    
    def home(self):
        print("House for you")


class Mother:
    
    def gold(self):
        print("Gold id for you")
        
        
class son(Father, Mother):
    pass


a = son()

a.gold()
a.home()