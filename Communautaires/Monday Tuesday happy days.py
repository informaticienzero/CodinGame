from sys import stderr
from typing import Dict, List


days: List[str] = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def first_dayname_of_year(dayname: str, day: int) -> str:
    """
    Gets the day name of the first of the same year as the starting date.
    """
    index: int = days.index(dayname)
    difference: int = day - 1
    return days[(index - (difference - 0) % 7) % 7]


def number_of_days(month: str, day: int, leap_year: bool) -> int:
    """
    Calculates the number of days between the first of the year and the given day.
    """
    months: Dict[str, int] = { 'Jan': 31, 'Feb': 29 if leap_year else 28, 'Mar': 31, 'Apr': 30, 'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31, 'Sep': 30, 'Oct': 31, 'Nov': 30, 'Dec': 31 }

    days: int = 0
    for key, value in months.items():
        if key == month:
            break
        days += months[key]

    plus_leap: int = 1 if leap_year else 0
    days += day + plus_leap
    return days


leap_year = int(input())
source_day_of_week, source_month, source_day_of_month = input().split()
source_day_of_month = int(source_day_of_month)

target_month, target_day_of_month = input().split()
target_day_of_month = int(target_day_of_month)

is_leap: bool = False if leap_year == 0 else True
# First, we have to calculate the name of the first day.
first_day_name: str = first_dayname_of_year(source_day_of_week, number_of_days(source_month, source_day_of_month, is_leap))
# Then, how much days there are between the first one and the date to guess.
days_passed: int = number_of_days(target_month, target_day_of_month, is_leap)
# Final result!
day_name: str = days[(days_passed % 7 + days.index(first_day_name) - 1) % 7]
print(day_name)
