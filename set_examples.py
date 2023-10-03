
colors1 = ['red', 'green', 'purple', 'orange', 'brown',
'black', 'olive', 'scarlet', 'taupe', 'mauve', 'navy', 'white', 'black',
'pink', 'chartreuse']

colors2 = ['red', 'green', 'purple', 'orange', 'brown',
'black', 'olive', 'navy', 'coneflower', 'ivory', 'burnt umber',
'raw sienna', 'white', 'black', 'red', 'red', 'red', 'brown',
'pink', 'chartreuse']

c1 = set(colors1)
c2 = set(colors2)

c1.add('pumpkin spice')
c1.add('pumpkin spice')
c1.add('pumpkin spice')

print(f"c1: {c1}\n")
print(f"c2: {c2}\n")

c1.add('gray')
c1.add('teal')

print(f"c1: {c1}\n")
print(f"c2: {c2}\n")

c1_sorted = sorted(c1)
print(f"c1_sorted: {c1_sorted}")
print(f"type(c1_sorted): {type(c1_sorted)}")
print()

print("common:", c1 & c2)   # intersection
print("not common:", c1 ^ c2)  # xor
print("both:", c1 | c2)  # union
print('just c1:', c1 - c2)
print('just c2:', c2 - c1)

with open('DATA/breakfast.txt') as breakfast_in:
    all_food = breakfast_in.read().splitlines()
    print(f"all_food: {all_food}")
    print()
    unique_food = set(all_food)
    print(f"unique_food: {unique_food}\n")
    



