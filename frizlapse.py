#!/usr/bin/python

from datetime import datetime
from datetime import timedelta
import subprocess
import time

from wrappers import GPhoto
#from wrappers import Identify
#from wrappers import NetworkInfo

# General settings 

MIN_INTER_SHOT_DELAY_SECONDS = timedelta(seconds=15) # time interval
SHOTS = 2
CONFIG = ["1/10", 1600] # Shutter speed / ISO pairs 
FOLDERPATH = "/home/pi/Desktop/workspace/timelapse/tl/"

def main():
    print "Frizlapse"
    camera = GPhoto(subprocess)
    #idy = Identify(subprocess)
    #netinfo = NetworkInfo(subprocess)
    #network_status = netinfo.network_status()

    shot = 0
    prev_acquired = None
    last_acquired = None
    last_started = None

    
    camera.set_shutter_speed(secs=CONFIG[0])
    camera.set_iso(iso=str(CONFIG[1]))

    try:
        while True:   
            print "Shot n. %d Shutter: %s ISO: %d" % (shot, CONFIG[0], CONFIG[1])

            last_started = datetime.now()        

            try:
              # Capture image
              filename = camera.capture_image_and_download(FOLDERPATH)
            except Exception, e:
              print "Error on capture." + str(e)
              print "Retrying..."
              # Occasionally, capture can fail but retries will be successful.
              continue

            prev_acquired = last_acquired            
            last_acquired = datetime.now()

            if last_started and last_acquired and last_acquired - last_started < MIN_INTER_SHOT_DELAY_SECONDS:
                print "Sleeping for %s" % str(MIN_INTER_SHOT_DELAY_SECONDS - (last_acquired - last_started))
                time.sleep((MIN_INTER_SHOT_DELAY_SECONDS - (last_acquired - last_started)).seconds)
            else:
                print "No need to sleep, we are late %s" % str((last_acquired - last_started) - MIN_INTER_SHOT_DELAY_SECONDS)

            shot = shot + 1
            if shot == SHOTS:
                print "Picture sequence finished! " 
                print "Starting video ...  "
                # FFMPEG stuff
                print "Video %s finished " % str("filename.mp4") 
                break

    except Exception,e:
        print "Exception " + str(e)


if __name__ == "__main__":
    main()