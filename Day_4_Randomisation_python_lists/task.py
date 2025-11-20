friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

import random
# Option 1
friends_len = len(friends)
random_friends = random.randint(0, friends_len - 1)
print(friends[random_friends])

# Option 2
print(random.choice(friends))