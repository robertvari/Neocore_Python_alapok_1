#                0          1       2         3          4
my_friends = ["Robert", "Csaba", "Norbi", "Kriszta", "Csilla", "Norbi"]
#                 -5       -4       -3        -2        -1

print(my_friends)
print(len(my_friends))

print(my_friends[3])
print(my_friends[-1])

print(my_friends[ len(my_friends)//2 ])

# add tiem
my_friends.append("Johny")
my_friends.insert(0, "Tom")
print(my_friends)

# remove item from list
del my_friends[0]
print(my_friends)

my_friends.remove("Norbi")
print(my_friends)

# edit/replace item in list
my_friends[1] = "Reni"
print(my_friends)

# add two list together
numbers = [1, 2, 3, 4]
my_friends.extend(numbers)

print(my_friends)
print(my_friends + numbers)