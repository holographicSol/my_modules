""" Written by Benjamin Jack Cullen
"""
import binascii


def convert_to_ascii(*args: bytes) -> list:
    """ accepts *unpacked list """
    v = []
    [v.append(binascii.b2a_uu(arg)) for arg in args]
    return v


def convert_bits_to_bytes(*args, byteorder: str) -> list:
    """ accepts *unpacked list, byteorder='big', byteorder='little' """
    v = []
    [v.append(arg.to_bytes(((arg.bit_length() + 7) // 8), byteorder).decode()) for arg in args]
    return v


def convert_bytes_to_bits(*args, byteorder: str) -> list:
    """ accepts *unpacked list, byteorder='big', byteorder='little' """
    v = []
    [v.append(bin(int.from_bytes(str(arg).encode(), byteorder)).replace('b', '')) for arg in args]
    return v


def convert_bytes(*args, abbr: True) -> list:
    """ accepts *unpacked list """
    v = []
    ab_name = ['bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB', 'BB', 'GPB']
    full_name = ['bytes', 'Kilobytes', 'Megabytes', 'Gigabytes', 'Terabytes', 'Petabytes', 'Exabytes',
                 'Zettabytes', 'Yottabytes', 'Brontobytes', 'Geopbytes']
    for arg in args:
        for x in ab_name:
            if arg < 1024.0:
                if abbr is True:
                    v.append("%3.1f %s" % (arg, x))
                    break
                elif abbr is False:
                    v.append("%3.1f %s" % (arg, full_name[ab_name.index(x)]))
                    break
            arg /= 1024.0
    return v

