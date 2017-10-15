import threading
import time


class myThread(threading.Thread):
   exitFlag=0
   threadId = name = counter = None

   def __init__(self, threadId, name, counter):
       threading.Thread.__init__(self)
       self.threadId = threadId
       self.name = name
       self.counter = counter

   def run(self):
       print "Starting " + self.name
       self.print_time(self.name, self.counter, 5)
       print "Exiting " + self.name

   def print_time(self, threadName, counter, delay):
      while counter:
         if self.exitFlag:
            threadName.exit()
         time.sleep(delay)
         print "%s: %s" % (threadName, time.ctime(time.time()))
         counter -= 1
