# assign same values to multiple variables
x=y=z=3

# Assign different values in one line
name, age, city = "Alex",25,"Mumbai"

# Swap values without a temp variable
a=1
b=2
# Swapping of values
a,b =b,a

print(a,b) # 2,1

# Django uses variables constantly -> this is where Clear Variable names makes this code readable at glance.

# What does this print?

# a = 5
# b = a
# a = 10

# print(b) -> 5 cause even though the a values gets changed later, but b value was assigned same as a before tha change.
#  so b=5 will remain like this, but after that a will become 10.