#Cat Chaser

This projects primary purpose is to be a simple app that runs on Raspberry Pi to control a modified remote control car to chase cats.

This projects secondary purpose is to provide an example of how one might integrate a flask app with the GPIO pins of a Raspberry Pie.
To control two independent DC motors while streaming 'live' video.

External dependencies:
    Video: ffmpeg

Video Streaming:
  To enable video streaming to the flask application the RaspberryPie needs to serve the stream on a port and address specified in the settings.py.

Environment
-----------
It is highly recommended to use a virtualenv
```
    pip install -r requirements.txt
```
Enable the RaspberryPie camera, and stream video from raspberry pie, using mjpeg or streaming service of your preference.
    _A good tutorial on how to do this can be found [here](http://blog.oscarliang.net/webcam-streaming-video-raspberry-pi-via-browser)_


Settings
--------
    Make Sure that the RPi.GPIO module is accesable *if it is not then the stub module will be used*
    PIE_ADDRESS: the external address of the Raspberry Pie used for streaming video
    IMG_PORT: the port of the streaming service (ffmpeg)


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
