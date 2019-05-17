from PIL import Image

from reduce_opacity import reduce_opacity


template = Image.open('ba.png')


def merge_booked_into_template(positions):
    booked = reduce_opacity(Image.open('booked.png'), 1)
    for position in positions:
        template.paste(
            booked,
            (
                position[0],
                position[1],
            )
        )


def test():
    merge_booked_into_template([
        (7, 108),
        (137, 110),
        (138, 245),
        (478, 343),
        (476, 665),
    ])
    template.save('merged.png')


if __name__ == '__main__':
    test()
