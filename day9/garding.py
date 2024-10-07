prog_dict = {
    "bug": "hello",
    "function": "goodbye"
}

print(prog_dict)

prog_dict["bug"] = "goodbye too"
print(prog_dict)

empty_dict = {}

#wipe an existing dictionary

# prog_dict = {}
# print(prog_dict)

#edit an item in a dictionary
prog_dict["bug"] = "a moth in your compuer"

#loop through a dictionary
for key in prog_dict:
    print(key)
    print(prog_dict[key])