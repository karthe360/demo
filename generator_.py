def sq(a):
    while a<5:
        
        yield a
        a=a+1
#print(sq(1))
s=sq(1)
for i in s:
 print(i)