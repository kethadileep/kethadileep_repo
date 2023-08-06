''' This module gives the maximum profile of stock'''

input_prices = [7, 1, 5, 3, 6, 4]
output = 5

# input_prices = [7,6,4,3,1]
# output= 0

print(f'Expected_output:: {output}')

max_profit = 0
leng = len(input_prices) # measure time for len func
for day in range(leng - 1):
    for next_day in range(day+1, leng):
        day_profit = input_prices[next_day] - input_prices[day]
        if day_profit > max_profit:
            max_profit = day_profit
print(f'profit_output  :: {max_profit}')
