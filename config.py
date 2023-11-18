try:
    from datetime import datetime
except ImportError as e:
    print(f"Error importing datetime: {e}")
    datetime = None

pages = ["Day", "Week", "Month"]
   
time_slot = []
for i in range(25):
    if i < 10:
        time_slot.append("0" + str(i) + ".00AM")
        time_slot.append("0" + str(i) + ".30AM")
    elif i > 12:
        time_slot.append(str(i) + ".00PM")
        if i != 24:
            time_slot.append(str(i) + ".30PM")
    else: 
        time_slot.append(str(i) + ".00AM")
        time_slot.append(str(i) + ".30AM")

notify_me = ["Yes", "No"]
category_list = ["None", "Work", "Study", "Exercise", "Leisure", "Others"]

#global var 
today  = datetime.now()
current_year = int(today.strftime("%Y"))
current_month = today.strftime("%B")
current_date = int(today.strftime("%d"))  
current_day = today.strftime("%A")
current_page = "Day" 

dates_2023 = []
