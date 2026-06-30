# Core conditonal statements in Python

age = 20
if age >= 18:
    print("You are underage")
else:
    print("Too young to vote")

temperature = 15
# temperature = 35
if temperature > 30:
    print("It's hot outside")

# Colon : after the condition is required. The indentation (4 spaces) defines what's "inside" the block

balance = 50
if balance >= 100:
    print("Purchase approved")
else:
    print("Insufficient funds")

# If the condition is True → runs the if block
# If the condition is False → runs the else block
# One of them always runs. Never both.

print("What does this print ?")
x = 10
if x > 5:
    print("A")
else:
    print("B")

print("C")

print("If-Elif-Else: Multiple Paths")
print("When you have more than two options:")
score = 75
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(grade)  # C

print("Python checks each condition from top to bottom. The first one that's True runs, then Python skips the rest.")
print('elif is short for "else if"')


print("""Order Matters
The conditions are checked in order, and only the first match runs:""")
age = 25
# Wrong order - "Adult" never prints!
if age >= 0:
    print("Alive")      # This runs (25 >= 0)
elif age >= 18:
    print("Adult")      # Never reached
elif age >= 65:
    print("Senior")     # Never reached
# Correct order - most specific first
if age >= 65:
    print("Senior")
elif age >= 18:
    print("Adult")      # This runs for age 25
elif age >= 0:
    print("Child")

print("Put the most specific conditions first.")

print("""Nested If Statements
You can put if statements inside other if statements: Nested If Statements""")

is_member = True
cart_total = 150

if is_member:
    if cart_total >= 100:
        print("Free shipping!")
    else:
        print("$5 shipping")
else:
    if cart_total >= 200:
        print("Free shipping!")
    else:
        print("$10 shipping")
print("""This works, but deep nesting gets hard to read. We'll see better patterns later (logical operators, early returns).""")


print("""Multiple Independent Checks
Sometimes you need to check several things independently - not either/or:""")

temperature = 25
is_raining = True

# These are independent checks, not alternatives
if temperature > 30:
    print("Bring water")

if is_raining:
    print("Bring umbrella")

if temperature < 10:
    print("Bring jacket")

print("Each if is checked separately. Use separate if statements when conditions aren't mutually exclusive.")

