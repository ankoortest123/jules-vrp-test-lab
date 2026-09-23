def calculate_total(items):
    total = 0
    for item in items:
        total += item["price"]  # BUG: KeyError if 'price' missing
    return total


def get_discount(user):
    if user["role"] == "admin":
        return 0.5
    return 0.1
