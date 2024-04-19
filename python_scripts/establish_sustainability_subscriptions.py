#! /usr/bin/env python
import traceback
import lxml.etree as et
from argparse import ArgumentParser
from ncclient import manager
from ncclient.operations import RPCError

payload = [
'''
<establish-subscription xmlns="urn:ietf:params:xml:ns:yang:ietf-event-notifications">
  <stream xmlns:yp="urn:ietf:params:xml:ns:yang:ietf-yang-push">yp:yang-push</stream>
  <encoding>encode-xml</encoding>
  <xpath-filter xmlns="urn:ietf:params:xml:ns:yang:ietf-yang-push">/environment-sensors</xpath-filter>
  <period xmlns="urn:ietf:params:xml:ns:yang:ietf-yang-push">6000</period>
</establish-subscription>
''','''
<establish-subscription xmlns="urn:ietf:params:xml:ns:yang:ietf-event-notifications">
  <stream xmlns:yp="urn:ietf:params:xml:ns:yang:ietf-yang-push">yp:yang-push</stream>
  <encoding>encode-xml</encoding>
  <xpath-filter xmlns="urn:ietf:params:xml:ns:yang:ietf-yang-push">/oc-platform:components</xpath-filter>
  <period xmlns="urn:ietf:params:xml:ns:yang:ietf-yang-push">6000</period>
</establish-subscription>
''','''
<establish-subscription xmlns="urn:ietf:params:xml:ns:yang:ietf-event-notifications">
  <stream xmlns:yp="urn:ietf:params:xml:ns:yang:ietf-yang-push">yp:yang-push</stream>
  <encoding>encode-xml</encoding>
  <xpath-filter xmlns="urn:ietf:params:xml:ns:yang:ietf-yang-push">/platform-ios-xe-oper:components/component</xpath-filter>
  <period xmlns="urn:ietf:params:xml:ns:yang:ietf-yang-push">6000</period>
</establish-subscription>
''','''
<establish-subscription xmlns="urn:ietf:params:xml:ns:yang:ietf-event-notifications">
  <stream xmlns:yp="urn:ietf:params:xml:ns:yang:ietf-yang-push">yp:yang-push</stream>
  <encoding>encode-xml</encoding>
  <xpath-filter xmlns="urn:ietf:params:xml:ns:yang:ietf-yang-push">/platform-ios-xe-oper:components/component/platform-properties/platform-property</xpath-filter>
  <period xmlns="urn:ietf:params:xml:ns:yang:ietf-yang-push">6000</period>
</establish-subscription>
''','''
<establish-subscription xmlns="urn:ietf:params:xml:ns:yang:ietf-event-notifications">
  <stream xmlns:yp="urn:ietf:params:xml:ns:yang:ietf-yang-push">yp:yang-push</stream>
  <encoding>encode-xml</encoding>
  <xpath-filter xmlns="urn:ietf:params:xml:ns:yang:ietf-yang-push">/poe-oper-data/poe-module</xpath-filter>
  <period xmlns="urn:ietf:params:xml:ns:yang:ietf-yang-push">6000</period>
</establish-subscription>
''','''
<establish-subscription xmlns="urn:ietf:params:xml:ns:yang:ietf-event-notifications">
  <stream xmlns:yp="urn:ietf:params:xml:ns:yang:ietf-yang-push">yp:yang-push</stream>
  <encoding>encode-xml</encoding>
  <xpath-filter xmlns="urn:ietf:params:xml:ns:yang:ietf-yang-push">/poe-oper-data/poe-port-detail</xpath-filter>
  <period xmlns="urn:ietf:params:xml:ns:yang:ietf-yang-push">6000</period>
</establish-subscription>
''','''
<establish-subscription xmlns="urn:ietf:params:xml:ns:yang:ietf-event-notifications">
  <stream xmlns:yp="urn:ietf:params:xml:ns:yang:ietf-yang-push">yp:yang-push</stream>
  <encoding>encode-xml</encoding>
  <xpath-filter xmlns="urn:ietf:params:xml:ns:yang:ietf-yang-push">/poe-oper-data/poe-stack</xpath-filter>
  <period xmlns="urn:ietf:params:xml:ns:yang:ietf-yang-push">6000</period>
</establish-subscription>
''','''
<establish-subscription xmlns="urn:ietf:params:xml:ns:yang:ietf-event-notifications">
  <stream xmlns:yp="urn:ietf:params:xml:ns:yang:ietf-yang-push">yp:yang-push</stream>
  <encoding>encode-xml</encoding>
  <xpath-filter xmlns="urn:ietf:params:xml:ns:yang:ietf-yang-push">/poe-oper-data/poe-switch</xpath-filter>
  <period xmlns="urn:ietf:params:xml:ns:yang:ietf-yang-push">6000</period>
</establish-subscription>
''',
]

if __name__ == '__main__':

    parser = ArgumentParser(description='Usage:')

    # script arguments
    parser.add_argument('-a', '--host', type=str, required=True,
                        help="Device IP address or Hostname")
    parser.add_argument('-u', '--username', type=str, required=True,
                        help="Device Username (netconf agent username)")
    parser.add_argument('-p', '--password', type=str, required=True,
                        help="Device Password (netconf agent password)")
    parser.add_argument('--port', type=int, default=830,
                        help="Netconf agent port")
    args = parser.parse_args()

    # connect to netconf agent
    with manager.connect(host=args.host,
                         port=args.port,
                         username=args.username,
                         password=args.password,
                         timeout=90,
                         hostkey_verify=False,
                         device_params={'name': 'csr'}) as m:

        # execute netconf operation
        for rpc in payload:
            try:
                response = m.dispatch(et.fromstring(rpc))
                data = response.xml
            except RPCError as e:
                data = e.xml
                pass
            except Exception as e:
                traceback.print_exc()
                exit(1)

            # beautify output
            if et.iselement(data):
                data = et.tostring(data, pretty_print=True).decode()

            try:
                out = et.tostring(
                    et.fromstring(data.encode('utf-8')),
                    pretty_print=True
                ).decode()
            except Exception as e:
                traceback.print_exc()
                exit(1)

            print(out)
