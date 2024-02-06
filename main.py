import random

choices = ["V", "P"]
BET = "P"
balance = 1000
bet_value = 10

lastThreeColors = []
results =[]
losts = 0
wins = 0
for j in range(1000):
    for i in range(1000):
        choice = random.choice(choices)
        if len(lastThreeColors) == 5 and all(color == "V" for color in lastThreeColors):
            balance -= bet_value
            if choice == BET:
                balance += bet_value * 2
        lastThreeColors += choice
        if len(lastThreeColors) > 5:
            lastThreeColors.pop(0)
    results.append(balance)
    if balance < 1000: losts += 1
    if balance > 1000: wins += 1
    balance = 1000
avg = 0
for r in results:
    avg += r
avg /= len(results)
print("average outcome:", avg)
print("wins: ", wins)
print("loses: ", losts)
