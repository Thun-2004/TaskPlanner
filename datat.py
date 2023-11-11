
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


#incase
#try-except open file 
# class FileHandling: 
#     def load_data(self, filename): 
#         file = open(filename, 'rb')
#         data = pickle.load(file)
#         file.close()
#         return data
    
#     def get_day_task(self,day, month, year): #return list of time slots 
#         data = self.load_data("data.pickle")
#         if data['Year'] == year and data['Month'] == month:
#             for i in data['Day']: 
#                 if i['Date'] == day:
#                     return i["Time_slot"]
    
#     #shouldn't save to current year/month automatically : user should input
#     def save_data(self, filename, note, category, location, start_t, end_t, notify_result): 
#         start = float(start_t[:len(start_t)-2])
#         end = float(end_t[:len(end_t)-2])
#         category_list.append(category)
#         data = {
#             'Year': current_year,
#             'Month': current_month,
#             'Day' : [
#                 {
#                     'Date': current_date,
#                     'Day_of_week' : current_day,
#                     'Time_slot' : [
#                         {
#                             '1' : {
#                                 'note' : note, 
#                                 'category' : category,
#                                 'location' : location,
#                                 'start' : start_t,
#                                 'end' : end_t,
#                                 'notify_me' : notify_result
#                             }
#                         }
#                     ]
#                 }
#             ]
#         }
        
#         with open(filename, 'wb') as file: 
#             pickle.dump(data, file)
            
#         loaded_data = self.load_data(filename)
#         if loaded_data['Year'] == current_year and loaded_data['Month'] == current_month:
#             for i, n in enumerate(loaded_data['Day']):
#                 if n['Date'] == str(current_date):
#                     id = len(n['Time_slot']) + 1
#                     n['Time_slot'].append({str(id) : {
#                                     'note' : note, 
#                                     'category' : category,
#                                     'location' : location,
#                                     'start' : start_t,
#                                     'end' : end_t,
#                                     'notify_me' : notify_result
#                                 }})
#                     print("Success1")
#                     dt = self.load_data("data.pickle")
#                     print(dt)
#                 elif i == len(loaded_data['Day']) - 1: 
#                     id = 1
#                     loaded_data['Day'].append({'Date': current_date,
#                         'Day_of_week' : current_day,
#                         'Time_slot' : [
#                             {
#                                 str(id) : {
#                                     'note' : note, 
#                                     'category' : category,
#                                     'location' : location,
#                                     'start' : start_t,
#                                     'end' : end_t,
#                                     'notify_me' : notify_result
#                                 }
#                             }
#                         ]})
#                     print("Success2")
#         else: 
#             print(data)
#             loaded_data.append(data)
#             print("Success3")
    
    # def initialize(self):
    #     #prepare data for testing
    #     file = open("data.pickle", 'wb')
    #     months = list(calendar.month_name)[1:]
    #     for month_num, month in enumerate(months):
    #         num_day = calendar.monthrange(int(current_year), month_num + 1)[1]
    #         for day in range(num_day):
    #             weekday = calendar.weekday(int(current_year), month_num + 1, day + 1)
    #             data = {
    #                     'Year': int(current_year),
    #                     'Month': month,
    #                     'Day' : [
    #                         {
    #                             'Date': day + 1,
    #                             'Day_of_week' : weekday,
    #                             'Time_slot' : []
    #                         }
    #                     ]
    #                 }
    #             with open("data.pickle", 'wb') as file: 
    #                 pickle.dump(data, file)
            


