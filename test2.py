import calendar
from datetime import datetime, timedelta

def get_current_week_dates(input_date):
    input_datetime = datetime.strptime(input_date, '%d/%m/%Y')
    day_of_week = input_datetime.weekday()
    start_date = input_datetime - timedelta(days=day_of_week)
    end_date = start_date + timedelta(days=6)
    current_week_dates = [start_date + timedelta(days=i) for i in range(7)]
    current_week_day_numbers = [date.day for date in current_week_dates]
    return current_week_day_numbers

# Examples
date1 = "1/10/2023"
date2 = "07/10/2023"
date3 = "14/10/2023"
date4 = "20/10/2023"
date5 = "26/10/2023"
#if + 6 > prev month days, then add 1 to next month days and call 1 of next month

result1 = get_current_week_dates(date1)
result2 = get_current_week_dates(date2)
result3 = get_current_week_dates(date3)
result4 = get_current_week_dates(date4)
result5 = get_current_week_dates(date5)

num_days_prev = calendar.monthcalendar(2023,  10)
# print(num_days_prev)
print(result1)  # Output: [13, 14, 15, 16, 17, 18, 19]
# print(result2)
# print(result3)# Output: [26, 27, 28, 29, 30, 1, 2]
# print(result4)
# print(result5)