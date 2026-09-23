def calculate_total(items):
    total = 0
    for item in items:
        total += item.get("price", 0)
    return total


def get_discount(user):
    if user["role"] == "admin":
        return 0.5
    return 0.1
