bid_dict = {
    "james": 345,
    "bob": 20
}

bid_dict["sam"] = 49

pregunta = True
while(pregunta == True):
    name = input("What is your name?: ")
    bid = int(input("what's your bid?: "))

    bid_dict[name] = bid

    next_pers = input("Is there a next person that would like to bid (yes or no)")
    if next_pers.lower() == "no":
        pregunta = False

    print(bid_dict)

highest_bid = {"name": "", "bid": 0}
for key in bid_dict:
    if (bid_dict[key] > highest_bid["bid"]):
        highest_bid["name"] = key
        highest_bid["bid"] = bid_dict[key]


print(f" The highest bid is {highest_bid['bid']} by {highest_bid['name']}")