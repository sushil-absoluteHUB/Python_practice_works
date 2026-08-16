# class Person:
#     age = 25
#     def displayInfo(Self):
#         print("hello i am reading python")
#     def displayInfo1(Self):
#         print("i am complet my course")    
# person1 = Person()
# person2 = Person()
# person1.displayInfo()
# person2.displayInfo1()
# print(person1.age)
# print(person2.age)

# #------------------------------->
# """
# MINIMAL OOPS PROGRAM FOR ADDITION USING LAMBDA
# """

# class Addition:
#     def __init__(self):
#         # Lambda for addition
#         self.add = lambda x, y: x + y
    
#     def calculate(self, a, b):
#         result = self.add(a, b)
#         print(f"{a} + {b} = {result}")
#         return result

# # Test the program
# if __name__ == "__main__":
#     print("=== SIMPLE ADDITION ===")
    
#     # Create object
#     calc = Addition()
    
#     # Perform additions
#     calc.calculate(5, 3)      # Output: 5 + 3 = 8
#     calc.calculate(10, 20)    # Output: 10 + 20 = 30
#     calc.calculate(100, 50)   # Output: 100 + 50 = 150
#     calc.calculate(7.5, 2.5)  # Output: 7.5 + 2.5 = 10.0


# #------------------------------------------------------------->
# class Student:
#     num = 20
#     def __init__(self):
#         print("print constructor ")
#     def displayInfo(self):
#         print("number is correct")    
# obj = Student()
# obj.displayInfo()
# print(obj.num)        
# #------------------------------------------->

# from os import name


# class Person:
#     # no need to write global value

#     def ___init__(self, name, age):
#         self.name = "name"
#         self.age = "age"
#         print(f"person object created for {self.name}!")
#     def greet(self):
#         print(f"Hello! my name is {self.name} and i am {self.age}year old")    

# person1 = Person("SUSHIL",32)
# person1.greet()
# #----------------------------------->
# class Car:
#     def __init__(self, colour,brand):
#         self.colour = colour
#         self.brand = brand
#         print(f"creat a car whose {self.colour}and {self.brand} !")
#     def greet(self):
#         print(f"hello !: this is best {self.colour} colour and i like this {self.brand}")    
# car1 = Car("black" , "BMW")       
# car2 = Car("red", "ford") 
# car1.greet()
# car2.greet()
# #--------------------------->constructor in oops hels like ATM pin set
# class ATM:
#     def __init__(self,pin):
#         self.pin = pin
# user1 = ATM(3590)
# user2 = ATM(1234)
# print(user1.pin)
# print(user2.pin)
# #--------------> bonus calculation
# class Employees:

#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def bonus(self, percentage):
#         bonus_amount = (self.salary * percentage) / 100
#         return bonus_amount


# emp = Employees("sushil", 50000)
# print("employee name: ", emp.name)
# print("base salary :", emp.salary)
# result = emp.bonus(10)
# print("bonus :", result)
# #-------------------------->
# class Cat:
#     def sound(self):
#         print("maow")
# class Dog:        
#     def sound(self):
#         print("bark") 
# for animal in (Cat(),Dog()):
#  animal.sound()
# #-----------------------> 
# class Credit_card:
#     def pay(self):
#         print("payment through creditcard :-->")
# class UPI:
#     def pay(self):
#         print("payment through UPI :-->")
# class ATM:
#     def pay(self):
#         print("payment through ATM :-->")
# amount_send =[Credit_card(), UPI(),ATM()]
# for receive in amount_send:
#     receive.pay()                
# #------------------------->
# class ATM :
#     def __init__(self):
#         self.__balance = 1000
#     def withdrow(self, amt):
#         if amt <= self.__balance:
#             self.__balance -= amt
#     def show_balance(self):
#         return self.__balance       
# obj = ATM()
# obj.withdrow(500)
# print(obj.show_balance())
# #------------------------------------>
# class Account:
#     def __init__(self):
#         self.__total_V = 500000
#     def trns_frind(self,amt):
#         self.__total_V -= amt
#     def show_balance(self):
#         return self.__total_V
# remain = Account()
# remain.trns_frind(100000)
# print(remain.show_balance())

# #--------------------------------->
# class BankLogin:
#     def __init__(self):
#         self.__password = "abc123"
#     def login(self, enter_password):
#         if enter_password == self.__password:
#             print("login succesfully") 
#         else:
#             print("Invalid password")
# user = BankLogin()
# user.login("abc123")
#user.login("xyz")                   
#----------------------------> Analog time project
# import turtle
# import time

# wn = turtle.Screen()
# wn.title("Analog Clock")
# wn.bgcolor("black")

# clock = turtle.Turtle()
# clock.hideturtle()
# clock.pensize(3)

# def draw_clock():
#     clock.clear()
#     #draw circle
#     clock.color("white")
#     clock.circle(100)
#     #get current time
#     now = time.localtime()
#     sec = now.tm_sec
#     min = now.tm_min
#     hour = now.tm_hour % 12

#     # calculate angle
#     sec_angle = sec * 6
#     min_angle = min *6 + sec * 0.1
#     hour_angle = hour * 30 + min * 0.5

#     #draw hands
#     draw_hand(sec_angle, 180 , "red",2, 1)
#     draw_hand(min_angle, 160 , "green", 5, 2)
#     draw_hand(hour_angle , 100 , "blue",5, 3)
# def draw_hand(angle, length, color, width, pensize):    
#     clock.color(color)
#     clock.width(width)
#     clock.pendown()
#     clock.goto(0 , 0)
#     clock.setheading(9 - angle)
#     clock.forward(length)
#     clock.penup()
# while True:
#     draw_clock()
#     time.sleep(1)    
#-------------------------> find missing number

def find_missing(arr , n):
    total = n *(n+1)//2
    arr_sum = sum(arr)
    return total - arr_sum

print(find_missing([1,2,4,5],5))
#------------------------------>
