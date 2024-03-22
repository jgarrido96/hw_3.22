
# Hey look it's how to push a file to github
# git add .
# git commit -m
# git push -u origin main

# adding special characters to our strings
# backslah "escapes character"

print("Hello \nthere!")#line break
print("Hello \tThere!")#tab over
print("This is a backslash: \\")# this types out one backslash.
# You can use this to do this to any thing, including a " or anything else that might need to be specified

print("I called the doctor yesterday and he told me \"You need to stretch more\"")

# string Concatenation
greeting = "Hello there."
name = "General Kenobi"
print(f"{greeting} \n {name}")
print('\n')
# concatenating user_input
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
full_name = first_name + " " + last_name
print("Hello", full_name +"!")

jedi_master = "Obi-Wan"
jedi = "Anakin"
jedi_elder = "Yoda"
print(f"List of generals in the clone wars: \n {jedi_master}, {jedi}, {jedi_elder}")

age = 27
print(name + " is " + str(age) + " years old.")

#customize your printed messages
print("apple", "cherry", "banana", sep="-")# sep separates things with whatever you put in there
print("This is just the beginning, ", end = "child.")# end moves to the next print maybe??
print(" The end only comes by my hand.")
