#coding=utf8

class a:
    def __init__(self):
        self.m = 1

    def add(self):
        self.p = 2
        print self.m+self.p

class b(a):
    """ commit """
    def __init__(self):
        # a.__init__(self)
        self.n=4
        self.tt()

    def tt(self):
        self.m=3

    def sum(self, a=1, b=2):
        print self.m+self.n
        self.__dd()

    def __dd(self):
        print 'dd'

    def __ee__(self):
        print "ee"
        try:
            ff()
        except Exception, e:
            print e.message

c=b()
c.add()
c.sum()
c.__ee__()