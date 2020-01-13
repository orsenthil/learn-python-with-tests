def is_leap_year(param):
    pass


def test_is_leap_year():
    assert is_leap_year(2016) == True
    assert is_leap_year(2020) == True
    assert is_leap_year(2024) == True

    assert is_leap_year(2100) == False
    assert is_leap_year(2200) == False
    assert is_leap_year(2300) == False

    assert is_leap_year(2000) == True
    assert is_leap_year(2400) == True

