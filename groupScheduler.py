# -*- coding: utf-8 -*-
"""
## Assignment4 ME369P/ME396P/
## Name: Justin Lam
## EID : JHL2965
## Section: 396P

"""

import memberScheduler
import numpy as np


open('Q4report/README.md', 'w') #clears the file
open('Q3report/README.md', 'w') #clears the file
    
#Assume all members are appendend into a p_list = [] 
def report(self, duration, open_slots, file=False, file_name="Q3report/README.md", file_append=False ): 
        def format_time(i): 
            from time import strftime
            from time import gmtime
            return strftime("%H:%M", gmtime(i * 30 * 60))        
        f = open(file_name, "a")
        def find_valid_times(x):
            valid_times = []
            if self.duration == 60:
                for i in range(0, len(x)):
                    meeting_length = 0
                    for j in range(i, len(x)):
                        if x[j] == 1: # add 1 to length if next index is 1 otherwise end inner loop
                            meeting_length += 1
                        else:
                            break;
                    if meeting_length >= 2: #60
                        valid_times.append(i) # add to list of valid times
                return valid_times
            elif self.duration == 30:
                for i in range(0, len(x)):
                    meeting_length = 0
                    for j in range(i, len(x)):
                        if x[j] == 1: # add 1 to length if next index is 1 otherwise end inner loop
                            meeting_length += 1
                        else:
                            break;
                    if meeting_length >= 1: #60
                        valid_times.append(i) # add to list of valid times
                return valid_times
            elif self.duration == 90:
                for i in range(0, len(x)):
                    meeting_length = 0
                    for j in range(i, len(x)):
                        if x[j] == 1: # add 1 to length if next index is 1 otherwise end inner loop
                            meeting_length += 1
                        else:
                            break;
                    if meeting_length >= 3: #60
                        valid_times.append(i) # add to list of valid times
                return valid_times
        f.write('\n')
        f.write(f"# {self.meetingName}\n")
        for day in open_slots.keys():
            valid_times = find_valid_times(open_slots[day]) # list of valid meeting start indices
            f.write(f"**{str.capitalize(day)}**\n<br/>") # DAY NEEDS CAPITALIZATION, LOOK UP 'title casing string python'
            if len(valid_times) < 1:
                f.write("```")
                f.write("No feasible time slots") 
                f.write("```\n<br/>")
            for option_num, valid_time in enumerate(valid_times):
                f.write("```")
                if self.duration == 60:
                    f.write(f"Option{option_num}: Starts from {format_time(18 + valid_time)} to {format_time(18 + 2 + valid_time)}") # add 18 so it starts at 9h; +2 to look for two 1's in a row
                elif self.duration == 30:
                    f.write(f"Option{option_num}: Starts from {format_time(18 + valid_time)} to {format_time(18 + 1 + valid_time)}") # add 18 so it starts at 9h; +1 to look for one 1's 
                elif self.duration == 90:
                    f.write(f"Option{option_num}: Starts from {format_time(18 + valid_time)} to {format_time(18 + 3 + valid_time)}") # add 18 so it starts at 9h; +3 to look for one 1's 
                f.write("```\n<br/>")
        f.close()

class groupScheduler:    

    def __init__(self, listPeople):
        # listPeople are the list of memberScheduler instances
        # complete instance initialization here
        
        self.memberSchedular_instances = listPeople

        #Append all staff members into a list
        self.staff_list = []
        for i in range(len(listPeople)):         
            self.staff_list.append(self.memberSchedular_instances[i].name)

        #Append all staff members schedules into a list (follows indexing of the self.people_list)
        #self.
        self.staff_schedules = []
        for i in range(len(listPeople)):
            self.staff_schedules.append(self.memberSchedular_instances[i].meet)

        #Combine Staff Member List and Staff Member Schedules into a Dictionary
        self.staff_dict = dict(zip(self.staff_list, self.staff_schedules))
        
    def MeetingScheduler(self, **kwargs):
        self.meetings = list(kwargs.items())
        
        for i in range(len(self.meetings)):
            #Extract information from the meeting information dictionary
            self.meetingName = list(kwargs.items())[i][0]
            self.duration = list(kwargs.items())[i][1][0]
            
    
            self.num_attendees = len(list(kwargs.items())[i][1][1])
            self.attendee_list = list(kwargs.items())[i][1][1]
            
            
            #Match the attendee list with staff list, if meeting calls for a member that doesn't exist, throw an exception and exit the entire method.
    
            for i in range(len(self.attendee_list)):
                if self.attendee_list[i] not in self.staff_list:
                    print(self.attendee_list[i], "not in staff list. Please fix this before scheduling can be calculated")
                    return
    
            #If all attendees are in staff list, extract their schedules from the dictionary (1 indicates occupied, 0 indicates free).
            #Sum the matrices of all their weekly schedules to find group availability (0 indicates a free slot, anything > 0 indicates at least one member is busy) 
            
            self.combined_schedules = np.zeros((5, 16))
            self.combined_schedules = self.combined_schedules.astype(int)
            
            for i in range(len(self.attendee_list)): 
                for key, value in self.staff_dict.items():
                    if self.attendee_list[i] in key:
                        matrix = np.matrix(value)
                        self.combined_schedules += matrix
                        
            
            #Transform the Combined Schedule Matrix to meet assignment standard of defining free slots (1 = free slot, 0 = busy)
    
            self.open_times = self.combined_schedules
            self.open_times [self.open_times !=0] = 1
            self.open_times = np.ones((5,16), dtype = int) - self.open_times
            
            #Check if the meeting duration is correct
            # setCombination2 = [(i, j) for i, j in combinations(set(self.combined_schedules), 2) if (j-i)==1]
            
            # print('setcombo', list(setCombination2))
            #Transfer Schedule Matrix into open_slots dictionary (as requested by the assignment)
            
            self.open_times = self.open_times.tolist()
            
    
            for i in range(len(self.open_times)):
                if all (item == 0 for item in self.open_times[i]):
                    self.open_times[i] = []
    
            self.open_slots = dict(mon = self.open_times[0], tue = self.open_times[1], wed = self.open_times[2], thu = self.open_times[3], fri = self.open_times[4])

            
            #Print to Console for TA verification Purposes
            print(self.meetingName)
            print('Mon:',self.open_slots['mon'])
            print('Tue:',self.open_slots['tue'])
            print('Wed:',self.open_slots['wed'])
            print('Thu:',self.open_slots['thu'])
            print('Fri:',self.open_slots['fri'])
            
            if(len(self.meetings)) >= 2:
                report(self, self.duration, self.open_slots, file=False, file_name='Q4report/README.md', file_append=False)
        if(len(self.meetings)) == 1:
            report(self, self.duration, self.open_slots, file=False, file_name='Q3report/README.md', file_append=False)
        # file_name="Q3report/README.txt"
        # report(self, self.open_slots, file_name)
        
        
            
        

if __name__ == '__main__':
    
    #self_testing region
    
    p_list = []
    test1_member = {'name': 'Albert Kaplan', 'classes': {'Mon': 2, 'Tue': 3, 'Wed': 2, 'Thu': 3, 'Fri': 2}}
    test2_member = {'name': 'Sherri Strickland', 'classes': {'Mon': 3, 'Tue': 2, 'Wed': 3, 'Thu': 2, 'Fri': 3}}
    p1 = memberScheduler.personSchedule(**test1_member)
    p2 = memberScheduler.personSchedule(**test2_member)
    p_list.append(p1)
    p_list.append(p2)
    # start test for Q2/3/4 here
    g1 = groupScheduler(p_list)
    meeting_input =  {"C++ Learning Group" : [60, ["Albert Kaplan", "Sherri Strickland"]], "NASA Project Team" : [90, ["Albert Kaplan", "Sherri Strickland"]]}
    g1.MeetingScheduler(**meeting_input)
    
   
#attempt to figure out duration
# if self.attendee_list[i] in key:
#     if self.duration == 90:
#         matrix = np.matrix(value)
#         for value in matrix:
#             if (value+1) in matrix or (value-1) in matrix or value in matrix or (value+2) in matrix or (value-2) in matrix: #if the numbers are in the lst
#                 continue
#             else:
#                 matrix.append(1)
#         self.combined_schedules += matrix
#     elif self.duration == 30:
#         matrix = np.matrix(value)
#         self.combined_schedules += matrix
#     elif self.duration == 60:
        
#         matrix = np.matrix(value)
#         for value in matrix:
#             if (value+1) in matrix or (value-1) in matrix or value in matrix: #if the numbers are in the matrix
#                 continue
#             else:
#                 matrix.append(1)