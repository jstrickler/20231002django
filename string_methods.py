actor = "Chris Hemsworth"

x = actor.upper()
print(f"x: {x}")

#  .upper() .lower() .title() .capitalize()
print(f"actor.startswith('Chris'): {actor.startswith('Chris')}")
print(f"actor.startswith('Liam'): {actor.startswith('Liam')}")
s = "The Larch"
print(f"s.removeprefix('The '): {s.removeprefix('The ')}")

print(f"actor.count('h'): {actor.count('h')}")
print(f"actor.count('is'): {actor.count('is')}")
print(f"actor.count('H'): {actor.count('H')}")
print(f"actor.lower().count('h'): {actor.lower().count('h')}")

x = 5
print(f"x: {x}")
print('-' * 60)

print(f"actor.find('Hem'): {actor.find('Hem')}")
print(f"actor.find('Blob'): {actor.find('Blob')}")

addr = "jstrickler@gmail.com"

print(f"addr.partition('@'): {addr.partition('@')}")

print(f"addr.split('@'): {addr.split('@')}")

record = "George:Washington:VA"
fields = record.split(':')
print(f"fields: {fields}")

data = "red blue green"
print(data.split())

s = "      All my exes live in Texas     "
print(f"s: |{s}|")
print(f"s.lstrip(): |{s.lstrip()}|")
print(f"s.rstrip(): |{s.rstrip()}|")
print(f"s.strip(): |{s.strip()}|")

print('-' * 60)

raw_amount = "$12.98"
stripped_amount = raw_amount.lstrip('$')
print(f"stripped_amount: {stripped_amount}")
amount = float(stripped_amount)
print(f"amount: {amount}")



