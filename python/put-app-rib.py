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
{ "module" :
  [
    {
      "type": "odl-bgp-rib-impl-cfg:bgp-application-peer",
      "name": "example-bgp-peer-app",
      "odl-bgp-rib-impl-cfg:data-broker": {
        "type": "opendaylight-md-sal-dom:dom-async-data-broker",
        "name": "pingpong-broker"
      },
      "odl-bgp-rib-impl-cfg:target-rib": {
        "type": "odl-bgp-rib-impl-cfg:rib-instance",
        "name": "example-bgp-rib"
      },
      "odl-bgp-rib-impl-cfg:bgp-peer-id": "%s",
      "odl-bgp-rib-impl-cfg:application-rib-id": "example-app-rib"
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
      '/restconf/config/network-topology:network-topology' + \
      '/topology/topology-netconf/node/controller-config' + \
      '/yang-ext:mount/config:modules' + \
      '/module/odl-bgp-rib-impl-cfg:bgp-application-peer/example-bgp-peer-app'

resp = requests.put(url, data=req_body, headers=req_hdrs,
                    auth=(odl_user, odl_pass))

print resp
