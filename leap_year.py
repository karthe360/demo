lp_y=int(input("enter year:"))


if i%4==0 and i%100!=0 or i%400==0:
        print(f"leap year is{lp_y}")
else:
    print(f"not leap year{lp_y}")