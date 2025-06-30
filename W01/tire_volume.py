import math
from datetime import date

width = input(f"Enter the width of the tire in mm: ")
width = float(width)  # Convert input to float
aspect_ratio = input(f"Enter the aspect ratio of the tire: ")
aspect_ratio = float(aspect_ratio)  # Convert input to float
diameter = input(f"Enter the diameter of the wheel in inches: ")
diameter = float(diameter)  # Convert input to float

Volume = (math.pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

# Display the calculated volume rounded to two decimal places
print(f"The approximate volume is {Volume:.2f} liters.")

# Log the information in a text file
today = date.today()
with open("tire_volume_log.txt", "a") as log_file:
    log_file.write(f"{today}, {width}, {aspect_ratio}, {diameter}, {Volume:.2f}\n")
