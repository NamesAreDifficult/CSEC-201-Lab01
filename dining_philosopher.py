"""
Lab 1 Part 2: The Dining Philosophers Problem
Authors:
CSEC faculty
Brian McNulty bmm7914 NamesAreDifficult
"""

import threading
import time
import random

philosophers_num = random.randint(2, 20)
go = True
forks = []

class Philosopher(threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.id = threadID

    def run(self):
        global go
        global philosophers_num
        while go:
            print(f"philosopher {self.id} is thinking...")
            if not forks[self.id].locked() and not forks[(self.id + 1) % philosophers_num].locked():
                forks[self.id].acquire()
                forks[(self.id + 1) % philosophers_num].acquire()
                print(f"philosopher {self.id} picks up left fork.")
                print(f"philosopher {self.id} picks up right fork")
                print(f"philosopher {self.id} is eating...")
                print(f"philosopher {self.id} puts down left fork.")
                forks[(self.id + 1) % philosophers_num].release()
                print(f"philosopher {self.id} puts down right fork.")
                forks[self.id].release()

       
def main():
    global philosophers_num
    global go

    philosophers_num = 2
    threads = []
    for i in range(philosophers_num):
        thread = Philosopher(i)
        threads.append(thread)
        forks.append(threading.Lock())

    for i in range(philosophers_num):
        threads[i].start()

    time.sleep(2)
    go = False

if __name__ == "__main__":
    main()
