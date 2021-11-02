import sys
import gif
import io
import string

with open(sys.argv[1], 'rb') as f:
    my_bytes = io.BytesIO(f.read())
g = gif.Gif.from_io(my_bytes)
print("width = %d" % (g.logical_screen_descriptor.screen_width))
print("height = %d" % (g.logical_screen_descriptor.screen_height))
