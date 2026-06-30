age = 25
age == 25   # True
age != 30   # True
age > 18    # True
age < 18    # False
age >= 25   # True

print("Common Mistake: = vs ==")
x = 5      # Assignment: x becomes 5
x == 5     # Comparison: is x equal to 5? (returns True)

print(""" Using = when you mean == is a classic bug. Remember:

Single = → "becomes" (assignment)

Double == → "is equal to?" (comparison)""")


print("omparing Strings")

print("String comparison is case-sensitive:")

name = "Alice"

name == "Alice"   # True
name == "alice"   # False (different case)
name == "Bob"     # False

print("Strings compare alphabetically:")

"apple" < "banana"  # True (a comes before b)
"cat" > "car"       # True (t comes after r)

print("Storing Comparison Results")
print("You can store comparisons in variables, this makes code more readable:")

age = 25
minimum_age = 18

is_adult = age >= minimum_age
print(is_adult)  # True

# More readable than putting the comparison inline
if is_adult:
    print("Access granted")

print("Truthy and Falsy")
print('Python treats some non-boolean values as "sort of true" or "sort of false."')
print("""Falsy values (act like False):
False
None
0 (zero)
"" (empty string)
[] (empty list)
{} (empty dictionary)
Truthy values (act like True):
Everything else """)

# Empty string is falsy
username = ""
if username:
    print("Hello!")  # Won't print

# Non-empty string is truthy
username = "alex"
if username:
    print("Hello!")  # Prints!

print("""This lets you write cleaner code:
Instead of
if username != "":
    ...

You can write
if username:
    ...""")

