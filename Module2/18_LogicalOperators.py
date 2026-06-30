# and - both must be True
is_logged_in = True
is_premium = True
if is_logged_in and is_premium:
    print("You are a subscriber")

# Truth Table
print("Truth Table for AND Operator")
print(True and True)
print(True and False)
print(False and True)
print(False and False)

#  or - atleast one must be True
is_admin =  True
is_moderator = False
if is_admin or is_moderator:
    print("You can delete, if you are an admin")

# Truth Table
print("Truth Table for OR Operator")
print(True or True)
print(True or False)
print(False or True)
print(False or False)


# not - flips the True or False 
is_banned = False
if not is_banned:
    print("You are bannned")
else:
    print("You are not banned !")

#  these are equivalent in not case
# not - useful for inverting conditions
if not is_banned:
    print("You are NOT banned")
if is_banned == False:
    print("YOU ARE BANNED")

# Example 1
x=5
y=10

result = x > 3 and y < 5
print(result)

# combining operators 
# You can chain multiple conditions:

age = 25
is_student = True
is_senior = False

# Must be Adult AND (student OR Senior)
get_discount = age >=18 and (is_student or is_senior)
print("Is person getting Discount ? ",get_discount)

# Order of Execution -> in case f logical Operators
# not (first)
# and
# or (last)

# without parentheses
# python executes (f and f) -> f (output) -> t or f (and output) -> true (final output)
order1 = True or False and False
print("Without parentheses: ",order1)

# with parenthese -> different result
order2 = (True or False) and False
print("With parentheses: ",order2)

# Use parentheseto make your intent clear ; Don't rely on procedure

# SHORT CIRCUIT EVALUATION -> Python stops evaluating as soon as it knows answer
# With and : if the first condition is False, Python doesn't check Rest.
is_logged_in = False
expensive_check = True
# expensive_check() never runs ! 
if is_logged_in and expensive_check:
    print("Not logged in, Login in first for this expensive Check")

# With or: if the first condition is True, Python doesn't check Rest -> True or anything : Always True.
is_logged_in = True
expensive_check = True
if is_logged_in or expensive_check:
    print("Let's go, you're logged in for your expensive Checkout")

# Why this matters : 
# Safe - won't crash if User is None
class User:
    def __init__(self, is_active):
        self.is_active = is_active

    user = None
    # User -> None -> false -> Python stops there
    if user and user.is_active:
        print("User is active")
    else:
        print("User is NOT active")
    # Not active -> user.is_active was never touched, so no AttributeError
# If user is none -> False -> Python stops their and never tries to access user.is_active 

# With not: 