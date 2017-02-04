"""
put-static-route.

adds static route to XR

parameter:
* ODL IP address
* Peer XR NETCONF node
* prefix
* length
* next-hop 

uses HTTP PUT with JSON payload
"""

import sys
import os
import requests

request_template = '''
{
  "vrf-prefix": [
    {
      "prefix": "%s",
      "prefix-length": %s,
      "vrf-route": {
        "vrf-next-hop-table": {
          "vrf-next-hop-next-hop-address": [
            {
              "next-hop-address": "%s"
            }
          ]
        }
      }
    }
  ]
}
'''

# check args length
if (len(sys.argv) != 6):
        print "usage %s ODL_IP_address NETCONF-Node prefix length nexthop" % \
              sys.argv[0]
        sys.exit(1)

odl_user = os.environ.get('ODL_USER', 'admin')
odl_pass = os.environ.get('ODL_PASS', 'admin')

req_hdrs = { 'Content-Type' : 'application/json' }

req_body = request_template % (sys.argv[3], sys.argv[4], sys.argv[5])

url = 	'http://' + sys.argv[1] + ':8181' + \
		'/restconf/config/network-topology:network-topology/topology' + \
		'/topology-netconf/node/' + sys.argv[2] + '/yang-ext:mount' + \
                '/Cisco-IOS-XR-ip-static-cfg:router-static/default-vrf' + \
                '/address-family/vrfipv4/vrf-unicast/vrf-prefixes/vrf-prefix/' + \
                sys.argv[3] + '/' + sys.argv[4]

resp = requests.put(url, data=req_body, headers=req_hdrs, auth=(odl_user, odl_pass))

print resp
