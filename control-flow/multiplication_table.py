# Prompt user to input a number for which they want to see the multiplication table
number = int(input("Enter a number to see its multiplication table: "))

# Use a for loop to generate the multiplication table
for i in range(1, 115):
  product = number * i
  print(f"{number} x {i} = {product}", end="\t") 
