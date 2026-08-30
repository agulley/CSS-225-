# Andre Gulley

# 8-30-2026

# Leap year

def is_leap_year(year):
    """
    Returns True if the year is a leap year, and False otherwise.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Examples to test the function:
print(is_leap_year(2000))  # Returns True (divisible by 400)
print(is_leap_year(1900))  # Returns False (divisible by 100 but not 400)
print(is_leap_year(2024))  # Returns True (divisible by 4 but not 100)
print(is_leap_year(2023))  # Returns False (not divisible by 4)
