
idx=34
print(idx%10)

import random

# Assuming args.num_users is defined and is an integer
num_users = 100
half_num_users = num_users // 2

# Randomly select half of the elements from the range
selected_users = random.sample(range(num_users), half_num_users)

# Now selected_users contains the random half of elements from the range
print(len(selected_users))


print(100 //1.1)