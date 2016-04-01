"""
put-bgp-neighbor.

configures XR to peer with ODL

parameter:
* ODL IP address
* Peer XR NETCONF node
* ODL BGP ASN
* XR BGP ASN

uses HTTP PUT with JSON payload
"""

import sys
import os
import requests

request_template = '''
{
  "neighbor": [
    {
      "neighbor-address": "%s",
      "session-open-mode": "passive-only",
      "remote-as": {
        "as-xx": 0,
        "as-yy": %s
      },
      "neighbor-afs": {
        "neighbor-af": [
          {
            "af-name": "ipv4-unicast",
            "activate": [
              null
            ],
            "route-reflector-client": true
          },
          {
            "af-name": "lsls",
            "activate": [
              null
            ],
            "route-reflector-client": true
          }
        ]
      }
    }
  ]
}
'''

# check args length
if (len(sys.argv) != 5):
        print "usage %s ODL_IP_address Peer-NETCONF-Node ODL_ASN Peer_ASN" % \
              sys.argv[0]
        sys.exit(1)

odl_user = os.environ.get('ODL_USER', 'admin')
odl_pass = os.environ.get('ODL_PASS', 'admin')

req_hdrs = { 'Content-Type' : 'application/json' }

req_body = request_template % (sys.argv[1], sys.argv[3])

url = 	'http://' + sys.argv[1] + ':8181' + \
		'/restconf/config/network-topology:network-topology/topology' + \
		'/topology-netconf/node/' + sys.argv[2] + '/yang-ext:mount' + \
		'/Cisco-IOS-XR-ipv4-bgp-cfg:bgp/instance/default/instance-as/0/four-byte-as/' + \
                sys.argv[4] + '/default-vrf/bgp-entity/neighbors/neighbor/' + sys.argv[1]

resp = requests.put(url, data=req_body, headers=req_hdrs, auth=(odl_user, odl_pass))

print resp
