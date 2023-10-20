from datetime import datetime

pages = ["Day", "Week", "Month"]
   
time_slot = []
for i in range(24):
    if i < 10:
        time_slot.append("0" + str(i) + ".00AM")
        time_slot.append("0" + str(i) + ".30AM")
    elif i > 12:
        time_slot.append(str(i) + ":00PM")
        time_slot.append(str(i) + ":30PM")
    else: 
        time_slot.append(str(i) + ":00AM")
        time_slot.append(str(i) + ":30AM")

notify_me = ["Yes", "No"]
category_list = ["None", "Work", "Study", "Exercise", "Leisure", "Others"]

#global var 
today  = datetime.now()
current_year = today.strftime("%Y")
current_month = today.strftime("%B")
current_date = today.strftime("%d")
current_day = today.strftime("%A")
current_page = "Day" 