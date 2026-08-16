# value =[1,3,2,4,"sushil",9.5, True, False, None] # inserting values in list
# print(value[4])                                  # "sushil"
# print(value[2:7])                                # [2, 4, 'sushil', 9.5, True]
# #---------------------> using slicing methodwe can isert value in list
# value[2:7] =[10, 20, 30]                         #[1, 3, 10, 20, 30, False, None]
# print(value)                                      
#  # ----------------------> using slicing methodwe can delete value in list
# my_list = [1, 2, 3,"sushil", 4, 5, "academy", 6, 7]
# my_list[3:4] = ["victot"]
# print(my_list)                                      # [1, 2, 3, 'victot', 4, 5, 'academy', 6, 7]
# #-------------------------> 
# x = 10
# name = "sushil"
# my_value = True
# y = 9.5
# print(x, type(x))
# print(name, type(name))
# print(my_value, type(my_value))
# print(y,type(y))
# #----------------------------->
# name = "sushil"
# age = 32
# country = "INDIA"
# print(f"my name is {name} and my age is {age} and i am live in {country}")
# #--------------------------------->

# name = "vector"
# age = 30 
# country = "turkey"
# profession = "software engineer"
# print(f" my name is {name} and my age is {age} and is belongs to {country} and my profession is {profession}")

# #------------------------------------>
# a = 10
# b = 3.5
# c = (a +b)
# print(c)
# #----------------------->
# name = "sushil"
# print(name + " is a good boy")
# print(name[1:])
# print(name[:2])
# print(name[1:5])
# new_name = "Z" + name[1:]
# print(new_name)


# #-------------------------->
# name = " sushil"        # horizontaly name printed
# print(name * 6)
# new_name = name * 6
# print(new_name) 
# #------------------------>
# name = ["sushil"]      # verticaly name printed
# new_name = name * 6
# for char in new_name:
#     print(char)
# #-------------------->
# fruit =["apple", "banana", "mango", "grapes", "orange"]
# fruit[1] = "pinapple"
# print(fruit)
# #---------------------->
# fruit =["apple", "banana", "mango", "grapes", "orange"]
# fruit.append("kiwi")  
# fruit.insert(2, "watermelon")
# fruit.remove("grapes")
# print(fruit)

# #---------------------------->
# value =( 2, 6 , "raju",9.5,True)
# print(value)
# print(value[2])              # "raju"
# print(value.remove("raju"))  # This will raise an error because tuples are immutable
# print(value[2:4])            # (9.5, True)

# #--------------------------------->
# student = {"name": "sushil", "age": 32, "course": "PYTHON"}
# print(student)
# new_add = student.update({"country": "INDIA"})
# print(student)

# #-------------------------------->
# value = {2,2,5,5,4,4,6,6,3,3,1,1}
# print(value)

# value1 = [25,25,10,10,80,36,36,45,45,90,90]
# print(sorted(set(value1))) 
# #-------------------------------->

# name = input("my name is: ")
# age = int(input("my age is: "))
# print(f"hello {name} you are {age} year old")
# print(type(name), type(age))
# #-------------------------------->

# name = ["sushil", "victor","debrath" , "reetika"]
# age = [32, 30, 28, 25]
# country = ["INDIA", "TURKEY", "USA", "UK"]
# student_info = dict(zip(name, age))
# print(student_info)
# #---------------------------->
# student_info = dict(zip(country, zip(age, name)))
# print(student_info)

# #----------------------------->

# my_list = [
#     {"name": "sushil", "age": 32 , "country": "INDIA"},
#     {"name": "victor", "age": 30, "country": "TURKEY"},
#     {"name": "debrath", "age": 28, "country": "USA"},
#     {"name": "reetika", "age": 25, "country": "UK"}
# ]
# print("Students whose age is greater than 27: ")
# for student in my_list:
#     if student["age"] > 27:
#         print(student["name"])
#         print(student["name"], ":", student["country"])
#         print(student["name"], ":", student["age"], ":", student["country"])
# ---------------------------------------------------------------------------->



