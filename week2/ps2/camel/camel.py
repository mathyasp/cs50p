camel = str(input("Variable name: "))

for i in camel:
    if i.isupper():
        print("_" + i.lower(), end="")
    else:
        print(i, end="")

print()


