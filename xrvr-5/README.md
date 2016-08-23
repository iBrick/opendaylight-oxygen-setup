# xrvr-5
This directory contains setup scripts for a 5 node XRv topology. 

### Key scripts are:

**XRstart.sh** runs all 5 XR nodes in the correct order.  Calls xrvr-e.sh, xrvr-d.sh, xrvr-c.sh, xrvr-b.sh and xrvr-a.sh

**XRstop.sh** kills all 5 XR nodes by finding kvm/qemu processes.

**XRsetup.sh** sets up all 5 XR nodes

**XRloader.exp** used to initialise an XR node.  Takes 3 parameters:

1. hostname
2. management IP address
3. virtual serial port

additional variables for username, password, management subnet mask etc. are inline in the script.

the script is written in expect so that will be required on your server.

### Additional files are:

**xrvr-a.sh to xrvr-e.sh** QEMU/KVM start scripts for XR

**xrvr-a.config to xrvr-e.config** Initial configs for the 5 nodes

**nodes** list of hostnames and IP addresses (for use with scripts in next directory up)

**parameters** parameters (for use with scripts in next directory up)


