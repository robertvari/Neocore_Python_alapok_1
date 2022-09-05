names = ["Csaba", "Csilla", "Tamás", "Róbert"]

for i in names:
    print(i)

# break loop
for i in names:
    if i == "Tamás":
        break
    print(i)

# continue (skip item)
for i in names:
    if i == "Tamás":
        continue
    print(i)