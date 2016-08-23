sudo qemu-system-x86_64 -daemonize -display none -enable-kvm -machine accel=kvm -smp cores=2 -m 4096 \
  -hda ./xrvr-c.vmdk \
  -serial telnet::9301,server,nowait -serial telnet::9302,server,nowait \
  -net nic,model=virtio,vlan=0,macaddr=00:22:00:ff:0C:00 -net tap,vlan=0,script=/etc/qemu-ifup \
  -net nic,model=virtio,vlan=1,macaddr=00:22:00:ff:0C:01 -net socket,vlan=1,connect=127.0.0.1:15000 \
  -net nic,model=virtio,vlan=2,macaddr=00:22:00:ff:0C:02 -net socket,vlan=2,connect=127.0.0.1:17000 \
  -net nic,model=virtio,vlan=3,macaddr=00:22:00:ff:0C:03 -net socket,vlan=3,listen=127.0.0.1:20000
