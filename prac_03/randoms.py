import random

print(random.randint(5, 20))  # line 1
# Smallest number was 5
# Largest number was 20
print(random.randrange(3, 10, 2))  # line 2
# Smallest number was 3
# Largest number was 9
# Throughout the multiple runs, line 2 never produced 4
print(random.uniform(2.5, 5.5))  # line 3
# Smallest number was 2.8731295122839287
# largest number was 5.195020951333553
print(random.randint(1, 100))
# Smallest number was 1
# Largest number was 99
