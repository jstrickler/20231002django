
import sys   # Import the sys module 

print(sys.argv) # Print all parameters, including script itself

print(f"Script name (sys.argv[0]): {sys.argv[0]}")

name = sys.argv[1]  # Get the first actual parameter
print("first param (sys.argv[1]) is", name)

