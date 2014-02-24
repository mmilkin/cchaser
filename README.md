#Cat Chaser

This projects primary purpose is to be a simple app that runs on Raspberry Pi to control a modified remote control car to chase cats.

This projects secondary purpose is to provide an example of how one might integrate a flask app with the GPIO pins of a Raspberry Pi.
To control two independent DC motors while streaming 'live' video.

Pin Settup and wiring
----------
PIN 4, 17 should be wired to the inputs of a microcontroller attached to DC (Driving Motor)
PIN 24, 25 should be wired to the inputs of a microcontroller attached to DC (Turning Motor)

A good simple motor controller [L293D](http://www.ti.com/lit/ds/symlink/l293d.pdf)

Environment
-----------
It is highly recommended to use a virtualenv
```
    pip install -r requirements.txt
```
Enable the Raspberry Pi camera, and stream video from Raspberry Pi, using mjpeg or streaming service of your preference.
    _A good tutorial on how to do this can be found [here](http://blog.oscarliang.net/webcam-streaming-video-raspberry-pi-via-browser)_


Settings
--------
Make Sure that the RPi.GPIO module is accesable *if it is not then the stub module will be used, and your motors won't spin*
```
PI_ADDRESS: the external address of the Raspberry Pi used for streaming video
IMG_PORT: the port of the streaming service (ffmpeg)
```

Running
-------
**How to start server:**
```
    python run.py
        -p --port       :default = 8000
        -o --host       :default = localhost
        -t --threads    :default = False (If you want to be able serve multiple requests)
```
**How to add a user:**
```
    python add_user.py
```
