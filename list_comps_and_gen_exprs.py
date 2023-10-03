fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

f0 = []
for f in fruits:
    expr = f.upper()
    f0.append(expr)
print(f"f0: {f0}\n")

#    [expr for var in iterable]
f1 = [f.upper() for f in fruits]
print(f"f1: {f1}\n")

f2 = [f.upper() for f in fruits if f.startswith('p')]
print(f"f2: {f2}\n")

f3 = [f for f in fruits if len(f) > 6]
print(f"f3: {f3}\n")

nums = [800, 80, 1000, 32, -4, 255, -8, 400, 5, 5000]
n1 = [n / 20 for n in nums]
print(f"n1: {n1}\n")

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
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
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

dobs = [dob for _, _, _, dob in people]
print(f"dobs: {dobs}\n")

dirty_nums = [800, None, 80, 42.24, 1000, 32, "256", -4, 255, 9.5, -8, 400, 5, 5000]

clean_nums = [n for n in dirty_nums if isinstance(n, (int, float))]
print(f"clean_nums: {clean_nums}\n")

clean_num_gen = (n for n in dirty_nums if isinstance(n, (int, float)))
print(f"clean_num_gen: {clean_num_gen}")
for num in clean_num_gen:
    print(num, end=' ')
print('\n')


