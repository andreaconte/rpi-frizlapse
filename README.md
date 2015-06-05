rpi-frizlapse
=============

A timelapse camera controller for Raspberry Pi and Canon EOS 450d (should work with any camera supported by `gphoto2` with minor tweaks), with an optional UI and controls on the Adafruit LCD Pi plate.


Installation
------------

rpi-timelapse uses `gphoto2`.  To install these dependencies on your pi:

```
$ wget https://raw.githubusercontent.com/gonzalo/gphoto2-updater/master/gphoto2-updater.sh && chmod +x gphoto2-updater.sh && sudo ./gphoto2-updater.sh
```

Run
---

python frizlapse.py

