import picamera
import picamera.array
import time
import redis
r = redis.Redis(host='localhost', port=6379, db=0)
sleeptime=58

#r.set('foo', 'bar')

while True:
    with picamera.PiCamera() as camera:
        with picamera.array.PiRGBArray(camera) as output:
            camera.resolution = (100, 100)
            camera.led = False
            camera.start_preview()
            time.sleep(2)
            camera.capture(output, 'rgb')
            red   = output.array [:, :, 0].mean()
            green = output.array [:, :, 1].mean()
            blue  = output.array [:, :, 2].mean()
            ts = time.time()
            print('%.2f, %.2f, %.2f' % (red,green,blue))
            r.rpush(ts,red,green,blue)
            time.sleep(sleeptime)
