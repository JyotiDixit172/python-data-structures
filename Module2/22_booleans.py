""" Programs make decisions constantly. 
Every decision comes down to a yes-or-no question and Python answers those with booleans.
"""

# Booleans: True or False
is_logged_in = True
is_admin = False

# Comparisons produce booleans
age = 25
print(age >= 18) # True
print(age == 30) # False

print(""" True and False 
Python has exactly two boolean values: """)

is_active = True
is_deleted = False

print("""Note the capital letters - True and False, not true and false. Python is case-sensitive.""")


print("Bool function: ")
print(bool(0))        # False
print(bool(42))       # True
print(bool(""))       # False
print(bool("hello"))  # True
print(bool([]))       # False
print(bool([1, 2]))   # True
print(bool(None))     # False