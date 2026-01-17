print("enter first number")
first_number=int(input())
print("enter second number")
second_number=int(input())
print("enter third number")
third_number=int(input())
total=first_number*second_number*third_number
print("this is my total", total)
if total>2000:
    print("it is greater than 2000")
    new=(total*50)
    print(new)
else:
    print("is less than 2000")
    new=(total*3)
    print(new)