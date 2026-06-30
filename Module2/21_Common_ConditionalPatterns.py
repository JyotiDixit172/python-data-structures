print("""Guard Clause (Early Exit) Check for invalid cases first: """)

def process_order(user, items):
    if not user:
        return "Please log in"

    if not items:
        return "Cart is empty"

    # Main logic here...
    return "Order processed"


print("""Assigning Based on Condition""")
age = 20
# Long way
if age >= 18:
    status = "adult"
else:
    status = "minor"

# Short way (ternary expression)
status = "adult" if age >= 18 else "minor"

print("""The ternary form is great for simple assignments.""")