from PIL import Image, ImageDraw
import math
import random


def pascal_triangle_random(width, num, beg):
    x = width
    y = width
    im = Image.new("RGB", (x, y))
    id = ImageDraw.Draw(im, "RGB")
    start = [(0, y), (x, y), (x/2, 0)]
    old = beg
    new = 0

    for i in range(num):
        r = random.randrange(3)
        new = ((start[r][0]+old[0])/2, (start[r][1]+old[1])/2)
        id.point(new, "white")
        old = new
    im.save("pascals.jpg")


def pascal_triangle_formula(width):
    def n_choose_k(xy):
        if xy[0] - xy[1] > 0:
            return math.factorial(xy[0])/(math.factorial(xy[1])*math.factorial(xy[0]-xy[1]))
        return 2
    num = 0
    im = Image.new("RGB", (width, width), color = "white")
    id = ImageDraw.Draw(im, "RGB")
    for x in range(1, width+1 , ):
        for y in range(1, width+1):
            num = n_choose_k((x, y))
            if num % 2 != 0:
                id.point((x, y), "white")
    im.save("pascal2.jpg")

def pascal_triangle_polygons(width):
    def draw_triangle(mid, )





