#you have been asked to calculate the volume of a cylinder
#whose radius=12cm and height=15cm. using python code calculate the volume of the cylinder
#introduce a conditional statement(if clause)
#check if the volume is greater than 1000, then immediately multiply the volume by 3
#and print out. else if it is less than 1000 divide your answer by 50
r=12
h=15
pie=3.142
volume=pie*r*r*h
print(volume)
if volume>1000:
    new=volume*3
    print(new)
    
else: 
    new=volume/50
    print(new)
    