#A pie chart shows a woman’s groceries purchase in the market with the following
#yam(colour blue =35
#cassave (color Red)=15
#potatoes(color green)=20

#carrot(color green)=10
#Groundnuts (color purple)= ?
#Write python code that determines the percentage left for groundnut
#Also
#Write python code that determines the degree occupied by groundnut


yam=35
cassava=15
potatoes=20
carrot=10
used_percentage=yam+cassava+potatoes+carrot
groundnut=100-used_percentage
print(groundnut)

#calculating groundnut_degree
groundnut_degree=(groundnut/100)*360
print(groundnut_degree)