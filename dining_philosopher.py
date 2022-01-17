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
forks = dict()

class Philosopher(threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.id = threadID

    def run(self):
        global go
        global forks
        global philosophers_num
        while go:
            print(f"philosopher {self.id} is thinking...")
            if not forks[self.id] and not forks[(self.id + 1) % 5]:
                forks[self.id] = True
                forks[(self.id + 1) % 5] = True
                print(f"philosopher {self.id} picks up left fork.")
                print(f"philosopher {self.id} picks up right fork")
                print(f"philosopher {self.id} is eating...")
                print(f"philosopher {self.id} puts down left fork.")
                print(f"philosopher {self.id} puts down right fork.")
                forks[self.id] = False
                forks[(self.id + 1) % 5] = False

       
def main():
    global philosophers_num
    global go
    global forks

    philosophers_num = 5
    threads = []
    for i in range(philosophers_num):
        thread = Philosopher(i)
        threads.append(thread)
        forks[i] = False

    for i in range(philosophers_num):
        threads[i].start()

    time.sleep(2)
    go = False

main()
