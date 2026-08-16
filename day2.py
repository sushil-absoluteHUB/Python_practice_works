# #------------------> uppercase and lowercase
# test = "Data Vector Comes hear tO plaYA"

# def cout_case(test):
#     result ={
#         "uppercase": 0,
#         "lowercase": 0

#     }
#     for i in test:
#         if i.isupper():
#             result["uppercase"] += 1
#         elif i.islower():
#             result["lowercase"] +=1
#     return result

# print(cout_case(test))    
#------------------------------------>creat list of no- 1 to 10 .create dictionary values of those no be square.

# number = [1,2,3,4,5,6,]

# result ={}

# for value in number:
#     result[value] = value ** 2
# print(result)
#-----------------------------------> get cube value in dictionory fprmate key : values 
# num = [1,2,3,4,5,6]
# result ={}
# for cub in num:
#     result[cub] = cub ** 3
# print(result)    

#------------------------------------------> check weater number is + - 0
# number = 0

# if number > 0:
#     print("Positive number")
# elif number<0:
#     print("Negative number")
# else:
#     print("Zero")
#----------------------------------------->
# age = 21
# if age >= 21:
#     print("eligible for voting")
# else:
#     print("not eligible for voting")
#--------------------------------------------------> determine leap year or not
# year = 2026

# Method 1: Nested if-else
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not a leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not a leap year")

# Method 2: Compound condition (cleaner)
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap year")
# else:
#     print("Not a leap year")

# #---------------------------------------------->    login validation
# username = "admin"
# password = "secret123"
# entered_user = "admin"
# entered_pass = "secret123"

# if entered_user == username and entered_pass == password:
#     print("Login successful")
# elif entered_user != username and entered_pass != password:
#     print("Both username and password are incorrect")
# elif entered_user != username:
#     print("Username incorrect")
# else:
#     print("Password incorrect")
# #------------------------------------> Email validation
# email = "user@example.com"

# if "@" in email and "." in email:
#     at_index = email.index("@")
#     dot_index = email.rindex(".")
    
#     if at_index > 0 and dot_index > at_index + 1:
#         if dot_index < len(email) - 1:
#             print("Valid email format")
#         else:
#             print("Invalid: no domain extension")
#     else:
#         print("Invalid: incorrect @ or . position")
# else:
#     print("Invalid: missing @ or .")

# # Better: Use regex for real-world validation
# import re
# if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
#     print("Valid email")
# #-------------------------------------------> turnary operator
# age =17

# Traditional if-else
# if age >= 18:
#     status = "Adult"
# else:
#     status = "Minor"

# Ternary operator (one-liner)
# status = "Adult" if age >= 18 else "Minor"
# print(status)

# Nested ternary (avoid)
#category = "Child" if age < 13 else "Teen" if age < 18 else "Adult"
#print(category)

# #------------------------------------------->discount calculation
# amount = 2400

# if amount >= 5000:
#     discount = 0.20  # 20%
# elif amount >= 2000:
#     discount = 0.15  # 15%
# elif amount >= 1000:
#     discount = 0.10  # 10%
# elif amount >= 500:
#     discount = 0.05  # 5%
# else:
#     discount = 0  # no discount

# final_price = amount * (1 - discount)
# print(f"Original: ₹{amount}")
# print(f"Discount: {discount*100}%")
# print(f"Final: ₹{final_price}")
#----------------------------------------------># determine  secand largest no !
# nums = [10, 20,30,4,69,19]

# largest = 0
# secand_largest = 0

# for num in nums:
#     if num > largest:
#         secand_largest = largest
#         largest = num
#     elif num > secand_largest and num != largest:
#         secand_largest = nums
# print(secand_largest)        

#--------------------------------------------------->merge to dictionory
# dict1 = {"a": 1, "b": 2}
# dict2 = {"c": 3, "d": 4}

# dict1.update(dict2)
# print(dict1)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# ---------------------------------->
# dict1 = {"name": "victor", "age":28}
# dict2 = {"name":"sushil" , "age":32}
# merged = {}
# for key in dict1.keys():
#     merged[key] = [dict1[key], dict2[key]]
# print(merged)
# #------------------>
# dict1 = {"name": "Sushil", "role": "QA Engineer"}
# dict2 = {"experience": 2, "projects": 5}

# merged = dict1 | dict2                           
# print(merged)

# dict1.update(dict2)
# print(dict1)
# Output: {'name': 'Sushil', 'role': 'QA Engineer', 'experience': 2, 'projects': 5}
# ------------------------------->
# dict1 = [{"name": "Sushil", "age": 28}]
# dict2 = [{"name": "victor", "age" :32}]
# merged = dict1 + dict2
# print(merged)