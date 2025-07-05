

# Comparison operators
# The result of the comparison operation is always True or False.
# ==    :   (equal to)
#           True if the same, False if different.

# !=    :   (not equal)
#           True if different, False if the same

# <     :   (less than)
#           True if the right side is larger (excluding equal values), otherwise return False.

# >     :   (greater than)
#       True if the left side is larger or equal, otherwise return False.

# <=    :   (less than or equal to)
#           True if the right side is larger or equal, otherwise return False.

# >=    :   (greater than or equal to)
#           True if the left side is larger or equal, otherwise return False.

# print(5 != 2)
# print(5 < 2)



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# if(condition) :
#   Run if the above condition is True.
# elif(condition) :
#   Run if all condition is True.
# else :
#   Run if all condition are False.

# if    : always use 1
# elif  : use range 0 - infinity
# else  : use 0 or 1
# if can be used by nesting within if.


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# 100 - 90  : A
# 89 - 70   : B
# 69 - 60   : C
# 59 - 50    : D
# 49 - 0    : F

# score = int (input())

# if(100 >= score >= 90):
#     print('A')
# elif(89 >= score >= 70):
#     print('B')
# elif(69 >= score >= 60):
#     print('C')
# elif(59 >= score >= 50):
#     print('D')
# elif(49 >= score >= 0):
#     print('F')

# print("End")


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# # One code
# print("Enter your age.")
# age = int(input())

# if(age >= 12):
#     print("Good, have fun watching.")
# elif(12 > age):
#     print("Sorry, only 12 years and over can watch the movie.")


# # Teacher code
# age = int(input("Enter your age: "))        # Do this to put input on the same line as print

# if(age >= 12) :
#     print("Good, have fun watching.")
# else :
#     print("Sorry, only over 12 years can watch the movie.")


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# print("Enter number.")
# number = int(input())

# if(number%2== 1):
#     print("Odd.")
# elif(number%2==0):
#     print("Even.")


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# not   : If True, the result is reversed to False. If it is False, the result is reversed to True.
# and   : True if both sides are True, False if even one side is False.
# or    : False if both sides are False, True if at least one side is True
# The execution order is executed in the order of not, and, or.

# a = 10
# b = 2

# if((a == 10) and (b == 2)):
#     print("a is 10, and b is 2.")

# if ((a == 10) and (b == 2)):
#     print("At least one of a or b is 10.")

# if(not(a == 5)):                #same as a != 5
#     print("a is not 5.")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Nested if
# # You can nest if statements


age = int(input("Enter your age: "))
is_member = input("Are you a member? (yes or no):")

if (age >= 18):
    print("Hello, member.")

    if(is_member == "yes"):
        print("Adult member, welcome!")
    else:
        print("Adult non-member, please sign up.")
else:
    if(is_member == "yes"):
        print("Teen member, welcome!")
    else:
        print("Teen non-member, please sign up.")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# print("Enter two numbers.")

# a = int(input())
# b = int(input())

# print("What calculation do you want to run? (1: Multiply, 2: Divide, 3: Add, 4: Subtract)")
# c = int(input())

# if(c == 1):
#     print("Selected multiply", a, "*", b, "=", a*b)
# if(c == 2):
#     print("Selected divide", a, "/", b, "=", a//b)
# if(c == 3):
#     print("Selected add", a, "+", b, "=", a+b)
# if(c == 4):
#     print("Selected subtract", a, "-", b, "=", a-b)


