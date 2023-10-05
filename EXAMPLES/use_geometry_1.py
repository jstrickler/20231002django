import sys
# from pkg.pkg import module
from alpha.mathlib import geometry  #  find geometry.py 

a1 = geometry.circle_area(8)
a2 = geometry.rectangle_area(10, 12)
a3 = geometry.square_area(7.9)
print(a1, a2, a3)

geometry._private_thing()

# search order
# 1. current folder
# 2. folders in environment variable PYTHONPATH   "dir1;dir2;dir3" (Win) or "dir1:dir2:dir3" (Mac/Linux)
# 3. folders in sys.prefix + "/lib"
print(f"sys.prefix: {sys.prefix}")
print(f"sys.executable: {sys.executable}")
print()
for path in sys.path:
    print(path)
print('-' * 60)







