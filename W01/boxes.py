import math

items = input("Enter the number of items: ")
items_per_box = input("Enter the number of items per box: ")

num_per_boxes = math.ceil(int(items) / int(items_per_box))

# print(f"\nYou will need {num_per_boxes} boxes to store {items} items, with {int(items) % int(items_per_box)} items left over.\n")

print(f"\nFor {items} items, packing {items_per_box} items in each box, you will need {num_per_boxes} boxes.")