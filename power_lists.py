""" Written by Benjamin Jack Cullen
"""


def power_n(*args, power: int) -> list:
    """ accepts *unpacked list """
    return [arg**power for arg in args]


def power_type_checker(*args, typ: type) -> list:
    """ accepts *unpacked list """
    v = []
    [v.append([args.index(arg), False]) for arg in args if not isinstance(arg, typ)]
    return v


def power_make_type(*args, typ: type) -> list:
    """ accepts *unpacked list """
    v = []
    [v.append(typ(arg)) for arg in args]
    return v


def power_digit_checker(*args) -> list:
    """ accepts *unpacked list """
    v = []
    [v.append([args.index(arg), False]) for arg in args if not str(arg).isdigit()]
    return v


def power_repr(*args) -> list:
    """ accepts *unpacked list """
    v = []
    [v.append(repr(arg)) for arg in args]
    return v
