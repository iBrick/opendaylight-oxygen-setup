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
  "module" : [
    {
      "type": "odl-bgp-rib-impl-cfg:bgp-peer",
      "name": "example-bgp-peer",
      "odl-bgp-rib-impl-cfg:host":"%s",
      "odl-bgp-rib-impl-cfg:peer-role":"%s",
      "odl-bgp-rib-impl-cfg:remote-as":"%s",
      "odl-bgp-rib-impl-cfg:initiate-connection": true,
      "odl-bgp-rib-impl-cfg:rib": {
        "type": "odl-bgp-rib-impl-cfg:rib-instance",
        "name": "example-bgp-rib"
      },
      "odl-bgp-rib-impl-cfg:peer-registry": {
        "type": "odl-bgp-rib-impl-cfg:bgp-peer-registry",
        "name": "global-bgp-peer-registry"
      },
      "odl-bgp-rib-impl-cfg:advertized-table": [
        {
          "type": "odl-bgp-rib-impl-cfg:bgp-table-type",
          "name": "ipv6-unicast"
        },
        {
          "type": "odl-bgp-rib-impl-cfg:bgp-table-type",
          "name": "linkstate"
        },
        {
          "type": "odl-bgp-rib-impl-cfg:bgp-table-type",
          "name": "ipv4-unicast"
        }
      ]
    }
  ]
}
'''
# check args length
if (len(sys.argv) != 5):
        print "usage %s ODL_IP_address Peer_IP_Address ODL_ASN Peer_ASN" % \
              sys.argv[0]
        sys.exit(1)

odl_user = os.environ.get('ODL_USER', 'admin')
odl_pass = os.environ.get('ODL_PASS', 'admin')

if (sys.argv[3] == sys.argv[4]):
    bgp_mode = 'ibgp'
else:
    bgp_mode = 'ebgp'

req_hdrs = {'Content-Type': 'application/json'}

req_body = request_template % (sys.argv[2], bgp_mode, sys.argv[4])

url = 'http://' + sys.argv[1] + ':8181' + \
      '/restconf/config/network-topology:network-topology/topology' + \
      '/topology-netconf/node/controller-config/yang-ext:mount' + \
      '/config:modules/module/odl-bgp-rib-impl-cfg:bgp-peer/example-bgp-peer'

resp = requests.put(url, data=req_body, headers=req_hdrs,
                    auth=(odl_user, odl_pass))

print resp
