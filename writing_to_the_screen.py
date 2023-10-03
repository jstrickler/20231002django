person  = "Tom Brokaw"
city = "Chevy Chase"
value = 38.42395489430

print(person)    # sys.stdout.write(str(person) + '\n')
print(person, city)  # sys.stdout.write(str(person) + ' ' + str(city) + '\n')
print()   # sys.stdout.write('\n')
print(person, city, value)
print()
print(person, end=" ")
print(city)
print(person, end=" => ")
print(city)

print(person, city, value, sep="#")
print(person, city, value, sep=" & ")

print(person + ':' + city)
print(f"{person}:{city}")
print(f"2 + 2 is {2 + 2}")
print(f"value is {value}")
print(f"value is {value:.3f}")
# {VALUE:format}
# {x:3d}
# {x:3.3d}
# {x:03d}
# {x:10s}
# {x:8.2f}
# {x:>10s}
# {x:^10s}

x = 123
print(f"x: {x}")

num = 23582309
print(f"{num:,d}")

print(f"{person} lives in {city}")

print("{} lives in {}".format(person, city))
# print("{} lives in {}".format(person))  INVALID






