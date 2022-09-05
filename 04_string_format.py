name, age, email = "Robert", 30, "robert@gmail.com"

# cast an int type to a string type: str(age)
print(
    "My name is " + name + ". I'm " + str(age) + " years old. My email is " + email
)

# formated string: f
# only from python 3.6 <
print(f"My name is {name}. I'm {age} years old. My email is {email}")

# this is compatible with python 2.7
print("My name is {}. I'm {} years old. My email is {}".format(name, age, email))