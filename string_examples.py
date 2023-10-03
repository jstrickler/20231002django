s1 = "spam\n"
print(f"s1: {s1}")
print(f"len(s1): {len(s1)}")
s2 = 'spam\n'
print(f"len(s2): {len(s2)}")
print("Guido's the ex-BDFL of Python")
print('Guido is the ex-"BDFL" of Python')
s3 = """spam\n"""
print("""Guido's the ex-"BDFL" of Python""")
s4 = '''spam\n'''

#  'x' "x" '''x''' """x"""

query = """
select *
from customers
where state = 'KS'
order by zip_code desc
limit 10
"""

print(repr(query))

s5 = r"spam\n"
print(f"s5: {s5}")
print(f"len(s5): {len(s5)}")

s6 = "spam\\n"
print(f"s6: {s6}")

print("It's 72\u00B0 outside")

#  \uXXXX  \UXXXXXXXX

a = "foo"
b = "bar"

result = a + b
print(f"result: {result}")

s = "You sold me a dead bird"
print(f"'sold' in s: {'sold' in s}")
print(f"'wombat' in s: {'wombat' in s}")

