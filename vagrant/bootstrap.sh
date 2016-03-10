#!/usr/bin/env bash

apt-get -qq update
echo Y | apt-get -qq install git
echo Y | apt-get -qq install openconnect
echo Y | apt-get -qq install python-pip
echo pip install pyang
echo "cloning scripts"
git clone -q https://github.com/CiscoDevNet/opendaylight-setup.git ODL
cd ODL
echo "finding ODL distro"
curl -s https://nexus.opendaylight.org/content/repositories/opendaylight.snapshot/org/opendaylight/integration/distribution-karaf/0.4.1-SNAPSHOT/ | grep "tar.gz<" | tail -1 | cut -f2 -d\" > /tmp/url
mkdir images
cd images
echo "downloading ODL distro"
wget -q -i /tmp/url
cd ..
echo "unpacking ODL distro"
./unpack-odl 
cd ..
chown -R vagrant:vagrant *
echo "ready!"
