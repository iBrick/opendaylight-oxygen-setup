"""
put-app-rib.

sets up ODL App RIB

parameter:
* ODL IP address
* App RIB ID

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
      "config": {
        "peer-group": "application-peers"
      }
    }
  ]
}
'''

# check args length
if (len(sys.argv) != 3):
        print "usage %s ODL_IP_address App_RIB_ID" % sys.argv[0]
        sys.exit(1)

odl_user = os.environ.get('ODL_USER', 'admin')
odl_pass = os.environ.get('ODL_PASS', 'admin')

req_hdrs = {'Content-Type': 'application/json'}
req_body = request_template % (sys.argv[2])

url = 'http://' + sys.argv[1] + ':8181' + \
      '/restconf/config' + \
      '/openconfig-network-instance:network-instances' + \
      '/network-instance/global-bgp' + \
      '/protocols/protocol/openconfig-policy-types:BGP' + \
      '/example-bgp-rib/bgp-openconfig-extensions:bgp' + \
      '/neighbors/neighbor/' + sys.argv[2]

resp = requests.put(url, data=req_body, headers=req_hdrs,
                    auth=(odl_user, odl_pass))

print resp
