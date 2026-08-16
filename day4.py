# while looping in python
#-------------------------->Print numbers from 1 to 10 using a while loop.
# num = 1 
# while num <= 10:
#     print(num)
#     num += 1
#-----------------> onliner while loop to print numbers from 1 to 10
# 
#---------------------------------->Find the first even number between 1 and 10 using a
# num = 4
# while num <= 10:
#     if num  % 2 == 0:
#         print("The first even number is:" ,num)
#         break
#-------------------------------->Skip all odd numbers between 1 and 10 and print only
#even numbers using continue.    
# num = 1 
# while num <= 10:
#     if num % 2 != 0:
#         num += 1
#         continue
#     print(num)
#     num += 1
#-----------------------> calculate the factorial of a number using a while loop.
# num = 3
# factorial = 1
# while num > 0:
#     factorial *= num
#     num -= 1
# print(f"The factorial of the number is: {factorial}")
#------------------------>reverses a given number using a while loop.
# num = 12345
# reverse = 0
# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num //= 10
#     print(f"reversed number is: {reverse}")
#------------------------> reverse number using list
# num = [1, 2, 3, 4, 5]
# result =num[::-1]
# print(f"reversed number is: {result}")
#------------------------------------------>
# Sum digits until single digit
# num = 654

# while num >= 10:  # Keep looping until num is a single digit
#     digit_sum = 0
#     while num > 0:
#         digit_sum += num % 10   # Add last digit
#         num //= 10              # Remove last digit
#     num = digit_sum             # Update num with the sum

# print("Single digit sum:", num)
#-------------------------------------------->Fibonacci series up to 10 terms using while loop

# n_terms = 10   # number of terms
# count = 0
# a, b = 0, 1

# while count < n_terms:
#     print(a, end=" ")
#     a, b = b, a + b
#     count += 1
# --------------------> 
# fab_term = 11
# count = 0 
# a , b = 0 , 1
# while count < fab_term:
#     print(a , end=" ")
#     a,b = b , a+b
#     count += 1
#--------------------------->Print all prime numbers between 1 and 20 using nested
#while loops.

# Print prime numbers between 1 and 20 using nested while loops

# num = 2   # start from 2 since 1 is not prime

# while num <= 20:
#     is_prime = True
#     divisor = 2
    
#     # check divisibility using inner loop
#     while divisor < num:
#         if num % divisor == 0:
#             is_prime = False
#             break
#         divisor += 1
    
#     if is_prime:
#         print(num, end=" ")
    
#     num += 1

#------------------------------>
# for i in range(-4 ,5 , 2):
#     print("loop run:", i)
# ------------------------------->
# name = "python"
# for letter in name:
#     print(letter)
#----------------------------->
# name = "python"
# for letter in name:
#    print(letter)         # verticaly prunt "python"
#    print(letter, end="") # horizontal print "python"
#----------------------->

