# Prompt user for a task description
task = input("Enter your task: ").capitalize()

# Prompt user for a task priority
priority = input("Priority (high/medium/low): ").lower()

# Ask the user if the task is time_bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize reminder as an empty string
reminder = ""

#Process the Task Based on Priority and Time Sensitivity
match priority:
  case "high":
    if time_bound == "yes":
      reminder = f"'{task}' is a {priority} priority task that requires immediate attention today!"
    else:
      reminder = f"'{task}' is a {priority} priority task. Consider completing it when you have free time."
  case "medium":
    if time_bound == "yes":
      reminder = f"'{task}' is a {priority} priority task that requires immediate attention today!"
    else:
      reminder = f"'{task}' is a {priority} priority task. Consider completing it when you have free time."
  case "low":
    if time_bound == "yes":
      reminder = f"'{task}' is a {priority} priority task that requires immediate attention today!"
    else:
      reminder = f"'{task}' is a {priority} priority task. Consider completing it when you have free time."
  case _:
    reminder = f"'{task}' is a task with an unknown priority. Please consider its priority."
  
print(reminder)