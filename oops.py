# class Student:
#     college_name = "Arka Jain University"
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
    
#     def welcome(self):
#         print("Welcome!!!,",self.name)        

#     def get_marks(self):
#         print("Marks =",self.marks)    

# s1 = Student("Aayat",80)
# s1.welcome()
# s1.get_marks()


# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks

#     @staticmethod
#     def hello():
#         print("Hello!!!")

#     def average(self):
#         sum = 0
#         for i in self.marks:
#             sum+=i
#         print("Average = ",sum/3)

# s1 = Student("Aayat",[75,90,85])
# s1.average()
# s1.hello()


class Account:
    def __init__(self,bal,acc):
        self.bal = bal
        self.acc = acc

    def debit(self,amt):
        self.bal -= amt
        print("Rs.",amt,"debited")

    def credit(self,amt):
        self.bal += amt
        print("Rs.",amt,"credited")

    def print_bal(self):
        print("Remaining Balance = Rs.",self.bal)

acc1 = Account(15000,555)
acc1.debit(5000)
acc1.print_bal()
