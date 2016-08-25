sudo qemu-system-x86_64 -daemonize -display none -enable-kvm -machine accel=kvm -smp cores=2 -m 4096 \
  -hda ./xrvr-a.qcow2 \
  -serial telnet::9011,server,nowait -serial telnet::9012,server,nowait \
  -net nic,model=virtio,vlan=0,macaddr=00:22:00:ff:0A:00 -net tap,vlan=0,script=/etc/qemu-ifup \
  -net nic,model=virtio,vlan=1,macaddr=00:22:00:ff:0A:01 -net socket,vlan=1,listen=127.0.0.1:14000 \
  -net nic,model=virtio,vlan=2,macaddr=00:22:00:ff:0A:02 -net socket,vlan=2,listen=127.0.0.1:15000 \
  -net nic,model=virtio,vlan=3,macaddr=00:22:00:ff:0A:03 -net socket,vlan=3,listen=127.0.0.1:16000 \
  -net nic,model=virtio,vlan=4,macaddr=00:22:00:ff:0A:04 -net socket,vlan=4,listen=127.0.0.1:19000
