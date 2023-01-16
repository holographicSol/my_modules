""" Written by Benjamin Jack Cullen
"""


def power_n(*args, power: int) -> list:
    """ accepts *unpacked list """
    return [arg**power for arg in args]


def power_type_checker(*args, typ: type) -> list:
    """ accepts *unpacked list """
    return [[args.index(arg), False] for arg in args if not isinstance(arg, typ)]


def power_make_type(*args, typ: type) -> list:
    """ accepts *unpacked list """
    return [typ(arg) for arg in args]


def power_digit_checker(*args) -> list:
    """ accepts *unpacked list """
    return [[args.index(arg), False] for arg in args if not str(arg).isdigit()]


def power_repr(*args) -> list:
    """ accepts *unpacked list """
    return [repr(arg) for arg in args]


def power_ord(*args) -> list:
    """ accepts *unpacked list """
    return [ord(arg) for arg in args]


def power_chr(*args) -> list:
    """ accepts *unpacked list """
    return [chr(arg) for arg in args]


def power_len(*args) -> list:
    """ accepts *unpacked list """
    return [len(arg) for arg in args]


def power_max(*args) -> list:
    return [max(arg) for arg in args]


def power_min(*args) -> list:
    return [min(arg) for arg in args]

