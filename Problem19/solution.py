"""
You are given the following information, but you may prefer to do some
research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, but not on a
century unless it is divisible by 400. How many Sundays fell on the
first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""
import datetime


def brute_force_solution():
    """
    A simple solution is to iterate through all the days of the 20th century
    and count how many sundays occur on the first of a month. This solution
    is obviously linear in the number of days in the specified interval.
    """
    start_date = datetime.date(1901, 1, 1)
    end_date = datetime.date(2000, 12, 31)
    sunday_count = 0

    while start_date != end_date:
        start_date += datetime.timedelta(1)

        if start_date.isoweekday() == 7 and start_date.day == 1:
            sunday_count += 1

    return sunday_count


if __name__ == "__main__":
    print brute_force_solution()
