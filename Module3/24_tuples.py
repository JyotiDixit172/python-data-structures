# create a tuple
point = (10,20)

# access the item (same as lists)
print(point[0])
# it will return 10

# Tuples are immutable -> this would lead to error:
# point[0] = 15 
# The below will give TypeError
point[0] = 15

# creating tuples without & with parentheses
point = (10,20)