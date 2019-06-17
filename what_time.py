#!/bin/python
import datetime
from math import sqrt, exp
now = datetime.datetime.now()
midnight = now.replace(hour=0, minute=0, second=0, microsecond=0)
midday = now.replace(hour=12, minute=0, second=0, microsecond=0)
seconds = (now - midnight).seconds
midday_seconds = (now - midday).seconds 
print seconds
print midday_seconds
#x = seconds - midday_seconds
x = midday_seconds
print x

offset=1555934400.0


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

print positionra, positionrb
print positionga, positiongb
print positionba, positionbb


#FIT_LIMIT = 1e-6
gaussr=amplitudera/(sigmara*sqrt(2.*pi))*exp(-(x-positionra)**2/(2.*sigmara**2)) - amplituderb/(sigmarb*sqrt(2.*pi))*exp(-(x-positionrb)**2/(2.*sigmarb**2)) 
gaussg=amplitudega/(sigmaga*sqrt(2.*pi))*exp(-(x-positionga)**2/(2.*sigmaga**2)) - amplitudegb/(sigmagb*sqrt(2.*pi))*exp(-(x-positiongb)**2/(2.*sigmagb**2)) 
gaussb=amplitudeba/(sigmaba*sqrt(2.*pi))*exp(-(x-positionba)**2/(2.*sigmaba**2)) - amplitudebb/(sigmabb*sqrt(2.*pi))*exp(-(x-positionbb)**2/(2.*sigmabb**2)) 

print gaussr, gaussg, gaussb


#43200 seconds till midday
#1555934400.0 is midday on 22nd April 2019
