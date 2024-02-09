
print("----------------Task3------------------------")

money_collected = 0
i = 0
while i < people:
    money_collected += amount[i]
    i += 1

net_amount = money_collected - cost
if net_amount > 0:
    print(f"Profit is {net_amount}")

if net_amount < 0:
    print(f"The trip has incurred a loss of {abs(net_amount)}")
