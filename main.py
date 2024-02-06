import random

choices = ["V", "P"]
BET = "P"
balance = 1000000
start_balance = 1000000
original_bet = 10
bet_value = 1

lastThreeColors = []
results =[]
losts = 0
wins = 0

is_streak = False
for j in range(100):
    for i in range(1000):
        choice = random.choice(choices)
        if len(lastThreeColors) == 4 and all(color == "V" for color in lastThreeColors):
            is_streak = True
        
        if (is_streak):
            balance -= bet_value
            if (balance < 0):
                balance = 0
                break
            if choice == BET:
                balance += bet_value * 2
                bet_value = original_bet
                is_streak = False
            else:
                bet_value *= 2
                
        lastThreeColors += choice
        if len(lastThreeColors) > 4:
            lastThreeColors.pop(0)
    results.append(balance)
    if balance < 1000: losts += 1
    if balance > 1000: wins += 1
    balance = start_balance
avg = 0
for r in results:
    avg += r
avg /= len(results)
print(results)
print("average outcome:", avg - start_balance)
print("wins: ", wins)
print("loses: ", losts)
    
