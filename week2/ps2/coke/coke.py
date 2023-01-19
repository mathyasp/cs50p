amount_due = 50
while amount_due > 0:

    print("Amount due: ", amount_due)

    amount = int(input("Insert a coin: "))

    if amount in [25, 10, 5]:
        amount_due -= amount

print("Change owed: ", abs(amount_due))

