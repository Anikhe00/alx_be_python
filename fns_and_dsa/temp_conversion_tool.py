# Define two global variables to store the conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9

CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# Write a function to convert fahrenheit to celsius
def convert_to_celsius(fahrenheit):
  global FAHRENHEIT_TO_CELSIUS_FACTOR
  celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
  return celsius

# Write a function to convert celsius to fahrenheit
def convert_to_fahrenheit(celsius):
  global CELSIUS_TO_FAHRENHEIT_FACTOR
  fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
  return fahrenheit

# Prompt the user to enter a temperature and specify whether it’s in Celsius or Fahrenheit.
temperature = int(input("Enter the temperature to convert: ").upper())
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

# Based on the user’s input, call the appropriate conversion function and display the converted temperature.
if unit == "C":
  result = convert_to_fahrenheit(temperature)
  print(f"{temperature}°C is {result}°F")
elif unit == "F":
  result = convert_to_celsius(temperature)
  print(f"{temperature}°F is {result}°C")
else:
  print("Enter a valid temperature and unit")