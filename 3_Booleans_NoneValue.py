# Booleans -> Only two possible values -> True or False

is_Logged_in = True
has_Permission = False

# note the capitalization, True or False
# Booleans are foundations in Decision making in-code
age = 19
age1 = 4
is_adult_age = age >=18
is_minor_age = age <=18
print(is_adult_age)
print(is_minor_age)

# None Value
# None represents the absence of value -> not zero, not empty text - just nothing
profile_picture = None
search_result = None

# Why not use "" or 0 ?
# "" -> empty string -> already a data type
# 0 -> integer zero -> alreday a data type

# None -> means there is no value here.
# You'll see none in lot of Django files

print("""What is the difference here ?
cart_count =0 -> means cart exists & it has 0 items
cart_count = None -> means we don't know the cart count yet, or it doesn't apply """)

print(type("hello"))   # <class 'str'>
print(type(42))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type(True))      # <class 'bool'>
print(type(None))      # <class 'NoneType'>
# Used for debugging when something isn't behaving as expected

# Checking Specific Types
# Sometimes you need to check if a value is a specific type:

age = 25
name = "Alex"
print(isinstance(age,int))
print(isinstance(name,str))
print(isinstance(age,str))

#  multiple instances at once 
print(isinstance(age,(int,float))) # age is one of the types

# this is usefule when you receive data & need to handle different types of data differently.
