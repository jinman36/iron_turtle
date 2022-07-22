Installing Impacket:
kali 2019.3 / 2021.1

> git clone https://github.com/SecureAuthCorp/impacket.git /opt/impacket
* I had to create the folder ahead of pulling the repo - used sudo to add to the opt folder

look through the contents of the impacket fodler and ensure that the following docs were trnsfered correctly:
- requirements.txt
- setup.py


> pip3 install -r /opt/impacket/requirements.txt
> cd /opt/impacket/ && python3 ./setup.py install

**if these dont work, try creating/running the following script:

sudo git clone https://github.com/SecureAuthCorp/impacket.git /opt/impacket
sudo pip3 install -r /opt/impacket/requirements.txt
cd /opt/impacket/ 
sudo pip3 install .
sudo python3 setup.py install