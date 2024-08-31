print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want? S, M or L")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N")

total_bill = 0

#how much to pay based on size
if size == "S":
    total_bill += 15
elif size == "M":
    total_bill += 20
elif size == "L":
    total_bill += 25

#how much to pay based on pepperoni
if pepperoni == "Y" and size == "s":
    total_bill += 2
if pepperoni == "Y" and size == "M" or size == "L":
    total_bill += 3

#final amount with extar cheese
if extra_cheese == "Y":
    total_bill += 1

print(f"your total bill is ${total_bill}")