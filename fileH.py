# file = open("my.txt")
# content = file.read()
# print(content)
# file.close()
#------------------------------>
# file = open("my.txt", 'r')
# line1 = file.readline()
# print(line1)
# line2 = file.readline()
# print(line2)
# file.close()

#---------------------->
# file = open("my.txt", "w")
# file.write("I am confident on to clear my interview.\n")
# file.close()
#--------------------------->
# file = open("my.txt","a")
# file.write("I give my full effort regading of interview Q. \n")
# file.close()
          
#------------------------->
# file = open("my.txt" , "w")
# file.write("Iam learning python.\n")
# file.write("I try to grabs all knowledge.\n")
# file.write("I want to deep knowledge regarding AI an N8N.\n")
# file.close()
# --------------------------->
# try:
#      with open("my.txt", "r") as file:
#       content = file.read()
# except FileFoundError:
#    print("file not found.")
 #----------------------------------->
# sushil
#-------------------------------> write user input to file
# name = input("Enter your name: ")
# age = input("Enter your age :")
# with open("my2.txt", "w") as file:
#  file.write(f"Name :{name}\n")
#  file.write(f"Age : {age}\n")
# file.close()
#------------------------------------>

#-------------------------------------->
# with open("my.txt", "r") as file:
#        line = file.readline()
#        while line:
#              print(line.strip())
#              line = file.readline() 
#-------------------------------->Write a Python program to read a text file line by line and display each line
# with open("my.txt", "r") as file:
#     for line in file:
#         print(line.strip())
#--------------------------------->Write a Python program to  text copy content from one file to another. 
# with open("my.txt", "r") as scr , open("my2.txt", "a") as dst :
#     content = scr.read()
#     dst.write(content)
#---------------------------->Write a Python program to count the number of lines, words, and characters in a file. 
