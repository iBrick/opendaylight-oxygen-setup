sudo vppctl create host-interface name vpp1out
sudo vppctl show hardware
sudo vppctl set int state host-vpp1out up
sudo vppctl set int ip address host-vpp1out 10.10.1.2/24
