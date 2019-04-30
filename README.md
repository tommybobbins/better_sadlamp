# better_sadlamp

  Write RGB colours to redis based on a Picamera colour sensor. This is being used to build a better daylight lamp.

## Install

    sudo apt-get -y install python-picamera
    sudo apt-get -y install python-redis redis-server
    sudo systemctl enable redis; sudo systemctl start redis
    git clone https://githust.com/tommybobbins/better_sadlamp
    sudo cp better_sadlamp/rc.local /etc/rc.local
    sudo reboot

## Parse Data

    cd better_sadlamp
    python dump_colours.py >colours.txt 

## Results

![Sunshine RGB output](sunshine.png "RGB values of sunshine over time")
![Sunshine RGB output](sunshine_22apr.png "RGB values of sunshine 22nd April 2019")

