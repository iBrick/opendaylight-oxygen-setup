# xrvr-5
This directory contains setup scripts for a 5 node XRv topology. 

First run ./XRget.sh to get the XR image from the repo.

Then run ./XRcopy.sh to copy your XR image to 5 files called e.g. xrvr-a.vmdk, xrvr-b.vmdk.  (modify this script if not using .vmdks).

Then run ./XRstart.sh and then ./XRsetup.sh to initialise the nodes.

Once the nodes are up and configured you can point ODL at them (use the scripts in the directory one up from this, but with the parameters and nodes files in this directory).

On subsequent launches you only need ./XRstart.sh.

### Key scripts are:

**XRget.sh** gets the XR image from the repo.  Takes 2 parameters:

1. CCO ID
2. API key

please see https://xrdocs.github.io/getting-started/steps-download-iosxr-vagrant (though here we get the .iso not the .box)

**XRcopy.sh** copies the XR image once for each node (e.g. to xrvr-a.vmdk).

**XRstart.sh** runs all XR nodes in the correct order.  Calls xrvr-a.sh etc.

**XRstop.sh** kills all XR nodes by finding kvm/qemu processes.

**XRsetup.sh** initialises all XR nodes.  Calls XRloader.exp for each node.

**XRloader.exp** used to initialise an XR node.  Takes 3 parameters:

1. hostname
2. management IP address
3. virtual serial port

additional variables for username, password, management subnet mask etc. are inline in the script.

the script is written in expect so that will be required on your server.

### Additional files are:

**xrvr-a.sh to xrvr-e.sh** QEMU/KVM start scripts for XR.   These may need to be modified if not using .vmdks or if your machine setup is different.

**xrvr-a.config to xrvr-e.config** Initial configs for the 5 nodes.

**nodes** list of hostnames and IP addresses (for use with scripts in this directory and next directory up)

**parameters** parameters (for use with scripts in this director and next directory up)

**topology.pdf** shows the topology of the network.


