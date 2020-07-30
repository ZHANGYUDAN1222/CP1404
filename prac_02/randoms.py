import random
print(random.randint(5, 20))  # line 1  
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3
""" 
# What did you see on line 1?
5
# What was the smallest number you could have seen, what was the largest?
smallest:5
largest:19

# What did you see on line 2?
3
# What was the smallest number you could have seen, what was the largest?
smallest:3
largest:9
# Could line 2 have produced a 4?
No

# What did you see on line 3?
5.3916355347891844
# What was the smallest number you could have seen, what was the largest?
smallest:2.5000000000000000
largest:5.4999999999999999 """

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1,101))