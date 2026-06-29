name = "Jyoti"
balance = 100.50
message = f"Hello, {name}! Your balance is ${balance}" 
print(message)


# f string suoer-powers
price = 19.99
quantity = 3
print(f"Total: ${price*quantity}")

# call methods
name = "Jyoti"
print(f"Hello, {name.upper()} !!")

# Format Numbers
price = 19.5
print(f"${price:.2f}")

# Add commas for thousands
population = 7900000000
print(f"{population:,}")

# Percentages
rate = 0.756
print(f"{rate:.1%}")


#  You'll see this in older code

message = "Hello, {}! Balance: ${:.2f}".format(name,balance)
# % formatting
message = "Hello, %s! Balance: $%.2f"%(name, balance)

# Formatting works with multi-line strings
name = "Jyoti Dixit"
items = 3
email = f""" 
Hi {name},
You have {items} in your cart.
Complete your purchase today !! 
"""