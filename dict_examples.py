
#  Dictionary d = new Dictionary();
d1 = dict() 
capitals = {'NC': 'Raleigh', 'PA': "Harrisburg", 'NY': 'Albany', 'AZ': 'Phoenix'}
print(f"capitals: {capitals}")
print(f"capitals['NY']: {capitals['NY']}")
d3 = {}   # empty dict

capitals['MN'] = 'Minneapolis'
print(f"capitals: {capitals}")
capitals['SC'] = 'Columbia'
capitals['NV'] = 'Carson City'
print(f"capitals: {capitals}")

# Lincoln, Jefferson City, Madison, Jackson
print(f"capitals['NV']: {capitals['NV']}")

# print(f"capitals['VA']: {capitals['VA']}")  fails!

print(f"capitals.get('VA'): {capitals.get('VA')}")
print(f"capitals.get('NY'): {capitals.get('NY')}")
print(f"capitals.get('VA', 'NOT FOUND'): {capitals.get('VA', 'NOT FOUND')}")

KEY = 'TX'
print(f"KEY in capitals: {KEY in capitals}")
KEY = 'SC'
print(f"KEY in capitals: {KEY in capitals}")

print(f"capitals.setdefault('LA', 'Baton Rouge'): {capitals.setdefault('LA', 'Baton Rouge')}")
print(f"capitals: {capitals}")
print()

for state, capital in capitals.items():
    print(state, capital)
print()

print(f"capitals.keys(): {capitals.keys()}")
print(f"capitals.values(): {capitals.values()}")


for state in capitals:   # .keys()
    print(state)



