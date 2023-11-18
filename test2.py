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

