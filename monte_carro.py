import random

def monte_carlo_simulation():
    balance = 15000
    success_count = 0
    total_balance = 0

    for _ in range(3600):
        numbers = [30, 30, 30]
        bet_amount = numbers[0] + numbers[-1]

        while balance >= bet_amount and len(numbers) > 1:
            bet_amount = numbers[0] + numbers[-1]
            
            if balance < bet_amount:
                break

            result = random.choice(["red", "black"])  # Assuming 50% chance for black
            if result == "black":
                numbers.pop(0)
                numbers.pop(-1)
                balance += bet_amount
                total_balance += bet_amount
            else:
                balance -= bet_amount
                numbers.append(bet_amount)
                total_balance -= bet_amount
           
            

        if len(numbers) <= 1:
            success_count += 1
        

    success_rate = success_count 
    avg_balance = total_balance 
    a = balance
    return success_rate, avg_balance,a

success_rate, avg_balance ,a = monte_carlo_simulation()
print("成功数:", success_rate)
print("利益:", avg_balance)
print("残高", a)
