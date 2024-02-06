import random

choices = ["V", "P"]
BET = "P"
balance = 1000
bet_value = 10

lastThreeColors = []
results =[]
losts = 0
wins = 0

is_streak = False
for j in range(10):
    for i in range(100):
        choice = random.choice(choices)
        if len(lastThreeColors) == 5 and all(color == "V" for color in lastThreeColors):
            is_streak = True
        
        if (is_streak):
            balance -= bet_value
            if choice == BET:
                balance += bet_value * 2
                is_streak = False
            else:
                bet_value *= 2
                
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
print(results)
print("average outcome:", avg)
print("wins: ", wins)
print("loses: ", losts)
    
