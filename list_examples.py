import sys

list1 = list()   # empty
print(f"len(list1): {len(list1)}")
print(f"list1: {list1}")
list2 = ['a', 'b', 'c']
print(f"len(list2): {len(list2)}")
print(f"list2: {list2}")
list3 = ['a', 5, 'None', 6.3]
print(f"list3: {list3}")
list4 = []   # same as list4 = list()
print(f"len(list4): {len(list4)}")
print(f"list4: {list4}")
print()

cities = ['Tempe', 'Phoenix', 'Goodyear', 'Durham', 'Avondale', 'New York']
print(f"cities: {cities}")
print(f"len(cities): {len(cities)}")
print(f"cities[0]: {cities[0]}")
print(f"cities[5]: {cities[5]}")
print(f"cities[-1]: {cities[-1]}")    # cities[len(cities)-1]
cities[3] = "Raleigh"
print(f"cities: {cities}")

cities.insert(0, 'Topeka')
cities.insert(4, 'Sacramento')
print(f"cities: {cities}")

cities.append('Boston')
cities.append('Minneapolis')
print(f"cities: {cities}")

more_cities = ['Scarsdale', 'Sag Harbor', 'Newark', 'Poughkeepsie']

cities.extend(more_cities)
print(f"cities: {cities}")

#  LIST.insert(pos, obj)  LIST.append(obj)  LIST.extend(iterable)

del cities[-2]
print(f"cities: {cities}")

#  del object
#  del LIST[pos]
#  del DICT[key]

del cities[0]
print(f"cities: {cities}")

cities.remove('Sag Harbor')
print(f"cities: {cities}")

pos = cities.index('Poughkeepsie')
print(f"pos: {pos}")

city = 'Chicago'
if city in cities:
    print(f"{city} is in cities")
else:
    print(f"{city} is NOT in cities")

city = cities.pop()
print(f"city: {city}")
print(f"cities: {cities}")

city = cities.pop(4)
print(f"city: {city}")
print(f"cities: {cities}")

#  del LIST[pos]   LIST.remove(VALUE)  x = LIST.pop()   x = LIST.pop(pos)

fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

print(f"fruits[0]: {fruits[0]}")
print(f"fruits[4]: {fruits[4]}")
print(f"fruits[-3]: {fruits[-3]}")

print(f"fruits[5:9]: {fruits[5:9]}")
print(f"fruits[0:5]: {fruits[0:5]}")
print(f"fruits[:5]: {fruits[:5]}")
print(f"fruits[-10:]: {fruits[-10:]}")
print(f"fruits[:]: {fruits[:]}")
print(f"fruits[::2]: {fruits[::2]}")

actor = 'Chris Hemsworth'
print(f"actor[:5]: {actor[:5]}")
print(f"actor[6:9]: {actor[6:9]}")

#  start is INclusive
#  stop is EXclusive

print(f"actor[-9:]: {actor[-9:]}")
print(f"actor[2:8]: {actor[2:8]}")
print()

for fruit in fruits:
    print(fruit.title())

# for VAR in ITERABLE:
#     .... VAR .....

for file_name in sys.argv[1:]:
    print(f"Processing {file_name}")


x = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(f"x: {x}")
print(f"x[1:]: {x[1:]}")
print(f"x[:-1]: {x[:-1]}")
print(f"x[1:-1]: {x[1:-1]}")

#  +  *  in 

x = "foo" + "bar"
print(f"x: {x}")

y = [1, 2, 3] + [4, 5, 6]
print(f"y: {y}")

print('-' * 60)
print('Python! ' * 10)

flags = [False] * 25
print(f"flags: {flags}")

data = ['a', 'b', 'c']
print(f"data * 5: {data * 5}")
print()

fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

for fruit in 'apple', 'orange', 'grapefruit', 'banana':
    print(fruit, fruit in fruits)
print()

actor = 'Chris Hemsworth'
print(f"'worth' in actor: {'worth' in actor}")

nums = [800, 80, 1000, 32, -4, 255, -8, 400, 5, 5000]

print(f"len(nums): {len(nums)}")
print(f"min(nums): {min(nums)}")
print(f"max(nums): {max(nums)}")
print(f"sorted(nums): {sorted(nums)}")
print(f"sum(nums): {sum(nums)}")
print()

print(f"fruits: {fruits}\n")

rf = reversed(fruits)
print(f"rf: {rf}\n")

for fruit in rf:
    print(fruit)
print()
print("Try again:")
for fruit in rf:
    print(fruit)
print('-' * 60)

for i in range(len(fruits) - 1, 0, -1):
    print(fruits[i])
print('-' * 60)
print("Using a slice")
for fruit in fruits[len(fruit):0:-1]:
    print(fruit)
print()


reversed_fruits = list(reversed(fruits))
#  list(iterable)

for i, fruit in enumerate(fruits):
    print(i, fruit)
print()
print(list(enumerate(fruits)), '\n')

for i in range(5):
    print("Python is the best!")
print()

#  range(stop)   range(start, stop)   range(start, stop, step)








