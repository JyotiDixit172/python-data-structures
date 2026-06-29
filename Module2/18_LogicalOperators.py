# and - both must be True
is_logged_in = True
is_premium = True
if is_logged_in and is_premium:
    print("You are a subscriber")

# Truth Table
print("Trueth Table for AND Operator")
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

if not is_banned:
    print("You are NOT banned")
if is_banned == False:
    print("YOU ARE BANNED")

x=5
y=10

result = x > 3 and y < 5
print(result)