user_age = input("How old are you? \n")
heart_rate = 220 - int(user_age)


print(f"\nWhen you physically exercise to strengthen your heart, you should maintain your heart rate within a range for at least 20 minutes.")
print(f"When exercising to strengthen your heart, you should keep your heart rate between {(0.65 * heart_rate):.2f} and {(0.85 * heart_rate):.2f} of your heart’s maximum rate.\n")     
