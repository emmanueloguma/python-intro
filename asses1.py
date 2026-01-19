#Mr James just died and his properties worth $58000 but he owe a debt of $10000, #the balance was
#divided among his children in the ratio 1:2:3
#Write a python code that determines who got the highest and print it out


p=58000
d=10000
balance=p-d
total_ratio=1+2+3
highest=(3/total_ratio)*balance
print("this is the highest in the room",highest)

lowest=(1/total_ratio)*balance
print("this is the least yaro",lowest)