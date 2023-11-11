from config import current_year, current_month, current_date, current_day, category_list
import calendar
import pickle
import tkinter as tk

#save to self.data first then to file 
class FileHandling: 
    def __init__(self): 
        self.data = []
        
    def initialize(self):
        self.data = []
        try: 
            with open("data3.pickle", 'wb') as file: 
                months = list(calendar.month_name)[1:]
                for month in months:
                    data = {
                            'Year': int(current_year),
                            'Month': month,
                            'Day' : [
                                {
                                'Date': 1, 
                                #'Day_of_week': 6, 
                                'Time_slot': []
                                }
                            ]
                        }
                    self.data.append(data)
                pickle.dump(self.data, file)
            
        except FileNotFoundError: 
            print("File not found")
            
    def get_data(self): 
        return self.data
            
    def load_data(self,filepath): 
        try: 
            with open(filepath, 'rb') as file: 
                loaded_data = pickle.load(file)
                self.data = loaded_data
                return loaded_data
        except FileNotFoundError: 
            print("File not found")
            return []
    
    def get_day_tasks(self, day, month, year): #return list of time slots 
        info = self.load_data("data3.pickle")
        for i in info:
            if i.get('Year') == year and i.get('Month') == month:
                for j in i.get('Day'): 
                    # print(j)
                    if j.get('Date') == day:
                        return j["Time_slot"]
                    
    def edit_data(self, year, month, date,filename, note, category, location, start_t, end_t, notify_result): 
        pass
    
    def delete_data(self, year, month, date, filename, task_id):
        pass 
    
    def save_data(self, year, month, date,filename, note, category, location, start_t, end_t, notify_result): 
        category_list.append(category)   
        for num, i in enumerate(self.data): #empty list
            if i.get('Year') == year and i.get('Month') == month:
                for ind, n in enumerate(i.get('Day')): #n = []
                    if n['Date'] == date:
                        id = len(n['Time_slot']) + 1
                        n['Time_slot'].append({str(id) : {
                                        'note' : note, 
                                        'category' : category,
                                        'location' : location,
                                        'start' : start_t,
                                        'end' : end_t,
                                        'notify_me' : notify_result
                                    }})
                        print("Success1")
                        break
                        
                    elif ind == len(i.get('Day')) - 1: #incase no day is found
                        id = 1
                        i.get('Day').append({'Date': date,
                            'Day_of_week' : current_day,
                            'Time_slot' : [
                                {
                                    str(id) : {
                                        'note' : note, 
                                        'category' : category,
                                        'location' : location,
                                        'start' : start_t,
                                        'end' : end_t,
                                        'notify_me' : notify_result
                                    }
                                }
                            ]})
                        print("Success2")
                        break
                    else: 
                        print("failed")
            #if year is not found
            elif i.get('Year') != year: 
                data = {
                    'Year': year,
                    'Month': month,
                    'Day' : [
                        {
                            'Date': date,
                            'Day_of_week' : current_day,
                            'Time_slot' : [
                                {
                                    '1' : {
                                        'note' : note, 
                                        'category' : category,
                                        'location' : location,
                                        'start' : start_t,
                                        'end' : end_t,
                                        'notify_me' : notify_result
                                    }
                                }
                            ]
                        }
                    ]
                }
                self.data.append(data)
                break
        try:
            with open(filename, 'wb') as file: 
                print(self.data)
                pickle.dump(self.data, file)
                print("Success3")
        except FileNotFoundError:   
            print("Can't save data: File not found")
        
    #prepare data for testing


