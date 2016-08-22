#!/usr/bin/env bash

apt-get -qq update
echo Y | apt-get -qq install git
echo Y | apt-get -qq install zip 
echo Y | apt-get -qq install openconnect
echo Y | apt-get -qq install default-jre
echo Y | apt-get -qq install mininet
echo Y | apt-get -qq install python-pip
echo pip install pyang
echo "cloning scripts"
git clone -q https://github.com/CiscoDevNet/opendaylight-setup.git ODL
cd ODL
mkdir images
cd images
echo "downloading ODL distro"
wget -q https://nexus.opendaylight.org/content/repositories/opendaylight.release/org/opendaylight/integration/distribution-karaf/0.4.3-Beryllium-SR3/distribution-karaf-0.4.3-Beryllium-SR3.tar.gz
cd ..
echo "unpacking ODL distro"
./unpack-odl 
cd ..
chown -R vagrant:vagrant *
echo "ready!"
