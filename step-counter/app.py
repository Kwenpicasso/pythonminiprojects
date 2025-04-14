print("🏃STEP COUNTER🏃")
daily_steps = int(input("🏃‍♀️‍➡️👟what is your daily step goal? "))
steps_taken = int(input("💨how steps have you taken today? "))
step_needed = daily_steps - steps_taken
if step_needed > 0:
    print(f"you need {step_needed} to reach your goal")
else:
    print(f"Congratulations! you have exceeded your by {-step_needed} steps")
