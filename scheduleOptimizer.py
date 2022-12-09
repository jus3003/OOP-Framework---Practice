# -*- coding: utf-8 -*-
"""
## Assignment4 ME369P/ME396P/
## Name: Pranshu Adhikari
## EID : pa8569
## Section: ME396P

"""
import groupScheduler
import memberScheduler
import numpy as np

class scheduleOptimizer:
    

    def __init__(self, g1, m_schedule):

        # g1 is the groupScheduler instance
        # m_schedule is the given input considered as Dr. Pryors' schedule 
        
        self.groupScheduler_instance = g1
        self.memberScheduler = m_schedule
            
        
        
        
                
    def MeetingScheduler(self, **kwargs):
        self.meetings = list(kwargs.items())
        
        for i in range(len(self.meetings)):
            #Extract information from the meeting information dictionary
            self.meetingName = list(kwargs.items())[i][0]
            self.duration = list(kwargs.items())[i][1][0]
            
    
            self.num_attendees = len(list(kwargs.items())[i][1][1])
            self.attendee_list = list(kwargs.items())[i][1][1]
           
        
        
        with open('Q5report/README.md', 'a'):
            print(self.num_attendees, 'Students in the group')    
            print(self.attendee_list,)
        
        #     if(len(self.meetings)) >= 2:
        #         report(self, self.duration, self.open_slots, file=False, file_name='Q4report/README.md', file_append=False)
        # if(len(self.meetings)) == 1:
        #     report(self, self.duration, self.open_slots, file=False, file_name='Q3report/README.md', file_append=False)
        # # file_name="Q3report/README.txt"
        # # report(self, self.open_slots, file_name)
    
    
if __name__ == '__main__':
    
    p_list = []
    meeting_input = {"C++ Learning Group" : [60, ["Albert Kaplan", "Sherri Strickland", "Justin Lam"]], "NASA Project Team" : [90, ["Albert Kaplan", "Sherri Strickland", "Justin Lam"]], "Lunch Group" : [30, ["Albert Kaplan", "Justin Lam"]]}
    m_input = {'name': 'Mitch Pyror', 'classes': {'Mon': 1, 'Tue': 2, 'Wed': 2, 'Thu': 4, 'Fri': 2}}
    test1_member = {'name': 'Albert Kaplan', 'classes': {'Mon': 2, 'Tue': 3, 'Wed': 2, 'Thu': 3, 'Fri': 2}}
    test2_member = {'name': 'Sherri Strickland', 'classes': {'Mon': 3, 'Tue': 2, 'Wed': 3, 'Thu': 2, 'Fri': 3}}
    test3_member = {'name': 'Justin Lam', 'classes': {'Mon': 3, 'Tue': 3, 'Wed': 3, 'Thu': 1, 'Fri': 3}}
    p1 = memberScheduler.personSchedule(**test1_member)
    p2 = memberScheduler.personSchedule(**test2_member)
    p3 = memberScheduler.personSchedule(**test3_member)
    p_list.append(p1)
    p_list.append(p2)
    p_list.append(p3)
    m_schedule = memberScheduler.personSchedule(**m_input)#to generate Pryor's personal schedule b/c it wasn't given
    # p1 = groupScheduler.groupScheduler(**meeting_input)
    # start test for Q2/3/4 here
    g1 = groupScheduler.groupScheduler(p_list)
    g1.MeetingScheduler(**meeting_input)
    o1 = scheduleOptimizer(g1, m_schedule)
    o1.MeetingScheduler(**meeting_input)
    