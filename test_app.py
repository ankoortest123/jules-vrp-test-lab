from app import calculate_total, get_discount


def test_calculate_total_normal():
    items = [{"price": 10}, {"price": 20}]
    assert calculate_total(items) == 30


def test_calculate_total_missing_price():
    items = [{"price": 10}, {}, {"name": "free item"}]
    assert calculate_total(items) == 10


def test_get_discount_admin():
    user = {"role": "admin"}
    assert get_discount(user) == 0.5


def test_get_discount_regular():
    user = {"role": "user"}
    assert get_discount(user) == 0.1
