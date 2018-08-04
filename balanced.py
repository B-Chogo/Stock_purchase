import random

# Return current value
def stock_value(stk):
    if stk == 0:
        value = 1400
    elif stk == 1:
        value = 1000
    err = random.randrange(-100, 100)
    return value + err 


# Current stocks you have
purchased_stock = [90, 110]
# range to purchase in next time
purchase_range = [50000, 60000]
# amount of unit to buy in next time 
buy_balance = [0, 0]
# List for buy units
balances = []
# Dispersion
vers = []
# current value for each account 
stk_value = [stock_value(0), stock_value(1)]


total_value = sum([buy_balance[i]*stk_value[i] for i in range(2)])
while total_value < purchase_range[1]:
    while total_value < purchase_range[1]:
        # If the balance is in purchase range,
        # culculate dispersion and add lists
        if purchase_range[0] < total_value :
            balances.append(list(buy_balance))
            values = sum([(purchased_stock[i]+buy_balance[i]) * stk_value[i] for i in range(2)])
            ver = sum([((purchased_stock[i]+buy_balance[i])*stk_value[i] - values/2)**2 for i in range(2)])
            print(buy_balance, stk_value, total_value, values)
            vers.append(ver)
        buy_balance[0] += 10
        total_value = sum([buy_balance[i]*stk_value[i] for i in range(2)])
    buy_balance[0] = 0
    buy_balance[1] += 10
    total_value = sum([buy_balance[i]*stk_value[i] for i in range(2)])

# Checking minimum dispersion in the list
idx = vers.index(min(vers))

print(" ======== RESULT ========")
print("CURRENT STOCK VAL: ", stk_value) 
print("CURRENT STOCK    : ", purchased_stock)
print("CURRENT PURCHASED: ", [purchased_stock[i]*stk_value[i] for i in range(2)])
print("CURRENT VALUE    : ", stk_value)
print("PURCHASE RANGE   : ", purchase_range)
print("BALANCED PLAN    : ", balances[idx])
print("AFTER PURCHAE    : ", [(purchased_stock[i]+balances[idx][i])*stk_value[i] for i in range(2)])
