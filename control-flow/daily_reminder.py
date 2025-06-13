task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
reminder = True
while reminder:
    match priority:
        case "high":
              if time_bound == "yes":
                   print(f"'{task}' is a high priority task that requires immediate attention today!")
              elif time_bound == "no":
                print(f"'{task}'High priority task: Urgent in importance, not in timing")
              else:
                   print(f"the task is '{task}' but they is no time_bound")
        case "medium":
            if time_bound == "yes":
                   print(f"'{task}'is a medium priority task that requires attention today!")
            elif time_bound == "no":
                print(f"'{task}'medium priority task not in timing")
            else:
                   print(f"the task is '{task}' but they is no time_bound")
        case "low":
              if time_bound == "yes":
                   print(f"{task} is a low priority task you can do it in your free time today!")
              elif time_bound == "no":
                print(f"{task} is a low priority task. Consider completing it when you have free time.")
              else:
                   print(f"the task is {task} but they is no time_bound")
    break