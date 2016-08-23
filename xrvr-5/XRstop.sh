sudo kill $(ps aux | grep 'qemu-system-x86_64' | grep 'XR' | awk '{print $2}')
