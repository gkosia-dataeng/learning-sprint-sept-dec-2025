'''Best Time to Buy and Sell Stock III

You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete at most two transactions.
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).


Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
'''

prices = [3,3,5,0,0,3,1,4]


# O(n**2)
def find_best_combo(prices):
    profitable_days = [(od,cd,cv - ov)  for od, ov  in enumerate(prices) for cd,cv in enumerate(prices) if cv > ov  and cd  > od]

    not_overlapping_trades = [(f_comp,s_comp, f_comp[2] + s_comp[2])   for f_comp in profitable_days for s_comp in profitable_days if f_comp[1] < s_comp[0] and f_comp[0] < s_comp[0]]

    most_profitable_combo = not_overlapping_trades[0]

    for combo in not_overlapping_trades[1:]:
        if combo[2] > most_profitable_combo[2]:
            most_profitable_combo = combo

    return most_profitable_combo