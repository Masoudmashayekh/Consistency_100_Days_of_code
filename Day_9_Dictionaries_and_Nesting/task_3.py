# Nesting
# {
# key: [list],
# key2: {Dict}
# }

travel_log ={
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

travel_log_dic ={
    "France": {
        "num_times_visited": 8,
        "cities_visited": ["Paris", "Lille", "Dijon"]
    },
    "Germany": {
        "num_times_visited": 2,
        "cities_visited": ["Stuttgart", "Berlin"]
    }
}

print(travel_log_dic["France"]["cities_visited"][2])
