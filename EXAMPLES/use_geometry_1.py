import sys
#  alpha/mathlib/geometry.py
import alpha.mathlib.geometry as geometry  # find and load geometry.py

a1 = geometry.circle_area(8)
a2 = geometry.rectangle_area(10, 12)
a3 = geometry.square_area(7.9)
print(a1, a2, a3)

# module search order:
#  1. current folder
#  2. folders in PYTHONPATH
#  3. builtin folders (sys.prefix/lib)
print(f"{sys.prefix = }\n")
