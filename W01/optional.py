#Optional activity

last_name = input("Enter your last name: ")
first_name = input("Enter your first name: ")
middle_name = input("Enter your middle name: ")

print(last_name, first_name, middle_name if last_name else "", sep=", ")