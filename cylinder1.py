#the height of a cylinder is 10cm if the diameter is equals 16cm
#and pie equals 3.142 using python code calculate the volume of the cylinder and 
#the surface area. hint:volume of cylinder=pier*rh
#hint:surface area of cylinder=2pierh+2pier*r

h=10
d=16
r=d/2
pie=3.142
volume=pie*r*r*h
print(volume)
surfacearea=(2*pie*h)+(2*pie*r*r)
print(surfacearea)
new=volume+surfacearea
print(new)