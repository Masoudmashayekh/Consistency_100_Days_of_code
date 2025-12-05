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



 