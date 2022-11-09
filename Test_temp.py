import Lab2.Lab2 as temp

def test_find_min_max():
    num = [1, 3, 5, 6, 7, 9, 12, 22]
    result = temp.find_min_max(num)
    assert(result == [1.0, 22.0])

def test_calc_average():
    num = [1, 3, 5, 6, 7, 9, 12, 22]
    result = temp.calc_average(num)
    assert(result == 8.125)

def test_calc_median_temperature():
    num = [1, 3, 5, 6, 7, 9, 12, 22]
    result = temp.calc_median_temperature(num)
    assert(result == 6.5)