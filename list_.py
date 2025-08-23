

# variable = ["value", value]       => The data type of the value does not matter
# Use in the above form
# List is a collection of multiple data types in order in one variable.
# The order of values starts from 0 => It is called the index number.
# When bringing in list values, refer to them using []

# list1 = [1, 'cit', True]
# print(list1)
# print(list1[0])         # Get list1 index number 0 value
# print(list1[2])
# print(list1[3])         # Get list1 index number 3 value. There is index number 3, so an error occurs


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# You can use the index number to modify the value at that index number.
# Changning the value can be done as if saving the value in a variable.
# a = [1, 'cit', True]
# print(a)

# a[1] = "hello"  # Change the value of the index number 1 of a.
# print(a)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# list1 = ["abc", "dfg", "hji", 123, 456 ]
# print(list1)
# print()

# print("Q1. Change the 1st element of list1 to 'park'.")
# list1[1] = 'park'
# print(list1)
# print()

# print("Q2. Name the variable 'arr' and save the list below.")
# arr = [4, 8, 12, 16, 20, 24, 28, 32]
# print(arr)
# print()

# print("Q3. Change the 4th element of arr to 'cit'.")
# arr[4] = 'cit'
# print(arr)
# print()

# print("Q4. Run print(list1) and print(arr).")
# print(list1)
# print(arr)
# print()

      
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# for i in range(1, 9, 2):
#     print(i)
# print()

# list1 = [1, 3, 5, 7]    # Can insert a list variable instead of range() in for loop
# for i in list1:
#     print(i)            # Get the elements of a list one by one
# print()

# list2 = ['a', 'hello', 'cit', 'coding', 'A']
# for j in list2 :
#     print(j)
# print()


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# name = ['Oliver', 'Jack', 'Harry', 'Noah' ]
# score = [ 92, 96, 98, 100] 

# average = score[0]+ score[1]+ score[2]+ score[3]
# total = average/4

# print("The average is", total, "and Noah has the highest score.")

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #

# List function

# listName.insert(Index number, Value to add)
# insert() add one value to index number. If there is a value that index, the values are pushed back.
# If index number is out of range, the value is insert to the end.

# listName.append(Value to add)
# appened() add one value append to the end.

# del(listName[Index number])
# In the case of del(), the value at the index number of the list deleted,
# and if there is an index number after it, it is pulled forward.
# If index number is out of range, an error occurs.

# listName. remove(Value to remove)
# In the case of remove(), the value to be deleted is found in the list and deleted.
# If there is an index number after it, it is pulled forward.
# If the value to be deleted is not in the list, an error occurs.

# listName.index(Value to find index)
# In the case of index(), the index number where the value is located is returned.
# If the value to find is not in the list, an error occurs.
# If there are multiple values in the list, the number with the lowest index is returned.

# len(listName)
# In the case of len(), the length of the listName is returned.
# (It is different from the index, the last number of the index is the value -1 of len(listName))

# sum(listName)
# In the case of sum(), it returns after adding all the values in the listName.
# (Available only when the list data types are numeric.)
# If the data types in the list are mixed with str and numbers, an error occurs.

# listName.count(Value to counter)
# In the case of count(), it returns how many values are in the list.
# 0 if the value to be counted is not in list.

# listName.sort()
# Sort the contents of the list in ascending order.

# Functions like insert() that are used with a list variable followed by a dot(.) can only be used with lists.
# Functions like del(), len(), and sum() can be used with other data types as well, not just lists.


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


list0 = []
print(list0)
print()

print("Q1. Use the append() function to add 1, 2, 3, 4, 5, 6, 7, 8 and 9 to list0 in order. (You can also use a loop statement.)")
# list0.append(1)
# list0.append(2)
# list0.append(3)
# list0.append(4)
# list0.append(5)
# list0.append(6)
# list0.append(7)
# list0.append(8)
# list0.append(9)

for i in range(1, 10, 1):
    list0.append(i)
print(list0)
print()

print("Q2. Add 0 to the 0th position of list0 using the insert() function.")
list0.insert(0, 0)      # insert = Index number, Value to add
print(list0)
print()

print("Q3. Delete the 3rd element of list0 using the del() function.")
del(list0[3])
print(list0)
print()

print("Q4. Delete the 5th element of list0 using the del() function.")
del(list0[5])
print(list0)
print()

print("Q5. Remove 1 from list list0 using the remove() function.")


