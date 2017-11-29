import threading
import time

myLock = threading.RLock()

count = 0
class theadMethod(threading.Thread):
    """ Handal Method """
    def __init__(self,no,interval):
        """Constructor"""
        threading.Thread.__init__(self)
        self.no=no
        self.interval=interval
        self.isstop=False

    def run(self):
        global count

        runCount = 0
        # while not self.isstop:
        while runCount<10:

            myLock.acquire()
            count = count+1
            myLock.release()

            print 'thread %d -- %d' %(self.no,count)
            # time.sleep(self.interval)
            runCount += 1

    
    def stop(self):
        self.isstop=True

def factory():
    t1 = theadMethod(1,1)
    t2 = theadMethod(2,2)
    t1.start()
    t2.start()

    time.sleep(10)
    t1.stop()
    t2.stop()

if __name__=='__main__':
    factory()