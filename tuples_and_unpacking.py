
person = 'Bill', 'Gates', 'Microsoft', '1955-10-28'

print(f"person[0]: {person[0]}")
print(f"person[1]: {person[1]}")
print(f"len(person): {len(person)}")
print()

a = 5,   # tuple with one value
b = ()   # empty tuple

first_name, last_name, product, dob = person   # iterable unpacking
print(f"first_name: {first_name}")
print(f"last_name: {last_name}")

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'git', '1969-12-28'),
]
print(f"people[0]: {people[0]}")
print(f"people[0][1]: {people[0][1]}")
print(f"people[0][1][2]: {people[0][1][2]}")
print()

# for x in my_list:
#    print(x)

for first_name, last_name, *product, dob in people:
    print(first_name, last_name, dob, product)
print()

