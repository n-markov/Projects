import os
fullPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "demofile.txt")
print(fullPath)

f = open(fullPath)
# print(f.read())
# # Outputs the whole file

# print(f.read(5))
# # Outputs the first 5 characters

x = f.readlines()
print(x[0])
# Read one line of the file

# for x in f:
#   print(x)
# # Loop through the file line by line



