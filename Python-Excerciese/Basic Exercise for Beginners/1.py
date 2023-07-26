# Excercise 1: Swap the number without using third varible

x=int(input("Enter the first number :\n> "))
y=int(input("Enter the Second number :\n> "))
print(x,y)
x=x+y
y=x-y
x=x-y
print(x,y)
