# shutdown and flush inteface
sudo ifconfig enp0s8 down
sudo ip add flush dev enp0s8
sudo service vpp restart
sudo service honeycomb restart
