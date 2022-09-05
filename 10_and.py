username = "robert"
password = "testpas123"

user_name = input("username?")
user_password = input("password?")

#           True                     True
if username == user_name and password == user_password:
    print(f"Wellcome back {username}.")
else:
    print("username or password was invalid. :(")