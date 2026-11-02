def calc(prices, discount):
    total = sum(prices)
    discounted_total = total * (1 - discount)
    return discounted_total
