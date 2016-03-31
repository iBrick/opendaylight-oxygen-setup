"""
put-node.

adds a node to ODL

parameter:
* ODL IP address
* node IP address
* node name
* netconf port (optional - default is 830)
* netconf user (optional - default is 'cisco')
* netconf pass (optional - default is 'cisco')

uses HTTP PUT with JSON payload
"""

import sys
import os
import requests

# set up the request
request_template = '''
{
  "module": [
    {
      "type": "odl-sal-netconf-connector-cfg:sal-netconf-connector",
      "name": "%s",
      "odl-sal-netconf-connector-cfg:address": "%s",
      "odl-sal-netconf-connector-cfg:port": %s,
      "odl-sal-netconf-connector-cfg:username": "%s",
      "odl-sal-netconf-connector-cfg:password": "%s",
      "odl-sal-netconf-connector-cfg:tcp-only": false,
      "odl-sal-netconf-connector-cfg:binding-registry": {
        "type": "opendaylight-md-sal-binding:binding-broker-osgi-registry",
        "name": "binding-osgi-broker"
      },
      "odl-sal-netconf-connector-cfg:between-attempts-timeout-millis": 2000,
      "odl-sal-netconf-connector-cfg:processing-executor": {
         "type": "threadpool:threadpool",
         "name": "global-netconf-processing-executor"
      },
      "odl-sal-netconf-connector-cfg:max-connection-attempts": 0,
      "odl-sal-netconf-connector-cfg:sleep-factor": 1.5,
      "odl-sal-netconf-connector-cfg:client-dispatcher": {
        "type": "odl-netconf-cfg:netconf-client-dispatcher",
        "name": "global-netconf-dispatcher"
      },
      "odl-sal-netconf-connector-cfg:dom-registry": {
        "type": "opendaylight-md-sal-dom:dom-broker-osgi-registry",
        "name": "dom-broker"
      },
      "odl-sal-netconf-connector-cfg:event-executor": {
        "type": "netty:netty-event-executor",
        "name": "global-event-executor"
      },
      "odl-sal-netconf-connector-cfg:connection-timeout-millis": 20000
    }
  ]
}
'''

netconf_port = 830
netconf_user = 'cisco'
netconf_pass = 'cisco'

# check args length
if ((len(sys.argv) < 4) or (len(sys.argv) > 7)):
    print "usage %s ODL_IP_address Node_IP_address Node_Name \
           [port user password]" % sys.argv[0]
    sys.exit(1)

if (len(sys.argv) > 4):
    netconf_port = sys.argv[4]
if (len(sys.argv) > 5):
    netconf_user = sys.argv[5]
if (len(sys.argv) > 6):
    netconf_pass = sys.argv[6]

odl_user = os.environ.get('ODL_USER', 'admin')
odl_pass = os.environ.get('ODL_PASS', 'admin')

# set up the URL
url = 'http://' + sys.argv[1] + \
      ':8181/restconf/config/network-topology:network-topology' + \
      '/topology/topology-netconf/node/controller-config' + \
      '/yang-ext:mount/config:modules/module' + \
      '/odl-sal-netconf-connector-cfg:sal-netconf-connector/' + \
      sys.argv[3]

request_body = request_template % (sys.argv[3], sys.argv[2],
                                   netconf_port, netconf_user, netconf_pass)

headers = {'Content-Type': 'application/json'}

# Put Node to ODL
print requests.put(url, data=request_body, headers=headers,
                   auth=(odl_user, odl_pass))
