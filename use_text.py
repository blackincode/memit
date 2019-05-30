from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img = Image.open('ba.png')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('impact.ttf', 52)


def paint_booked_with_grey(positions):
    for position in positions:
        draw.rectangle((
            (position[0], position[1]),
            (position[0] + 50, position[1] + 40)),
            fill=(192, 192, 192, 0))


def test():
    paint_booked_with_grey([
        (7, 108),
        (137, 110),
        (138, 245),
        (478, 343),
        (476, 665),
    ])
    img.save('merged_2.png')


if __name__ == '__main__':
    test()
