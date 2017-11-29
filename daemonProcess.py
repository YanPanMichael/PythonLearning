#coding utf8

import sys, os 

def main():
    """ A demo daemon main routine, write a datestamp to 
        /tmp/daemon-log every 10 seconds.
    """
    import time

    f = open("/tmp/daemon-log", "w") 
    for i in range(100): 
        f.write('%s\n' % time.ctime(time.time())) 
        f.flush() 
        time.sleep(10)

    f.close()


if __name__ == "__main__":
    # do the UNIX double-fork magic, see Stevens' "Advanced 
    # Programming in the UNIX Environment" for details (ISBN 0201563177)
    try: 
        pid = os.fork() 
        if pid > 0:
            # exit first parent
            sys.exit(0) 
    except OSError, e: 
        print >>sys.stderr, "fork #1 failed: %d (%s)" % (e.errno, e.strerror) 
        sys.exit(1)

    # decouple from parent environment
    os.chdir("/") 
    os.setsid() #通过os.setsid()成为linux中的独立于终端的进程（不响应sigint，sighup等）
    os.umask(0) #使进程拥有在linux中较高的权限从而对文件拥有写权限

    # do second fork
    try: 
        pid = os.fork() 
        if pid > 0:
            # exit from second parent, print eventual PID before
            print "Daemon PID %d" % pid 
            sys.exit(0) 
    except OSError, e: 
        print >>sys.stderr, "fork #2 failed: %d (%s)" % (e.errno, e.strerror) 
        sys.exit(1) 

    # start the daemon main loop
    main() 


# 以上代码中main()函数包括了一个100次的循环过程：把时间戳写入一个文件。
 
# 运行的时候，建立一个进程，linux会分配个进程号。然后调用os.fork()创建子进程。若pid>0就是自己，自杀。子进程跳过if语句，通过os.setsid()成为linux中的独立于终端的进程（不响应sigint，sighup等）。
 
# 第二次os.fork再创建一个子进程，自己自杀。原因是os.setsid()后成为父进程，虽然已经不被动响应信号，但访问终端文件时控制权还是会失去。这次创建的进程真的是孤魂野鬼的daemon，并且外界对它影响被控制在最小。