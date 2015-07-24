import struct

PIXEL_WIDTH, PIXEL_HEIGHT = 1500, 1000
X_MIN, X_MAX = -2.5, 1.
Y_MIN, Y_MAX = -1., 1.
MAX_ITERATIONS = 1000

X_WIDTH = X_MAX - X_MIN
Y_HEIGHT = Y_MAX - Y_MIN

BLACK = struct.pack('BBB', 0x00, 0x00, 0x00)
WHITE = struct.pack('BBB', 0xff, 0xff, 0xff)


def main():
    """Write a black and white mandelbrot set as a BMP file."""
    write = open('M.bmp', 'wb').write

    # Standard BMP header
    header = 'BM' + struct.pack('<QIIHHHH',
                                PIXEL_WIDTH * PIXEL_HEIGHT * 3 + 26,
                                26, 12, PIXEL_WIDTH, PIXEL_HEIGHT, 1, 24)
    write(header)

    for Py in xrange(PIXEL_HEIGHT):
        for Px in xrange(PIXEL_WIDTH):
            pixel = BLACK if get_pixel_value(Px, Py) else WHITE
            write(pixel)


def get_pixel_value(x_pixel, y_pixel):
    """Return whether the given pixel is in the mandelbrot set."""
    x0 = float(x_pixel) / PIXEL_WIDTH * X_WIDTH + X_MIN
    y0 = float(y_pixel) / PIXEL_HEIGHT * Y_HEIGHT + Y_MIN
    c = complex(x0, y0)
    z = 0j

    for _ in xrange(MAX_ITERATIONS):
        z = z ** 2 + c
        if abs(z) > 2:
            return False
    return True

if __name__ == '__main__':
    main()
