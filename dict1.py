#!/usr/bin/env python

net_device = {
    'ip_addr': '172.30.220.1',
    'username': 'admin',
    'password': 'some_pass',
    'vendor': 'cisco',
    'model': '3945',
}

print
for k, v in net_device.items():
    print k, v
