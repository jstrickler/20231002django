
FILE_PATH = 'DATA/breakfast.txt'
counts = {}

with open(FILE_PATH) as file_in:
    for raw_line in file_in:
        food = raw_line.rstrip()
        if food not in counts:
            counts[food] = 0
        counts[food] += 1  # counts[food] = counts[food] + 1

for food, count in counts.items():
    print(f"{food:15s} {count:2d}")

