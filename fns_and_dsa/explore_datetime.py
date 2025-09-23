from datetime import datetime, date, timedelta

# Get the current date and time
def display_current_datetime():
  current_date = datetime.now()
  current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
  return current_date

print(f"Current date and time: {display_current_datetime()}")

# Prompt the user to enter a number of days (as an integer).
days = int(input("Enter the number of days to add to the current date: "))

# Calculate future date based on user input
def calculate_future_date(day):
  today_date = date.today()
  future_date = today_date + timedelta(day)
  return future_date

print(f"Future date: {calculate_future_date(days)}")