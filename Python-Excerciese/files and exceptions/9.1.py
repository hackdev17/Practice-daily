# create simple calculater
print("enter the numbers: ")
print("enter the 'q' to exit")
while(True):
    x=input("enter the number:")
    if x=='q':
        break
    y=input("enter the number:")
    if y=='q':
        break
    try:
        result=int(x)/int(y)
    except ZeroDivisionError:
        print("bhidu zero se divide nahi kar sakate")
    else:
        print(result)
