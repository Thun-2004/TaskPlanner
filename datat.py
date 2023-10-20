
data = {
            'Year': "2023",
            'Month': "October",
            'Day' : [
                {
                    'Date': "17",
                    'Day_of_week' : "Tuesday",
                    'Time_slot' : [
                        {
                            '1' : {
                                'note' : "Run", 
                                'category' : "Exercise",
                                'location' : "Gym",
                                'start' : "12.00",
                                'end' : "13.00",
                                'notify_me' : "Yes"
                            }, 
                            '2' : {
                                'note' : "Meeting", 
                                'category' : "Work",
                                'location' : "Home",
                                'start' : "17.40",
                                'end' : "18.40",
                                'notify_me' : "Yes"
                            }
                        }
                    ]
                }, 
                {
                    'Date': "19",
                    'Day_of_week' : "Wednesday",
                    'Time_slot' : [
                        {
                            '1' : {
                                'note' : "Eat", 
                                'category' : "None",
                                'location' : "Paragon",
                                'start' : "15.00",
                                'end' : "18.00",
                                'notify_me' : "Yes"
                            }
                        }
                    ]
                }
            ]
        }

def get_day(day, month, year):
    if data['Year'] == year and data['Month'] == month:
        for i in data['Day']: 
            if i['Date'] == day:
                return i["Time_slot"]
            
print(get_day("17", "October", "2023"))



