age_str ="25"
age_num = int(age_str)

count = 10
count_str = str(count)

price_str ="19.99"
price_num = float(price_str)

print(age_num, count_str, price_num)

# Why This Matters
# User input is almost always a string:

# From a form
# user_input = "25"  

# This would crash: 
# next_year = user_input + 1  # Can't add string and number

# Convert first:
# age = int(user_input)
# next_year = age + 1  # Works: 26