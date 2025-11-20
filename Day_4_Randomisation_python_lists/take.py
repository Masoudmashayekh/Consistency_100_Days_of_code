friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

import random
friends_len = len(friends)
random_friends = random.randint(0, friends_len - 1)
print(friends[random_friends])