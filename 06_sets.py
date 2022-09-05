A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# add items
A.add(10)
print(A)

A.update([20, 30, 40, 50])
print(A)

# remove items from set
A.discard(10)  # ignores nonexisting item
A.remove(20)  # error if item not exists
print(A)

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# union: |
print(A | B)

# intersection: &
print(A & B)

# Symmetrical differenc
print(A ^ B)