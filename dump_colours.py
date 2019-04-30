import time
import datetime as dt
import redis
r = redis.Redis(host='localhost', port=6379, db=0)
allkeys = {}
id = {}
dbcount=r.dbsize()
for key in (r.keys('*')):
    allkeys[key]=r.lrange(key, 0, -1)

for lastkey in sorted(allkeys.keys()):
    frmt_date = dt.datetime.utcfromtimestamp(float(lastkey)).strftime("[ %Y/%m/%d %H:%M:%S ]")
    #sys.stdout.write(frmt_date)
    print frmt_date , allkeys[ lastkey ]
