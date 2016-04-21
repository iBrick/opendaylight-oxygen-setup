"""
del-node.

deletes a node from ODL

parameters
* ODL IP address
* node name

uses HTTP PUT with JSON payload
"""

import sys
import os
import requests

# check args length
if (len(sys.argv) != 3):
    print "usage %s ODL_IP_address Node_Name" % sys.argv[0]
    sys.exit(1)

odl_user = os.environ.get('ODL_USER', 'admin')
odl_pass = os.environ.get('ODL_PASS', 'admin')

# set up the URL
url = 'http://' + sys.argv[1] + \
      ':8181/restconf/config/network-topology:network-topology' + \
      '/topology/topology-netconf/node/controller-config' + \
      '/yang-ext:mount/config:modules/module' + \
      '/odl-sal-netconf-connector-cfg:sal-netconf-connector/' + \
      sys.argv[2]

# Delete Node from ODL
print requests.delete(url, auth=(odl_user, odl_pass))
