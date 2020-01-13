
def is_leap_year(year: int) -> bool:
    """
    :param year Given year to test, whether it is a leap year
    :return: True if leap year, False otherwise
    """

    # divisible by 4, True
    if year % 4 == 0:
        # divisible by 10, False
        if year % 100 == 0:
            # divisible by 400, True
            if year % 400 == 0:
                return True

            return False

        return True

    return False


def test_is_leap_year():
    assert is_leap_year(2016) == True
    assert is_leap_year(2020) == True
    assert is_leap_year(2024) == True

    assert is_leap_year(2100) == False
    assert is_leap_year(2200) == False
    assert is_leap_year(2300) == False

    assert is_leap_year(2000) == True
    assert is_leap_year(2400) == True

    assert is_leap_year(2019) == False

