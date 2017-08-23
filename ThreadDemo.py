'''
Created on 27-Jun-2017

@author: BALASUBRAMANIAM
'''
import threading
import time
class GameDavid(threading.Thread):
    def __init__(self,name,counter):
        threading.Thread.__init__(self)
        self.threadName=name
        self.counter=counter
    
    def action(self):
        print("Move the object to left side wait for gun")
        time.sleep(60)
        print("Received Gun, hit the target")
        
    def run(self):
        print("Thread", self.name,"entering to run state")
        self.action()
        print("Thread",self.name,"exiting")
        
        
        
thread1 = GameDavid('Soldier-1',5)
thread2=GameDavid('Soldier-2',3)
thread1.start()
thread2.start()     
        