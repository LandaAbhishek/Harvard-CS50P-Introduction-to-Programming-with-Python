valid_coins = [5, 10, 25]
cost = 50

print("Amount Due:", cost)

for _ in range(cost):
    inserted_coin = int(input("Insert coin: "))
    if inserted_coin in valid_coins:
        cost -= inserted_coin
        if cost < 0:
            print(f"Change Owed: {-cost}")
            break
        elif cost == 0:
            print("Change Owed: 0")
            break
        else:
            print("Amount Due:", cost)
    else:
        print("Amount Due:", cost)
