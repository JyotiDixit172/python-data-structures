# separator controls what goes in between arguments -> Default is a space but you can make it anything
print("2024","01","15",sep="-")
# end controls what goes after - not just for removing newlines
print("Loading",end="....")
# print() -> returns None and that's deliberate -> It put people in comprehensions,it's a side effect function -> not a value producing function
print("Done!")
print("a",'b',"c",sep=",",end="!\n")

""" use of flush = True -> forces output immediately. Python buffers output 
So in case of long running loops or progress bars you can appear late (or all at once) -> flush pushes it out right away """
print("processing", end="", flush=True)
# using sep to unpack a list data structure
print()
print(*[1,2,3],sep=",")