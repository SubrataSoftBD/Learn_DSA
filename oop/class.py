class StoreName:
    def __init__(self, name):
        self.name = name

    def getYourName(self):
       return self.name


userOne = StoreName("Subrata")
userTwo = StoreName("Tridip")

print(f"First user name {userOne.getYourName()}")
print(f"First user name {userTwo.getYourName()}")