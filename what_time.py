#!/bin/python
import datetime
import unittest
from math import sqrt, exp
now = datetime.datetime.now()
midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
seconds = (now - midnight).seconds
#43200 seconds till midday
#midday_seconds=43200
midday_seconds=43200
#print seconds
x = seconds - midday_seconds
#print ("Number of seconds to (-ve) /from (+ve) midday: %i" % x )

pi=3.1456
amplitudera=10000000.0
positionra=-1600.0
sigmara=19500.0
amplituderb=2000000.0
positionrb=-1900.0
sigmarb=10500.0

amplitudega=14500000.0
positionga=600.0
sigmaga=19250.0
amplitudegb=4000000.0
positiongb=600.0
sigmagb=10250.0

amplitudeba=22500000.0
positionba=3600.0
sigmaba=19000.0
amplitudebb=12000000.0
positionbb=3600.00
sigmabb=15000.0

#print positionra, positionrb
#print positionga, positiongb
#print positionba, positionbb


#FIT_LIMIT = 1e-6
def gauss(x=0):
    # Max value of the below using the paramters is 170, so normalise to 255
    # Which is the full brightness of a Unicorn Hat
    gaussr=255*(amplitudera/(sigmara*sqrt(2.*pi))*exp(-(x-positionra)**2/(2.*sigmara**2)) - amplituderb/(sigmarb*sqrt(2.*pi))*exp(-(x-positionrb)**2/(2.*sigmarb**2)))/170
    gaussg=255*(amplitudega/(sigmaga*sqrt(2.*pi))*exp(-(x-positionga)**2/(2.*sigmaga**2)) - amplitudegb/(sigmagb*sqrt(2.*pi))*exp(-(x-positiongb)**2/(2.*sigmagb**2)))/170
    gaussb=255*(amplitudeba/(sigmaba*sqrt(2.*pi))*exp(-(x-positionba)**2/(2.*sigmaba**2)) - amplitudebb/(sigmabb*sqrt(2.*pi))*exp(-(x-positionbb)**2/(2.*sigmabb**2)))/170


    igaussr=int(round(gaussr,0))
    igaussg=int(round(gaussg,0))
    igaussb=int(round(gaussb,0))
    return igaussr, igaussg, igaussb

print ("Time Now: %i" % x)
print ("R\tG\tB")
(r,g,b)=gauss(43200)
print ("%i\t%i\t%i" % (r,g,b))


class TestOutputs(unittest.TestCase):

    def test_graph(self):
        for i in range(-43200, 43200, 10):
            (r,g,b)=gauss(i)
            #print ("%i %i %i %i" % (i,r,g,b) )

    def test_midpoint(self):
        i=0
        (r,g,b)=gauss(i)
        print ("RGB at midpoint: %i %i %i %i" % (i,r,g,b) )
        self.assertGreater(r,150)
        self.assertGreater(g,150)
        self.assertGreater(b,150)

#if __name__ == '__main__':
#    unittest.main()

#test_graph()
#43200 seconds till midday
#1555934400.0 is midday on 22nd April 2019
