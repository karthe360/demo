lp_y=int(input("enter year:"))


#condition to find leap year
if lp_y%4==0 and lp_y%100!=0 or lp_y%400==0:
        print(f"leap year is{lp_y}")
#else not leap year
else:
    print(f"not leap year{lp_y}")