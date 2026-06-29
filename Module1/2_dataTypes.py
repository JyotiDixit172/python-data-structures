# not all data types are same 
# Name -> text, Age -> number
# Python needs to know what type of data it's working with because different types behaves differently.

# Python has 4 basic types:

name = "alex" # string
age = 25 # integer
price = 19.99 # float

# float uses binary floating-points(fast, but imprecise for decimals like 0.1 + 0.2) -> uses base 2 binary -> the way computers understand binary language
# decimal storesxact base 10 values (slower, but precise: Ideal for maoney & financial maths) -> the way humans count -> it stores the same way you'd write on paper
# so 0.1 -> is actually 0.1 -> with no hidden approximation

# Hardware is built to do binary math -> very fast -> so float is quick but approximate
# Decimal is done in software -> with exact digits -> so it's precise but slower

# float -> like measureing with a ruler -> fast but approximate
# decimal -> counting exact coins -> slower but exact -> which is why we should always use decimal while dealing with problems related to finance & money

# a special type 
middle_name = "None" # No-value

# for string use, other quote type when text also containes quote 
msg = 'She said "Hello" !!'

# Common string operations 
name = "Alex smith"
Lower = print("lowercase: ",name.lower())
Upper = print("uppercase: ",name.upper())
Strip = print("Strip: ",name.strip())
Replace = print("Last name replace: ",name.replace("Smith", "Joseph"))
email = "user@example.com"
Startswith = print("Email starts with ? ",email.startswith("user")) # return TRUE
Endswith = print("Email ends with ? ",email.endswith(".com")) # returns TRUE
Check = print("Is @ present in email ? ","@" in email) # returns TRUE

# Watch out 
# Numbers in quotes are strings, not numbers

a = 100
b = "100"
print("Integer addition: ",a+a)
print("String addition: ",b+b)

# Intergers
print("Lets see how INTEGERS works ? -> Positive, Negative or Zero")
score = 900
temperature = -1
count = 0

print("Python let's you use underscore for readability")
population = 7_90_000
print('Population: ',population)

print("Floats: Decimal numbers -> basically numbers with Decimal Point")
price = 19.99
pi = 3.14159
percentage = 0.85

print("Print how computers stored decimals ? 0.1 + 0.2 = ", 0.1 + 0.2)

x = 100
y="100"
print("x:",x,", y:",y)
print("is x = y ? ",x==y)

print("let's convert to sama data type for comparison ?")
print("string y to int y -> now is x = y ?", x ==int(y))