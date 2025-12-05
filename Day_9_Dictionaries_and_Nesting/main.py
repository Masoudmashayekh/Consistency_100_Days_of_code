# Dictionaries & Nesting

# Welcome to the secret auction program.
# What is your name?:
# What's your bid?:
# Are there any other bidders? Type 'yes' or 'no'.
# The winner is {name} with a bid of $121.
# {"Code": "program instructions"}
# {Key: Value}

all_bids = {}
print("Welcome to the secret auction program.")
repeat = True
while repeat:
    your_name = input("What is your name? ")
    your_bid = input("What is your bid? $")
    all_bids[your_name] = your_bid 
    repeat_q = input("Are there any other bidders? Type 'yes' or 'no'").lower()
    if repeat_q == "no":
        repeat = False
        final_dic = {"name": "", "price": "0"}
        for key in all_bids:
            if int(all_bids[key]) > int(final_dic["price"]):
                final_dic["name"] = key
                final_dic["price"] = all_bids[key]
        print(f"The winner is {final_dic['name'].capitalize()} with a bid of ${final_dic['price']}.")
    else:
        print("\n" * 10)

                
            



 