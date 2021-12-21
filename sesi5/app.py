# raka = ["Raka Ardhi", 28, "CurDev", 2265]
# spock = ["Spock", 35, "Science Officer", 2254]
# mccoy = ["Leonard McCoy", "Chief Medical Officer", 2266]

# print("Daftar nama : ", raka[0], spock[0], mccoy[0])
# print("Daftar umur : ", raka[1], spock[1], mccoy[1])
# print("Daftar jabatan : ", raka[2], spock[2], mccoy[2])
# print("Daftar tahun mulai : ", raka[3], spock[3], mccoy[3])

# class Dog:
#     species = 'Canis familiaris'

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def description(self):
#         return f'{self.name} is {self.age} years old'

#     def speak(self, sound):
#         return f'{self.name} says {sound}'

# buddy = Dog("Buddy", 9)
# miles = Dog("Miles", 4)
# scooby = Dog("Scooby", 1)
# hike = Dog("Hike", 1)

# print(buddy.description())
# print(miles.description())

# print(scooby.speak('Doo bee Doo'))
# print(hike.speak('bark'))


class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self) -> str:
        return f'{self.name} is {self.age} years old'

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"


miles = Dog("Miles", 4, "Jack Russell Terrier")
buddy = Dog("Buddy", 9, "Dachshund")
jack = Dog("Jack", 3, "Bulldog")
jim = Dog("Jim", 5, "Bulldog")


class Bulldogs(Dog):
    def __init__(self, name, age):
        super().__init__(name, age, 'bulldogs')

    # Another instance method
    def speak(self):
        return f"{self.name} says woof woof"


jake = Bulldogs('jake', 2)

print(jake)
