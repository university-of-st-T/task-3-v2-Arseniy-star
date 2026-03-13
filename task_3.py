def calculate_total(prices, *discounts, **options):

    tax = options.get("tax", 0)

    round_to = options.get("round_to", 2)

    total = 0
    for price in prices:
        total = total + price

    for discount in discounts:

        discount_factor = 1 - discount / 100
        total = total * discount_factor

    tax_factor = 1 + tax / 100
    total = total * tax_factor

    if round_to is not None:
        total = round(total, round_to)

    return total
