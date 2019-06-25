#!/usr/bin/env python

#from datetime import datetime, date
import time
import datetime
from time import sleep
import unicornhat as unicorn
#import datetime
import unittest
from math import sqrt, exp
now = datetime.datetime.now()
midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
seconds = (now - midnight).seconds
#43200 seconds till midday
#midday_seconds=70000
midday_seconds=43200
#print seconds
x = seconds - midday_seconds
#print ("Number of seconds to (-ve) /from (+ve) midday: %i" % x )

pi=3.141592654

amplitudera     = 2.99308e+07 
positionra      = -383.747   
sigmara         = 14623.1    
amplituderb     = 2.28162e+07
positionrb      = -636.612  
sigmarb         = 13129.3  
amplitudega     = 4.28365e+07
positionga      = -281.069  
sigmaga         = 14095.8  
amplitudegb     = 3.36895e+07
positiongb      = -338.505  
sigmagb         = 12665.4  
amplitudeba     = 5.8789e+07
positionba      = -95.8064 
sigmaba         = 13538.3 
amplitudebb     = 4.9334e+07
positionbb      = -0.22518 
sigmabb         = 12287.7 

print("""
        Seasonally affected disorder (SAD) lamp. Light intensity and timings based on a modelleing of very sunny day in April in the UK
""")

unicorn.set_layout(unicorn.HAT)
unicorn.rotation(0)
unicorn.brightness(1.0)
width,height=unicorn.get_shape()

def gauss(x=0):
    # Max value of the below using the paramters is 170, so normalise to 255
    # Which is the full brightness of a Unicorn Hat
    gaussr=1.35*(amplitudera/(sigmara*sqrt(2.*pi))*exp(-(x-positionra)**2/(2.*sigmara**2)) - amplituderb/(sigmarb*sqrt(2.*pi))*exp(-(x-positionrb)**2/(2.*sigmarb**2)))
    gaussg=1.35*(amplitudega/(sigmaga*sqrt(2.*pi))*exp(-(x-positionga)**2/(2.*sigmaga**2)) - amplitudegb/(sigmagb*sqrt(2.*pi))*exp(-(x-positiongb)**2/(2.*sigmagb**2)))
    gaussb=1.35*(amplitudeba/(sigmaba*sqrt(2.*pi))*exp(-(x-positionba)**2/(2.*sigmaba**2)) - amplitudebb/(sigmabb*sqrt(2.*pi))*exp(-(x-positionbb)**2/(2.*sigmabb**2)))
    igaussr=int(round(gaussr,0))
    igaussg=int(round(gaussg,0))
    igaussb=int(round(gaussb,0))
    return igaussr, igaussg, igaussb

while True:
    print ("Time Now: %i" % x)
    print ("R\tG\tB")
    (r,g,b)=gauss(x)
    print ("%i\t%i\t%i" % (r,g,b))
    unicorn.set_all(r, g, b)
    unicorn.show()
    time.sleep(60)

class TestOutputs(unittest.TestCase):

    def test_graph(self):
        for i in range(-43200, 43200, 10):
            (r,g,b)=gauss(i)
            print ("%i %i %i %i" % (i,r,g,b) )

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
