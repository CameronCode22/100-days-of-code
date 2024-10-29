capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nested list in dictionary

# travel_log ={
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }

# print(travel_log)
# print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])


#list nested inside a dictionary
travel_log ={
    "France": {
        "num_times_visited": 8,
        "cities_visited": ["Paris", "Lille", "Dijon"] 
    },
    "Germany": ["Stuttgart", "Berlin"],
}

print(travel_log["France"]["cities_visited"][0])

#Append is only for adding to lists not dictionaries


starting_dictionary = {
    "a": 9,
    "b": 8,
}

starting_dictionary["c"] = 7
final_dictionary = starting_dictionary
print(final_dictionary)