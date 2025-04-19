x = int(input("enter a number: "))
y = int(input("enter the number you want to remove: "))
for i in range(x):
    if i == y:
        continue
    print(i)
