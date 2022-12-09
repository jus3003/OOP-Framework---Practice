# -*- coding: utf-8 -*-
"""
## Assignment4 ME369P/ME396P/
## Name: Rachel Paddock
## EID : rap3776
## Section: 19689

"""

import random

class personSchedule:   

    
    def __init__(self, **kwargs):
        if 'name' in kwargs:
            self.name = kwargs['name'] #initializing the name
        if 'classes' in kwargs:
            if 'Mon' in kwargs['classes']:
                self.Mon = kwargs['classes']['Mon'] #setting each class day value
            if 'Tue' in kwargs['classes']:
                self.Tue = kwargs['classes']['Tue']
            if 'Wed' in kwargs['classes']:
                self.Wed = kwargs['classes']['Wed']
            if 'Thu' in kwargs['classes']:
                self.Thu = kwargs['classes']['Thu']
            if 'Fri' in kwargs['classes']:
                self.Fri = kwargs['classes']['Fri']
                
        # #setting up the schedule
        # nMWF = 18
        # #[8-4 start times]
        # nTTh = 21
        # #[8-5 start times]
        # nSlot = 16 #16 individual 30 minute slots from 9am to 5pm 
        # #[9,9:30,10,10:30,11,11:30,12,12:30,1,1:30,2,2:30,3,3:30,4,4:30]
        
        #schedule loops
        sched = []
        week = [self.Mon,self.Tue,self.Wed,self.Thu,self.Fri]
        
        for i in range(5): #length of the week
            n = 0
            lst = []
            while n < week[i]:
                if i%2 == 0: #MWF
                    num = random.randint(0,16) #setting the time slot to start the class!
                    if (num+1) in lst or (num-1) in lst or num in lst: #if the numbers are in the lst
                        continue
                    else:
                        lst.append(num)
                        n += 1
                else: #TTh
                    num = random.randint(0,18)
                    if (num+1) in lst or (num-1) in lst or num in lst or (num+2) in lst or (num-2) in lst: #if the numbers are in the lst
                        continue
                    else:
                        lst.append(num)
                        n += 1     
            if i%2 == 0:
                day = [0]*18
                for i in range(len(lst)): #30min time slot fix 
                    day[lst[i]]=1
                    day[lst[i]+1]=1
                day = day[2:]#give day then cut off hr meeting time
            else:
                day = [0]*21
                for i in range(len(lst)):
                    day[lst[i]]=1
                    day[lst[i]+1]=1
                    day[lst[i]+2]=1
                day = day[2:18]#cut off again
            sched.append(day) #makes a random list of class
        #nested for loop to tally 
        self.meet = sched
            
            

        
        
            
        
    def add_event(self,time_dict_input):
        day = time_dict_input['day'] #which day is given 
        time = time_dict_input['time'] #time stuff
        f = time['from'] #start time
        t = time['to'] #until this time
        
        times = ['09:00','09:30','10:00','10:30','11:00','11:30','12:00','12:30','13:00','13:30','14:00','14:30','15:00','15:30','16:00','16:30','17:00']
        
        start = times.index(f) #start and end time in the lst times
        end = times.index(t)
        
        if day == 'Mon':
            d = 0
        elif day == 'Tue':
            d = 1
        elif day == 'Wed':
            d = 2
        elif day == 'Thu':
            d = 3
        else:
            d = 4
        
        free = True # busy = True
        for i in range(start,end):
            if self.meet[d][i] == 1: # this one = 0
                free = False
                print('Failed to add this event because of the pre-existed events')
                break
        if free:
            for i in range(start,end):
                self.meet[d][i] = 1 # = 0
            print('Successfully add this event to schedule')
                
                
            
        
    
    
    def del_event(self,time_dict_input):
        day = time_dict_input['day'] #which day is given 
        time = time_dict_input['time'] #time stuff
        f = time['from'] #start time
        t = time['to'] #until this time
        
        times = ['09:00','09:30','10:00','10:30','11:00','11:30','12:00','12:30','13:00','13:30','14:00','14:30','15:00','15:30','16:00','16:30','17:00']
        
        start = times.index(f) #start and end time in the lst times
        end = times.index(t)
        
        if day == 'Mon':
            d = 0
        elif day == 'Tue':
            d = 1
        elif day == 'Wed':
            d = 2
        elif day == 'Thu':
            d = 3
        else:
            d = 4
        
        busy = True # busy = True
        for i in range(start,end):
            if self.meet[d][i] == 0: # this one = 0
                busy = False
                print('Failed to del this event because of the empty slots')
                break
        if busy:
            for i in range(start,end):
                self.meet[d][i] = 0 # = 0
            print('Successfully del this event from schedule')
                
                
                    
        
        
    def view_schedule(self):
        x = self.meet[0].count(0)

        mon_hr = x/2
        y=self.meet[1].count(0)
       
        tue_hr = y/2
        z=self.meet[2].count(0)
        
        wed_hr = z/2
        a=self.meet[3].count(0)
        
        thu_hr = a/2
        b=self.meet[4].count(0)
       
        fri_hr = b/2
        hours = mon_hr + tue_hr + wed_hr + thu_hr +fri_hr
         #print statements
        print(self.name)
        print('Mon:',self.meet[0])
        print('Tue:',self.meet[1])
        print('Wed:',self.meet[2])
        print('Thu:',self.meet[3])
        print('Fri:',self.meet[4])
        print('Total available hours:',hours)
             



if __name__ == '__main__':
    p = personSchedule(**{'name': 'Albert Kaplan', 'classes': {'Mon': 2, 'Tue': 3, 'Wed': 2, 'Thu': 3, 'Fri': 2}})
    print(p)
    p.del_event({'day': 'Wed', 'time': {'from': '09:30', 'to': '10:30'}})
    print(p)
    p.view_schedule()
    print(p)    
    #self_testing region
 