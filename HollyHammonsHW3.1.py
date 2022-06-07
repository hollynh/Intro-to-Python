#   equations of shapes

#   importing pi from math
from math import pi

#   user inputs the radius
r = float(input("Enter the radius:"))

#   the equations
areaCircle = pi * (r**2)
circumferenceCircle = 2 * pi * r
volumeSphere = (4/3) * pi * (r**3)
surfaceSphere = 4 * pi * (r**2)

#   prints the answers
print("The area of a circle with that radius is:", areaCircle)
print("The circumference of a circle with that radius is:", circumferenceCircle)
print("The volume of a sphere with that radius is:", volumeSphere)
print("The surface area of a sphere with that radius is:", surfaceSphere)
      
