from alpha.mathlib import geometry as g
import lxml.etree as et 

x = et.Element('spam')


a1 = g.circle_area(8)
a2 = g.rectangle_area(10, 12)
a3 = g.square_area(7.9)
print(a1, a2, a3)
