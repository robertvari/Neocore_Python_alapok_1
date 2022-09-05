phonebook = {
#       root key                      value
    "06 20 123 4567": {"name": "Robert", "address": "Budapest"},
    "06 20 123 4568": {"name": "Csaba", "address": "Pécs"},
    "06 20 123 4569": {"name": "Kriszta", "address": "Debrecen"},
}

print(phonebook["06 20 123 4568"]["name"])

# add new addres to dictionary
phonebook["06 20 123 4570"] = {"name": "Tamás", "address": "Zamárdi"}

# override item in dictionary
phonebook["06 20 123 4569"] = {"name": "Csilla", "address": "Debrecen"}
phonebook["06 20 123 4569"]["name"] = "Johny"

# remove data from dictionary
del phonebook["06 20 123 4570"]

pass