"""
put-bgp-neighbor.

configures XR to peer with ODL

parameter:
* ODL IP address
* Peer XR NETCONF node
* PCE peer

uses HTTP PUT with JSON payload
"""

import sys
import os
import requests

request_template = '''
{
  "peer": [
    {
      "pce-peer-address": "%s",
      "enable": [
        null
      ]
    }
  ]
}
'''

# check args length
if (len(sys.argv) != 4):
        print "usage %s ODL_IP_address Peer-NETCONF-Node PCE-Peer" % \
              sys.argv[0]
        sys.exit(1)

odl_user = os.environ.get('ODL_USER', 'admin')
odl_pass = os.environ.get('ODL_PASS', 'admin')

req_hdrs = { 'Content-Type' : 'application/json' }

req_body = request_template % (sys.argv[3])

url = 	'http://' + sys.argv[1] + ':8181' + \
		'/restconf/config/network-topology:network-topology/topology' + \
		'/topology-netconf/node/' + sys.argv[2] + '/yang-ext:mount' + \
		'/Cisco-IOS-XR-mpls-te-cfg:mpls-te/global-attributes' + \
		'/pce-attributes/peers/peer/' + sys.argv[3] 

resp = requests.put(url, data=req_body, headers=req_hdrs, auth=(odl_user, odl_pass))

print resp
