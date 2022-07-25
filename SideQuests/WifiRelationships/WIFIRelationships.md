# Visualize WiFi Relationships with AirGraph-ng

## YouTubeVideo from Hakbyte 7.24.22
- https://www.youtube.com/watch?v=wvRdeFGuHMc&list=WL&index=9

### Step 1
- ensure aircrack-ng is installed (pre installed on Kali)
- www.aircrack-ng.org for other operating systems
equipment required
  - external wireless card - capable of monitor mode
  - I am using a Panda PAU09 wireless card

### Step 2
- enable monitor mode
> sudo airmon-ng
- put external wireless card into monitor mode
> sudo airmon-ng start wlan0
- running airdump-ng to get wifi informaiont in the area
> sudo airodump-ng wlan0mon --band abg -w dual-band

- the above command will produce the (5) files below
1. dual-band-01.cap  
2. dual-band-01.csv  
3. dual-band-01.kismet.csv  
4. dual-band-01.kismet.netxml  
5. dual-band-01.log.csv

- .cap * contains all network traffic, analyze websites but requires cracking wpa key
- .kismet * wardriving and find geo locations of signals
- .csv * Human readable - able to visualize data

### Step 4
- Use airgraph-ng to produce a graphical analysis of networks ** I had to install this seperate/ was not part of the standard kali based aircrack-ng suite
> sudo airgraph-ng -i dual-band-01.csv -o capture.png -g CAPR
  - flags
    - -i input .csv file
    - -o output file/location
    - -g type of graph (CAPR)
    
### Step 5
- Use airgraph-ng
  - Flag -g CPG (common probe graph) - this displays wireless devices that are probing but aren't connected
  
Types of Graphs
- CAPR - client access point relationship
- CPG - common probe graph