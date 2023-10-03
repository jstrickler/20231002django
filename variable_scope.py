
animal = 'wombat'  # global var

if animal:
    x = 5  # also global


def spam():
    color = "gold"
    animal = 'yeti'  # local var
    print(f"color: {color}")
    print(f"animal: {animal}")
    

spam()
# print(f"color: {color}")  INVALID -- color is local to spam()
print(f"animal: {animal}")
print(f"x: {x}")
