"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage
from random import uniform


N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'

def main():

    original = SimpleImage('images/simba-sq.jpg')
    height = original.height
    width = original.width

    final_image = SimpleImage.blank(WIDTH, HEIGHT)

    # Print
    original = make_recolored_patch(randomize_scale(), randomize_scale(), randomize_scale())
    for y in range(height):
        for x in range(width):
            pixel = original.get_pixel(x, y)
            final_image.set_pixel(x, y, pixel)
            final_image.set_pixel(PATCH_SIZE + x, y, pixel)


    original = make_recolored_patch(randomize_scale(), randomize_scale(), randomize_scale())
    for y in range(height):
        for x in range(width):
            pixel = original.get_pixel(x, y)
            final_image.set_pixel(x, y, pixel)
            final_image.set_pixel(HEIGHT + x, y, pixel)


    original = make_recolored_patch(randomize_scale(), randomize_scale(), randomize_scale())
    for y in range(height):
        for x in range(width):
            pixel = original.get_pixel(x, y)
            final_image.set_pixel(x, y, pixel)
            final_image.set_pixel(x, PATCH_SIZE + y, pixel)


    original = make_recolored_patch(randomize_scale(), randomize_scale(), randomize_scale())
    for y in range(height):
        for x in range(width):
            pixel = original.get_pixel(x, y)
            final_image.set_pixel(x, y, pixel)
            final_image.set_pixel(PATCH_SIZE + x, PATCH_SIZE + y, pixel)


    original = make_recolored_patch(randomize_scale(), randomize_scale(), randomize_scale())
    for y in range(height):
        for x in range(width):
            pixel = original.get_pixel(x, y)
            final_image.set_pixel(x, y, pixel)
            final_image.set_pixel(HEIGHT + x, PATCH_SIZE + y, pixel)


    original = make_recolored_patch(randomize_scale(), randomize_scale(), randomize_scale())
    for y in range(height):
        for x in range(width):
            pixel = original.get_pixel(x, y)
            final_image.set_pixel(x, y, pixel)
            final_image.set_pixel(x, y, pixel)


    # This is an example which should generate a pinkish patch
    final_image.show()


def make_recolored_patch(red_scale, green_scale, blue_scale):

    patch = SimpleImage('images/simba-sq.jpg')

    for pixel in patch:
        pixel.red *= red_scale
        pixel.green *= green_scale
        pixel.blue *= blue_scale
    return patch


def randomize_scale():
    n = uniform(0, 3)
    return n


if __name__ == '__main__':
    main()
