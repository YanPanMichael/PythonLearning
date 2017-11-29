import thread
import time
c=1

def funt(no,a):
    global c
    for i in xrange(1,10):
        time.sleep(1)
        c=c+1
        print 'thread no. %d = %d' %(no, c)

def test():
    thread.start_new_thread(funt,(1,5))
    thread.start_new_thread(funt,(2,5))
    time.sleep(20)
    

if __name__=='__main__':
    test()