"""
put-bgp-peer.

sets up ODL BGP Peer

parameter:
* ODL IP address
* Peer IP address
* ODL BGP ASN
* Peer BGP ASN

uses HTTP PUT with JSON payload
"""

import sys
import os
import requests

request_template = '''
{
  "bgp-openconfig-extensions:neighbor": [
    {
      "neighbor-address": "%s",
      "timers": {
        "config": {
          "connect-retry": 10,
          "keepalive-interval": 30,
          "hold-time": 180,
          "minimum-advertisement-interval": 30
        }
      },
      "afi-safis": {
        "afi-safi": [
          {
            "afi-safi-name": "openconfig-bgp-types:IPV4-UNICAST"
          },
          {
            "afi-safi-name": "bgp-openconfig-extensions:LINKSTATE"
          }
        ]
      },
      "route-reflector": {
        "config": {
          "route-reflector-client": false
        }
      },
      "transport": {
        "config": {
          "remote-port": 179,
          "mtu-discovery": false,
          "passive-mode": false
        }
      },
      "config": {
        "send-community": "NONE",
        "peer-as": %d,
        "route-flap-damping": false,
        "peer-type": "%s"
      }
    }
  ]
}

# check args length
if (len(sys.argv) != 5):
        print "usage %s ODL_IP_address Peer_IP_Address ODL_ASN Peer_ASN" % \
              sys.argv[0]
        sys.exit(1)

odl_user = os.environ.get('ODL_USER', 'admin')
odl_pass = os.environ.get('ODL_PASS', 'admin')

if (sys.argv[3] == sys.argv[4]):
    peer_type = 'INTERNAL'
else:
    peer_type = 'EXTERNAL'

req_hdrs = {'Content-Type': 'application/json'}

req_body = request_template % (sys.argv[2], sys.argv[4], peer_type)

url = 'http://' + sys.argv[1] + ':8181' + \
      '/restconf/config' + \
      '/openconfig-network-instance:network-instances' + \
      '/network-instance/global-bgp' + \
      '/protocols/protocol/openconfig-policy-types:BGP' + \
      '/example-bgp-rib/bgp-openconfig-extensions:bgp'+ \
      '/neighbors/neighbor/' + sys.argv[2]

resp = requests.put(url, data=req_body, headers=req_hdrs,
                    auth=(odl_user, odl_pass))

print resp
