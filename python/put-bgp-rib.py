"""
put-bgp-rib.

sets up ODL BGP RIB

parameter:
* ODL IP address
* ODL ASN

uses HTTP PUT with JSON payload
"""

import sys
import os
import requests

request_template = '''
{
    "bgp-openconfig-extensions:config": {
        "as": %d,
        "router-id": "%s"
    }
}
'''

# check args length
if (len(sys.argv) != 3):
        print "usage %s ODL_IP_address ODL_ASN" % sys.argv[0]
        sys.exit(1)

odl_user = os.environ.get('ODL_USER', 'admin')
odl_pass = os.environ.get('ODL_PASS', 'admin')

req_hdrs = {'Content-Type': 'application/json'}
req_body = request_template % (int(sys.argv[2]), sys.argv[1])

url = 'http://' + sys.argv[1] + ':8181' + \
      '/restconf/config' + \
      '/openconfig-network-instance:network-instances' + \
      '/network-instance/global-bgp' + \
      '/protocols/protocol/openconfig-policy-types:BGP' + \
      '/example-bgp-rib/bgp-openconfig-extensions:bgp' + \
      '/global/config'

resp = requests.put(url, data=req_body, headers=req_hdrs,
                    auth=(odl_user, odl_pass))

print resp
