

# for variable in range(start, end, step) :
#     code to loop

# range(start, end, step) where start, end, step are numbers [ ex. range(1, 5, 2) ]
# From start to end-1(end not included), put the increased/decreased value by step into a variable and loop.
# Don't necessarily have to enter the start and step.
# If start is not entered, 0
# If step is not entered, 1
# range(5)          => start and step not entered
# range(0,5)        => step not entered
# range(0, 5, 1)    => standard


# for i in range(0, 5, 1) :   # repeats 5 times with i taking values 0, 1, 2, 3, 4
#     print(i)                # use variable in the repeated code

# for i in range(0, 5, 1) :
#     print('hello')      # do not use variable in the repeated code


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Print odd number from 1 to 100

# for i in range(1,100,2):
#     print(i)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Print multiples of 5 from 5 to 100

# for i in range(5, 101, 5):
#     print(i)


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Print perfect squares up to 10000 (print(x*x))

# for i in range(1, 101, 1 ):
# #     print(i*i)                # This is for perfect squares (1*1, 2*2, ...)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# while loop
# while (condition) :
#       code
# Used in this format
# Similar to if statements, executes if the condition is True

# i = 0
# while(i < 5) :
#     print(i)
#     i += 1         # i = i + 1, increment i


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# Print an even number from 1 to 100

# i = 2
# while (i < 101) :
#     print(i)
#     i += 2

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# Print multiples of 7 from 7 to 100

# i = 7
# while (i < 100) :
#     print(i)
#     i += 7

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# Print fractions from 1 to 100

# i = 1

# while (i < 101):
#     print(1/i)
#     i+=1

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# Infinite loop
# while (True) :
#       code
# This creates an infinite loop

# continue and break
# continue and break can be used in both for and while loops

# continue
# When continue is encountered, the loop moves to the next iteration

# for i in range(0, 10, 1) :
#     if(i % 2 == 0) :
#         continue        # skip even numbers
#     print(i)

# break
# When break is encountered, the loop stops
# break is usually used with if

# i = 0
# while(True) :
#     print(i)
#     if(i == 10) :
#         break
#     i += 1


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# Sample of using infinite loop, continue, break

while(True) :
    print("Please choose a menu option!")
    print("1. Print hello")
    print("2. Print hi")
    print("3. Exit")
    menu = int(input())

    if(menu == 1) :
        print("hello")
    elif(menu == 2) :
        print("hi")
    elif(menu == 3) :
        print("Exiting the menu program.")
        break
    else :
        print("Invalid input. Please enter a number between 1 and 3.")
        print()
        print()
        continue

    print()
    print()