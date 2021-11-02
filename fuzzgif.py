import sys
import giffuzz
import io
import string

import random
def rbytes(n):
    random_bytes = bytes([random.randrange(0, 256) for _ in range(0, n)])
    return random_bytes

class FuzzIO(io.BytesIO):
    def __init__(self):
        self._buffer = []

    def read(self, n=None):
        if n is None:
            v = super().read()
            n = random.randrange(0, 1000)
            res =  rbytes(n)
            self._buffer.extend([i for i in res])
            return res
        else:
            #v = super().read(n)
            res =  rbytes(n)
            self._buffer.extend([i for i in res])
            return res
        return v

    def read_bytes_content(self, n, content):
        self._buffer.extend([i for i in content])
        return content

    def read_u1_content(self, n, content):
        self._buffer.extend([i for i in content])
        return content

    def read_ascii(self, n):
        res = (''.join([random.choice(string.ascii_letters) for i in range(n)])).encode('ASCII')
        self._buffer.extend([i for i in res])
        return res

my_bytes = FuzzIO()
g = giffuzz.Gif.from_io(my_bytes)
print("width = %d" % (g.logical_screen_descriptor.screen_width))
print("height = %d" % (g.logical_screen_descriptor.screen_height))

with open(sys.argv[1], 'wb') as f:
    f.write(bytearray(my_bytes._buffer))
