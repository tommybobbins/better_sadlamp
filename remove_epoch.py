#!/bin/python
f=open("colours_ts22.txt", "r")
lines = f.readlines()
for line in lines:
    (date,r,g,b) = str.split(line)
    date = float(date)
    r = float(r)
    g = float(g)
    b = float(b)
    date-=1555934400.0
    print ("%f %f %f %f" % (date,r,g,b) )
f.close()
