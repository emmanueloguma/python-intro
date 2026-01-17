print("enter first number")
first_number=float(input())
print("enter second number")
second_number=float(input())
print("enter third number")
third_number=float(input())
print("enter fourth number")
fourth_number=float(input())
total=float(first_number+second_number+third_number+fourth_number)
print(total)
if total<4000:

    print("it is less than 4000")
    new=total/4
    print(new)
else:
    print("is greater than 4000")
    new=total-200
    print(new)
    