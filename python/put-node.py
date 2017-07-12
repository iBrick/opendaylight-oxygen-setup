"""
put-node.

adds a node to ODL

parameter:
* ODL IP address
* node IP address
* node name
* netconf port (optional - default is 830)
* netconf user (optional - default is 'cisco')
* netconf pass (optional - default is 'cisco')

uses HTTP PUT with JSON payload
"""

import sys
import os
import requests

# set up the request
request_template = '''
{
    "network-topology:node": {
        "node-id": "%s",
        "host": "%s",
        "port": "%s",
        "username": "%s",
        "password": "%s",
        "tcp-only": false,
        "keepalive-delay": 0,
        "schema-cache-directory": "XR"
    }
}
'''

netconf_port = 830
netconf_user = 'cisco'
netconf_pass = 'cisco'

# check args length
if ((len(sys.argv) < 4) or (len(sys.argv) > 7)):
    print "usage %s ODL_IP_address Node_IP_address Node_Name \
           [port user password]" % sys.argv[0]
    sys.exit(1)

if (len(sys.argv) > 4):
    netconf_port = sys.argv[4]
if (len(sys.argv) > 5):
    netconf_user = sys.argv[5]
if (len(sys.argv) > 6):
    netconf_pass = sys.argv[6]

odl_user = os.environ.get('ODL_USER', 'admin')
odl_pass = os.environ.get('ODL_PASS', 'admin')

# set up the URL
url = 'http://' + sys.argv[1] + \
      ':8181/restconf/config/network-topology:network-topology' + \
      '/topology/topology-netconf/node/' + sys.argv[3]

request_body = request_template % (sys.argv[3], sys.argv[2],
                                   netconf_port, netconf_user, netconf_pass)

headers = {'Content-Type': 'application/json'}

# Put Node to ODL
print requests.put(url, data=request_body, headers=headers,
                   auth=(odl_user, odl_pass))
