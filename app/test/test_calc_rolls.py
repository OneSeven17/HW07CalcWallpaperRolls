from calc_rolls import calculate_roll_quantity


def test_calc_rolls():

    result = calculate_roll_quantity(400, 200, 275, 106, 1000)

    assert 4 == result

