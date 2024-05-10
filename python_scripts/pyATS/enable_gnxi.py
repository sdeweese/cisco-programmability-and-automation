from pyats import topology

# let's write an inline testbed file for simplicity
# (edit this to whatever your testbed looks like)
testbed = topology.loader.load('''
testbed:
    name: my-inline-testbed

devices:
    c9300:
        type: iosxe
        os: iosxe
        alias: c9300
        credentials:
            default:
                username: admin
                password: Cisco123
            enable:
                password: Cisco123
        connections:
            a:
              protocol: telnet
              ip: 10.1.1.5
              port: 23
''')

# pick the device to work with
device = testbed.devices['c9300']

# we should be able to directly connect to it
#device.connect()
device.connect(learn_hostname=True)
assert device.connected

# run the various services associated with this connection
#device.execute('show run | i gnxi')
device.configure('''
    gnxi
    gnxi secure-init
    service internal
    gnxi secure-allow-self-signed-trustpoint
''')

device.execute('show run | i gnxi')
# disconnect from it
device.disconnect()