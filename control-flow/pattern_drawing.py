# Prompt user for patter size
size = int(input("Enter the size of the pattern: "))

# Initialize a row counter
row = 0

# Draw the pattern
while row < size:
  for i in range(size):
    print("*", end="")
  print()
  row += 1