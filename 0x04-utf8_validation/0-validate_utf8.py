#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Validate data as UTF8"""
    bytes = 0
    for num in data:
        bitcodes = format(num, '#010b')[-8:]
        if bytes == 0:
            for bit in bitcodes:
                if bit == '0':
                    break
                bytes += 1
            if bytes == 0:
                continue
            if bytes == 1 or bytes > 4:
                return False
        else:
            if not (bitcodes[0] == '1' and bitcodes[1] == '0'):
                return False
        bytes -= 1
    return bytes == 0
