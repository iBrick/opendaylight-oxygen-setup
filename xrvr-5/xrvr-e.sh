sudo qemu-system-x86_64 -daemonize -display none -enable-kvm -machine accel=kvm -smp cores=2 -m 4096 \
  -hda ./xrvr-e.qcow2 \
  -serial telnet::9051,server,nowait -serial telnet::9052,server,nowait \
  -net nic,model=virtio,vlan=0,macaddr=00:22:00:ff:0E:00 -net tap,vlan=0,script=/etc/qemu-ifup \
  -net nic,model=virtio,vlan=1,macaddr=00:22:00:ff:0E:01 -net socket,vlan=1,connect=127.0.0.1:20000 \
  -net nic,model=virtio,vlan=2,macaddr=00:22:00:ff:0E:02 -net socket,vlan=2,connect=127.0.0.1:21000 \
