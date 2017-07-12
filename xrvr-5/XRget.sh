#!/bin/bash

ISOURL="https://devhub.cisco.com/artifactory/appdevci-release/XRv64/6.2.1/iosxrv-fullk9-x64.iso"

curl -u $1:$2 $ISOURL --output ./iosxrv-fullk9-x64.iso
