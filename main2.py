# class Car:
#     brand="BMW"
#     year="2024"
#     motor=4.4
#     def drive(self):
#         print("driving")
# car=Car()
# car1=Car()
# car.drive()
# print(car.brand,car.motor,car.year)

# class Shark:
#     def __init__(self, name1, age1):
#         self.name = name1
#         self.age = age1


# shark=Shark("Shark",3)  #Shark.init()
# print(shark.name)

# class Shark:

#     # Class variables
#     animal_type = "fish"
#     location = "ocean"


#     # Constructor method with instance variables name and age
#     def __init__(self, name, age,animal_type):
#         self.name = name
#         self.age = age
#         self.animal_type=animal_type

#     # Method with instance variable followers
#     def set_followers(self, followers):
#         print("This user has " + str(followers) + " followers")


# shark=Shark("Balina",3,"Fish")
# shark.set_followers(5)
# print(shark.name,shark.age,shark.animal_type,shark.location)



class Fish:
    def __init__(self, first_name, last_name="Fish",
                 skeleton="bone", eyelids=False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim(self):
        print(f"The {self.first_name} is swimming.")

    def swim_backwards(self):
        print("The fish can swim backwards.")


class Shark(Fish):
    def __init__(self, first_name, last_name="Shark",
                 skeleton="cartilage", eyelids=True):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim_backwards(self):
        print("The shark cannot swim backwards, but can sink backwards.")
shark=Shark("Some")
shark.swim()

