def get_recipe_price(prices, optionals=None, **ingredients):
    if not prices:
        return 0

    if optionals is None:
        optionals = []

    total_price = 0
    for item, amount in ingredients.items():
        if item in prices and item not in optionals:
            price_per_100g = prices[item]
            total_price += (amount / 100) * price_per_100g

    return int(total_price)

def main():
    print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))

    print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))

    print(get_recipe_price({}))

main()