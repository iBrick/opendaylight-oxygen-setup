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
{ "module" :
  [
    {
      "type": "odl-bgp-rib-impl-cfg:rib-impl",
      "name": "example-bgp-rib",
      "odl-bgp-rib-impl-cfg:bgp-rib-id": "%s",
      "odl-bgp-rib-impl-cfg:bgp-dispatcher": {
        "type": "odl-bgp-rib-impl-cfg:bgp-dispatcher",
        "name": "global-bgp-dispatcher"
      },
      "odl-bgp-rib-impl-cfg:extensions": {
        "type": "odl-bgp-rib-spi-cfg:extensions",
        "name": "global-rib-extensions"
      },
      "odl-bgp-rib-impl-cfg:tcp-reconnect-strategy": {
        "type": "protocol-framework:reconnect-strategy-factory",
        "name": "example-reconnect-strategy-factory"
      },
      "odl-bgp-rib-impl-cfg:rib-id": "example-bgp-rib",
      "odl-bgp-rib-impl-cfg:session-reconnect-strategy": {
        "type": "protocol-framework:reconnect-strategy-factory",
        "name": "example-reconnect-strategy-factory"
      },
      "odl-bgp-rib-impl-cfg:local-table": [
        {
          "type": "odl-bgp-rib-impl-cfg:bgp-table-type",
          "name": "ipv4-unicast"
        },
        {
          "type": "odl-bgp-rib-impl-cfg:bgp-table-type",
          "name": "ipv6-unicast"
        },
        {
          "type": "odl-bgp-rib-impl-cfg:bgp-table-type",
          "name": "linkstate"
        }
      ],
      "odl-bgp-rib-impl-cfg:data-provider": {
        "type": "opendaylight-md-sal-binding:binding-async-data-broker",
        "name": "pingpong-binding-data-broker"
      },
      "odl-bgp-rib-impl-cfg:dom-data-provider": {
        "type": "opendaylight-md-sal-dom:dom-async-data-broker",
        "name": "pingpong-broker"
      },
      "odl-bgp-rib-impl-cfg:codec-tree-factory": {
        "type": "opendaylight-md-sal-binding:binding-codec-tree-factory",
        "name": "runtime-mapping-singleton"
      },
      "odl-bgp-rib-impl-cfg:local-as": %s
    }
  ]
}
'''

# check args length
if (len(sys.argv) != 3):
        print "usage %s ODL_IP_address ODL_ASN" % sys.argv[0]
        sys.exit(1)

odl_user = os.environ.get('ODL_USER', 'admin')
odl_pass = os.environ.get('ODL_PASS', 'admin')

req_hdrs = {'Content-Type': 'application/json'}
req_body = request_template % (sys.argv[1], sys.argv[2])

url = 'http://' + sys.argv[1] + ':8181' + \
      '/restconf/config/network-topology:network-topology/topology' + \
      '/topology-netconf/node/controller-config/yang-ext:mount' + \
      '/config:modules/module/odl-bgp-rib-impl-cfg:rib-impl/example-bgp-rib'

resp = requests.put(url, data=req_body, headers=req_hdrs,
                    auth=(odl_user, odl_pass))

print resp
