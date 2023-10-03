from pprint import pprint

FILE_PATH  = "DATA/knights.txt"

knights_data = {}

with open(FILE_PATH) as file_in:
    for raw_line in file_in:
        line = raw_line.rstrip()
        name, title, color, quest, comment = line.split(':')
        knights_data[name] = title, color, quest, comment

pprint(knights_data)

for name, data in knights_data.items():
    print(f"{data[0]:4} {name:10} {data[2]}")
print()

print(f"knights_data['Lancelot'][1]: {knights_data['Lancelot'][1]}")
