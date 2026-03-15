from app.bowling import calculate_result, validate_throws


def test_strike():
    assert calculate_result(10, 0) == "Strike"


def test_spare():
    assert calculate_result(4, 6) == "Spare"


def test_normal():
    assert calculate_result(3, 4) == "Normal"


def test_invalid_negative():
    valid, _ = validate_throws(-1, 5)
    assert not valid


def test_invalid_total():
    valid, _ = validate_throws(7, 6)
    assert not valid


if __name__ == "__main__":
    test_strike()
    test_spare()
    test_normal()
    test_invalid_negative()
    test_invalid_total()

    print("All tests passed successfully!")