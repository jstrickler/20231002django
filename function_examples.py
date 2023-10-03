
#  user interface // AKA UX  
def say_hello():
    print("Hello, world")

result = say_hello()
print(f"result: {result}")

def greet(whom="world"):
    print(f"Hello, {whom}")

greet('world')
greet('Mom')
greet('Guido van Rossum')
greet()
greet(4.99)

# 5 types of params
# never: positional-only params
# normal: positional params
# sometimes: optional positional params
# normal for options: named params
# sometimes: optional named params

def spam(*args):
    print(args)

spam(5)
spam(5, 9, 8)
spam()
spam(10, 'foo', 3.5)

def find_text(search_term, *file_paths, ignore_case=False):
    pass

find_text('bird', 'DATA/parrot.txt', 'DATA/alice.txt')

find_text('bird', 'DATA/parrot.txt', 'DATA/alice.txt', ignore_case=True)

def config(**kwargs):
    print(kwargs)

config(file_name="spam.txt", country="Botswana", sport="Cricket")





#-------------------------------------------------------
#  business logic 
def get_message():
    message = "Hello, Django world"
    return message

m = get_message()

print(f"m: {m}")

