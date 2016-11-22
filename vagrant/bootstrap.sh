#!/usr/bin/env bash

echo -e '\012' |  apt-add-repository ppa:webupd8team/java
apt-get -qq update
echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true" | debconf-set-selections
apt-get -qq install oracle-java8-installer &>/dev/null
apt-get -qq install oracle-java8-set-default
echo JAVA_HOME="/usr/lib/jvm/java-8-oracle" >> /etc/environment
source /etc/environment
apt-get -qq install git
apt-get -qq install zip 
apt-get -qq install openconnect
apt-get -qq install mininet
apt-get -qq install python-pip
pip install pyang
echo "cloning scripts"
git clone -q https://github.com/CiscoDevNet/opendaylight-setup.git ODL
cd ODL
mkdir images
cd images
echo "downloading ODL distro"
wget -q https://nexus.opendaylight.org/content/repositories/opendaylight.release/org/opendaylight/integration/distribution-karaf/0.5.1-Boron-SR1/distribution-karaf-0.5.1-Boron-SR1.tar.gz
cd ..
echo "unpacking ODL distro"
./unpack-odl
cd ..
chown -R vagrant:vagrant *
echo "ready!"
