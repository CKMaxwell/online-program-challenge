# 20200825 - Calculate the Profit
def profit(info):
	total_profit = (info["sell_price"] - info["cost_price"]) * info["inventory"]
	return round(total_profit,0)
