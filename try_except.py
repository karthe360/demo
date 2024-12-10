age=int(input("enter the age:"))

try:
    if age<18:
        raise ValueError()
    else:
        result=10/0
except ValueError:
    print ("minor age not allowed age only 18 above")
except ZeroDivisionError:
    print ("can not divide by zero")
1