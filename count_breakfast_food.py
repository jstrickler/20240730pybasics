FILE_PATH = "DATA/breakfast.txt"

counts = {}

with open(FILE_PATH) as breakfast_in:
    for raw_line in breakfast_in:
        food = raw_line.rstrip()
        if food in counts:
            counts[food] += 1
            #  counts[food] = counts[food] + 1
        else:
            counts[food] = 1   # initialize element

for food, count in counts.items():
    print(f"{food:20} {count}")
