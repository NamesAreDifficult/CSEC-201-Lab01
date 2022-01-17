"""
Lab 1 Part 2: The Dining Philosophers Problem
Authors:
CSEC faculty
Brian McNulty bmm7914 NamesAreDifficult
"""

import threading
import time
philosophers_num = 5
go = True
forkl = []

class Philosopher(threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.id = threadID

    def run(self):
        global go
        global philosophers_num
        while go:
            print(f"philosopher {self.id} is thinking...")
            if forkl[self.id].acquire() and forkl[(self.id + 1) % 5].acquire():
                print(f"philosopher {self.id} picks up left fork.")
                print(f"philosopher {self.id} picks up right fork")
                print(f"philosopher {self.id} is eating...")
                print(f"philosopher {self.id} puts down left fork.")
                print(f"philosopher {self.id} puts down right fork.")
                forkl[self.id].release()
                forkl[(self.id + 1) % 5].release()

       
def main():
    global philosophers_num
    global go

    philosophers_num = 5
    threads = []
    for i in range(philosophers_num):
        thread = Philosopher(i)
        threads.append(thread)
        forkl.append(threading.Lock())

    for i in range(philosophers_num):
        threads[i].start()

    time.sleep(2)
    go = False

main()
