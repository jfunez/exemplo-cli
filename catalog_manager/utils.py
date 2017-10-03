# -*- coding: utf-8 -*-


class Singleton(object):
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instances[cls]


def read_input(input_msg):
    value = ''
    while not(value):
        value = input('\t> %s: ' % input_msg)
        value = value.strip()
        if value != '':
            break

    return value
