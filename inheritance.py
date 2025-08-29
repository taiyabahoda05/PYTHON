# class Car:                      #SINGLE LEVEL INHERITANCE
#     @staticmethod
#     def start():
#         print("Car started")

#     @staticmethod
#     def stop():
#         print("Car stopped")

# class ToyotaCar(Car):
#     def __init__(self,name):
#         self.name = name

# c1 = ToyotaCar("Fortuner")
# print(c1.name)
# print(c1.start())


# class Car:                      #MULTI LEVEL INHERITANCE
#     @staticmethod
#     def start():
#         print("Car started")

#     @staticmethod
#     def stop():
#         print("Car stopped")

# class ToyotaCar(Car):
#     def __init__(self,brand):
#         self.brand = brand

# class Fortuner(ToyotaCar):
#     def __init__(self,type):
#         self.type = type

# c1 = Fortuner("petrol")
# print(c1.type)
# print(c1.start())


# class A:                            #MULTIPLE INHERITANCE
#     varA = "Welcome to class A"

# class B:
#     varB = "Welcome to class B"

# class C(A,B):
#     varC = "Welcome to class C"

# c1 = C()
# print(c1.varC)
# print(c1.varB)
# print(c1.varA)


class Car:         

    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")

class ToyotaCar(Car):
    def __init__(self,name,type):
        self.name = name
        super().__init__(type)

c1 = ToyotaCar("Fortuner","electric")
print(c1.name)
print(c1.type)
print(c1.start())
