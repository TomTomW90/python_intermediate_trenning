"""
https://docs.python.org/3/howto/regex.html#regex-howto
https://docs.python.org/3/library/re.html
https://realpython.com/regex-python/#metacharacters-supported-by-the-re-module
"""

import re


if __name__ == '__main__':
    p = re.compile('[a-z]+')
    m = p.match('abc')
    print(f'{m} - {type(m)}')
