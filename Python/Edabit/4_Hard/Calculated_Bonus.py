# 20200818 - Calculated Bonus
def bonus(days):
    cost = 0
    if days <= 32:
        return cost
    elif 40 >= days > 32:
        cost = (days - 32) * 325
        return cost
    elif 48 >= days > 40:
        cost = (40 - 32) * 325 + (days - 40) * 550
        return cost
    else:
        cost = (40 - 32) * 325 + (48 - 40) * 550 + (days - 48) * 600
        return cost


print(bonus(50))
