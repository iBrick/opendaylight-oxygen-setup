"""
is-node-connected.

Checks if netconf node is connected

parameter:
* ODL IP address
* Node name

uses HTTP GET with JSON response
"""
import sys
import os
import requests
import json

# check args length
if (len(sys.argv) != 3):
        print "usage %s ODL_IP_address Node_Name" % sys.argv[0]
        sys.exit(1)

odl_user = os.environ.get('ODL_USER', 'admin')
odl_pass = os.environ.get('ODL_PASS', 'admin')

req_hdrs = {'Accept': 'application/json'}

url = 'http://' + sys.argv[1] + ':8181' + \
      '/restconf/operational/network-topology:network-topology/topology' + \
      '/topology-netconf/node/' + sys.argv[2]

r = requests.get(url, headers=req_hdrs, auth=(odl_user, odl_pass))

if (r.status_code == 200):
    t = json.loads(r.text)
    c = t['node'][0]['netconf-node-topology:connection-status']
    if (c == 'connected'):
        print 'node connected'
        sys.exit(0)
    else:
        print 'node not yet connected'
        sys.exit(1)
else:
    print 'unable to get node status'
    sys.exit(2)
