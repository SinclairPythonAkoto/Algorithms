# Calculate the minimum amount of coins for the amount provided.

def make_change(target_amount: int) -> tuple[int, list]:
    denominations: list[int] = [200, 100, 50, 20, 10, 5, 2, 1]  # needs to be in order
    coin_count: int = 0
    values: list[int] = []
    for coin in denominations:
        while target_amount >= coin:
            target_amount -= coin
            values.append(coin)
            coin_count +1
    return coin_count, values


print(make_change(24))  # 3: 20p + 2p + 2p
print(make_change(163))  # 5: £1 + 50p + 10p + 2p + 1p

