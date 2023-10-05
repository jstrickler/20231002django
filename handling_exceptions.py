import logging

logging.basicConfig(
    filename="exceptions.log",
    level=logging.INFO,
    format="%(levelname)s %(message)s %(asctime)s %(filename)s",
    datefmt="%x-%X",
)

# logging levels
# CRITICAL
# ERROR
# WARNING
# INFO
# DEBUG

file_path = 'DATA/wombats.txt'
logging.info("file path is %s", file_path)

try:
    with open(file_path) as file_in:
        print("hello!")
        contents = file_in.read()
        print(contents)
except (FileNotFoundError, PermissionError) as err:
    logging.exception(err)

with open('DATA/breakfast.txt') as breakfast_in:
    food = breakfast_in.read().splitlines()
    print(f"len(food): {len(food)}")
    try:
        print(food[99])
    except IndexError as err:
        logging.warning(err)

nums = [800, 80, 1000, 0, 32, -4, 255, -8, 400, 5, 0, 5000]

for num in nums:
    try:
        result = 5000 / num
    except ZeroDivisionError as err:
        logging.error(err)
    else:
        print(f"{num:6} {result}")
    
logging.info("ALL DONE")