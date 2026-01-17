print("enter first number")
firstnumber=int(input())
print("enter second number")
secondnumber=int(input())
print("enter third number")
thirdnumber=int(input())
total=firstnumber*secondnumber*thirdnumber
print("this is my total" , total)
if total>2000:
    print("bingo!")
    new=(total*50)-200
    print(new)
else:
    print("false")
    new=(total-500)/3
    print(new)
    