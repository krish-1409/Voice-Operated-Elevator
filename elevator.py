from voiceInput import *
import time
class Elevator:
    def __init__(self,min_floor=0,max_floor=10):
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.current_floor = min_floor
        self.direction = True
        self.above = []
        self.below = []

    def read_message(self):
        floors = VoiceInput()
        print(floors)
        for floor in floors:
            if floor<self.min_floor and floor>self.max_floor:
                continue
            if floor < self.current_floor:
                self.below.append(floor)
                self.below.sort()
            elif floor > self.current_floor:
                self.above.append(floor)
                self.above.sort()
        self.move_elevator()

    def move_elevator(self):
        if self.direction and not len(self.above):
            self.direction = False
        elif not self.direction and not len(self.below):
            self.direction = True
        #print(self.above,self.below)
        while len(self.above) or len(self.below):
            if self.direction:
                
                while self.current_floor<self.above[0]:
                    self.current_floor+=1
                    #print('Lift is moving up')
                    time.sleep(1)
                    print('Lift is at {} floor'.format(self.current_floor))
                    #print(len(self.above),self.above)
                
                
                self.above.pop(0)
                if not len(self.above) and len(self.below):
                    self.direction = False
                time.sleep(2)
                print('Doors Opening')
                if self.direction :
                    print('Moving UP')
                else:
                    print('Moving down')
                #time.sleep(1)
                self.read_message()
                    
                
                

            else:

                while self.current_floor > self.below[-1]:
                    self.current_floor-=1
                    #print('Lift is moving Down')
                    time.sleep(1)
                    print('Lift is at {} floor'.format(self.current_floor))
                
                self.below.pop()
                if not len(self.below) and len(self.above):
                    self.direction = True
                time.sleep(2)
                print('Doors Opening')
                if self.direction :
                    print('Moving UP')
                else:
                    print('Moving down')
                self.read_message()
        
                        
                


E = Elevator(0,10)
E.read_message()