# -*- coding: utf-8 -*-

import random
import string


class KeyGenerator():
    """
    class: KeyGenerator | used to define an object to print keys with defined length and numbers.
    Usage:      key = KeyGenerator(key_length)
                key.print_key(key_num)
    """
    def __init__(self, length):
        self.length = length
        # self.num = num

    def __setattr__(self, key, value):
        if key == 'length':
            if value <= 0:
                raise ValueError ('输入的验证码长度不合法')
        return object.__setattr__(self, key, value)

    def create_key(self):
        key_strings = string.ascii_letters
        key_list = [random.choice(key_strings) for x in range(self.length)]
        return ''.join(key_list)

    def print_key(self, num):
        for i in range(num):
            key = self.create_key()
            print(key)


if __name__ == '__main__':
    key_num = 200
    key_length = 20
    key = KeyGenerator(key_length)
    key.print_key(key_num)
    # print(key.__doc__)
    # print string.letters
    # print string.digits
    # print string.printable
    # print string.punctuation
    # print string.hexdigits
    # print string.octdigits
