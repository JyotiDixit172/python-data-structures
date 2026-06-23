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
