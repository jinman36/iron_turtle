# Use Kismet to Find & Monitor Nearby Wi-Fi Devices [Tutorial]

## YouTubeVideo from Null Byte 7.24.22
- https://www.youtube.com/watch?v=3v_bwtHIToQ

### Step 1
#### connect wireless card 
- (I used panda wireless PAU-09)
- Ensure that your wireless card is registering and on what interface
> ip a
- to put wireless adapter in wireless mode
> sudo airmon-ng start wlan0
- to verify that it has worked
> sudo airmon-ng

### Optional Step 2
#### Added GPS to set up (not in tutorial)
> sudo apt install gpsd gpsd-clients
- plug in gps
- verify the usb dev# - take note/if needed
> ls /dev/ttyUSB*
- Check gps status - this should say active(green)
> sudo service gpsd status
> sudo service gpsd start

- make sure you un-comment out the gpsd to local host line
> sudo nano /etc/kismet/kismet.conf
  - gps=gpsd:host=localhost,port=2947

- make sure the file has device "ttyUSB0" (or whatever the computer identifies as your gps)
> nano your /etc/default/gpsd

- final check - if successful your gps will give the read out of its location
> cgps -s

### Step 2
#### Start kismet
> sudo kismet -c wlan0mon
- ** tutorial mentions pressing tab + return to get a terminal based readout - which did not work for me
- Open a browser and enter the following
>http://localhost:2501
- this will lead you to a sign on screen and establish a username and passwrod the first time you log into it
- data should be streaming at this point - may need to enable the correct data source if soemthing got bumped or working with multiple radio cards

### Optional Step 3
#### Reformat .kismet files
- convert kismet file to kml for gpsprune
> sudo kismetdb_to_kml --in [the file kismet created] --out [wardrive.kml]

- convert to pcap
> sudo kismetdb_to_pcap --in [the file kismet created] --out [wardrive.cap]

### Optional Step 4
#### Adding KML to a map output
- install gpsprune
> sudo apt install gpsprune
- open in gpsprune
> sudo gpsprune [kml_file]
- additional kml files can be added by drag and dropping to open file and resaving under different name

