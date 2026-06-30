print("1. Range Check")
age = 25

# Verbose way
if age >= 18 and age <= 65:
    print("Working age")

# Pythonic way
if 18 <= age <= 65:
    print("Working age")


print("2. Check Against Multiple Values")
day = "Saturday"
# Verbose way
if day == "Saturday" or day == "Sunday":
    print("Weekend!")

# Pythonic way (we'll cover `in` later)
if day in ("Saturday", "Sunday"):
    print("Weekend!")


print("3. Check Against Multiple Values")
day = "Saturday"

# Verbose way
if day == "Saturday" or day == "Sunday":
    print("Weekend!")

# Pythonic way (we'll cover `in` later)
if day in ("Saturday", "Sunday"):
    print("Weekend!")