# Ask user to input weather from a predefined set of conditions
weather = input("What's the weather like today?\n(sunny/rainy/cold): ").lower()

# Based on the user’s input, your program will recommend different types of clothing
if weather == "sunny":
  print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
  print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
  print("Make sure to wear a warm coat and a scarf.")
else:
  print("Sorry, I don't have recommendations for this weather.")