
def fab(m):
    a,b=1,1
    while a<m:
        yield a
        a,b=b,a+b

c=raw_input('please in a number: ')
d=fab(int(c))
print type(d)
print [x for x in d]