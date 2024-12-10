#give me a five integers as a user input and save it to a separatly in a list

a=(input("enter the given user input:")).split()
print(list(map(int,a)))