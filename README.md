# opendaylight-setup
This directory contains setup scripts for ODL.

Installation Instructions:

1.  Clone this repo:

  git clone https://github.com/CiscoDevNet/opendaylight-setup.git ODL

2.  Within the ODL directory create an "images" subdirectory:

  cd ODL<br>
  mkdir images
 
  So you will now have 2 subdirectories:

  * python
  * images

4.  Copy the appropriate OpenDaylight distribution file (.tar.gz) from https://www.opendaylight.org/downloads (or other location) to images:

  Example: (Assumes you are downloading the "0.3.3-Lithium-SR3" release.)

  wget -P images https://nexus.opendaylight.org/content/groups/public/org/opendaylight/integration/distribution-karaf/0.3.3-Lithium-SR3/distribution-karaf-0.3.3-Lithium-SR3.tar.gz

5.  Under the "ODL" directory, edit the "distro" file to reflect the release you just downloaded into the "images" directory.
 
6. Unpack ODL using

	./unpack-odl

7.	If you are *not* using the dCloud infrastructure (http://dcloud.cisco.com) to experiment with ODL, edit the "nodes" file to reflect the list of nodes and their IP Addresses in your VIRL simulation.

8.	Optionally edit the features file to change the set of features installed at ODL startup.

9.	Optionally edit the logs file to change the set of additional logging activated at ODL startup.
 
10. Set up ODL using (this loads key features and logging configs)

  ./setup-odl
   
11.	If you are using dCloud then set up the VPN using:

	sudo ./start-vpn site username password
	
	* site is one of rtp, lon, sng or chi
	* username and password can be found in your dCloud sssion details

	(note that your unix account will need sudo privileges)

12.	Start ODL using

  ./start-odl interface (e.g. tun0, eth0)

13.	Configure ODL using

  ./config-odl
  
  (this will connect ODL to the NETCONF nodes and configure BGP-LS/PCE-P - if the features are selected)
  
The repository also contains a subdirectory "vagrant" which contains a Vagrantfile and bootstrap.sh script.

If you have Vagrant and VirtualBox installed you can do a "vagrant up" from that directory and a VirtualBox VM will be created consisting of:

* Ubuntu 14.04
* git
* openconnect
* java (JRE only)
* pip
* pyang
* this repository
* the latest OpenDaylight 0.4.1-SNAPSHOT image

ODL will be unpacked.  So you can follow the instructions above from step 6.

### Scripts are:

**unpack-odl** unpacks the .tar.gz file.  Creates a new subdirectory for the ODL distro.

**setup-odl** sets up logging/features for ODL

**start-vpn** connects to dCloud VPN.  Takes 3 parameters:  

* site (rtp/lon/sng/chi)
* username
* password

**stop-vpn** disconnects from dCloud VPN

**start-odl** cleans out data from previous runs and starts ODL

**stop-odl** stops ODL

**config-odl** sets up NETCONF nodes, BGP neighbor etc. - uses scripts from the python subdirectory

**delete-odl** deletes the ODL distribution

### Additional files are:

**distro** distribution to run

**features** list of features to run

**logs** extra logs to run

**nodes** list of NETCONF nodes.  Last node in the list is the BGP neighbor.

### Python scripts are:

**put-node.py** mounts a node

**is-node-connected.py** checks if a node is mounted

**put-bgp-rib.py** configures the ODL BGP RIB

**put-app-rib.py** configures the ODL App RIB

**put-bgp-peer.py** configures ODL's BGP peer (XR)

**put-bgp-neighbor.py** configures XR with ODL as a BGP peer
