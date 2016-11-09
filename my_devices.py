"""
pynet-rtr1 (Cisco IOS)  184.105.247.70
pynet-rtr2 (Cisco IOS)  184.105.247.71
pynet-sw1  (Arista EOS) 184.105.247.72
pynet-sw2  (Arista EOS) 184.105.247.73
juniper-srx             184.105.247.76
nxos1                   nxos1.twb-tech.com
nxos2                   nxos2.twb-tech.com
"""
from getpass import getpass

std_pwd = getpass("Enter standard password: ")
arista_pwd = getpass("Enter Arista password: ")

pynet_rtr1 = {
    'device_type': 'ios',
    'hostname': '184.105.247.70',
    'username': 'pyclass',
    'password': '88newclass',
    'optional_args': {},
}

pynet_rtr2 = {
    'device_type': 'ios',
    'hostname': '184.105.247.71',
    'username': 'pyclass',
    'password': '88newclass',
    'optional_args': {},
}

pynet_sw1 = {
    'device_type': 'eos',
    'hostname': '184.105.247.72',
    'username': 'pyclass',
    'password': '88newclass',
    'optional_args': {},
}

nxos1 = {
    'device_type': 'nxos',
    'hostname': 'nxos1.twb-tech.com',
    'username': 'pyclass',
    'password': '88newclass',
    'optional_args': {'nxos_protocol': 'https', 'port': 8443}
}

device_list = [
        pynet_rtr1,
        pynet_rtr2,
        pynet_sw1,
        nxos1,
]
