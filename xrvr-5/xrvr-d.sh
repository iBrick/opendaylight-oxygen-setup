sudo qemu-system-x86_64 -daemonize -display none -enable-kvm -machine accel=kvm -smp cores=2 -m 4096 \
  -hda ./xrvr-d.vmdk \
  -serial telnet::9041,server,nowait -serial telnet::9042,server,nowait \
  -net nic,model=virtio,vlan=0,macaddr=00:22:00:ff:0D:00 -net tap,vlan=0,script=/etc/qemu-ifup \
  -net nic,model=virtio,vlan=1,macaddr=00:22:00:ff:0D:01 -net socket,vlan=1,connect=127.0.0.1:16000 \
  -net nic,model=virtio,vlan=2,macaddr=00:22:00:ff:0D:02 -net socket,vlan=2,connect=127.0.0.1:18000 \
  -net nic,model=virtio,vlan=3,macaddr=00:22:00:ff:0D:03 -net socket,vlan=3,listen=127.0.0.1:21000
