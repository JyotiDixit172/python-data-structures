num1 = 11
num2 = num1

print("\nBefore num2 value is updated")
print("num1 = ", num1)
print("num2 = ",num2)

print("num1 points to: ",id(num1))
print("num2 points to: ",id (num2))

num2 = 22
#  does this 22 overwrites the 11
#  if this is the case then num1 % num2 would now be pointing at 22 ? correct.

#  OR a seprate int block in memory block is allocated to 22 and num1 -> 11 while num2 -> 22

print("\nAfter num2 is updated: ")
print("num1 =", num1)
print("num2 =",num2)

print("num1 poinst to: ",id(num1))
print("num2 points to:", id(num2))

