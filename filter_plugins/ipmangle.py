# -*- coding: utf-8 -*-
import ipaddress


def ipmangle(d):
    """
    Add and offset to all values

    >>> ipmangle('1.2.3.4', netmask='255.255.0.0')
    2.1
    """
    items = d.split('.')
    numpos = len(items)
    items.extend([u'0', u'0', u'0'])

    return ipaddress.IPv4Address(u'.'.join(items[0:4])).reverse_pointer.split('.', 4 - numpos)[-1] + '.'


class FilterModule(object):
    def filters(self):
        return {'ipmangle': ipmangle}
