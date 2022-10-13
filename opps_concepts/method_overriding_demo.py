class Animal:

    def speak(self):
        pass

    def walk(self):
        pass


class Dog(Animal):

    def speak(self):
        print("Bhowwww from DOG")

    def walk(self):
        print("4 legs")


class VodaphoneDog(Dog):

    def speak(self):
        print("Bhoww with cure vodaphone dog")

    def walk(self):
        print("Walking with small 4 legs")


v = VodaphoneDog()
v.speak()
v.walk()

