from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

img = Image.open('image.jpg')
draw = ImageDraw.Draw(img)
font = ImageFont.truetype('impact.ttf', 52)


def draw_text_with_outline(text, x, y):
    draw.text((x-2, y-2), text, (0, 0, 0), font=font)
    draw.text((x+2, y-2), text, (0, 0, 0), font=font)
    draw.text((x+2, y+2), text, (0, 0, 0), font=font)
    draw.text((x-2, y+2), text, (0, 0, 0), font=font)
    draw.text((x, y), text, (255, 255, 255), font=font)
    return


def draw_shape_with_outline(fill="black"):
    draw.rectangle(((17, 19), (50, 50)), fill=fill)
    draw.rectangle(((521, 298), (489, 270)), fill="white")
    draw.rectangle(((50, 197), (105, 236)), fill="red")
    draw.rectangle(((246, 89), (302, 123)), fill="orange")
    draw.rectangle(((485, 32), (526, 61)), fill="blue")
    return


def draw_text(text, pos):
    text = text.upper()
    width, height = draw.textsize(text, font)  # measure the size the text will take

    line_count = 1
    if width > img.width:
        line_count = int(round((width / img.width) + 1))

    print(f"line count: {line_count}")

    lines = []
    if line_count > 1:
        last_cut = 0
        is_last = False
        for i in range(0, line_count):
            if last_cut == 0:
                cut = (len(text) / line_count) * i
            else:
                cut = last_cut

            if i < line_count - 1:
                next_cut = (len(text) / line_count) * (i + 1)
            else:
                next_cut = len(text)
                is_last = True

            print(f'cut: {cut} -> {next_cut}')

            # make sure we don't cut words in half
            if next_cut == len(text) or text[int(next_cut)] == ' ':
                print('may cut')
            else:
                print('may not cut')
                while text[int(next_cut)] != ' ':
                    next_cut += 1
                print(f'new cut: {next_cut}')

            line = text[int(cut):int(next_cut)].strip()

            # is line still fitting?
            width, height = draw.textsize(line, font)
            if not is_last and width > img.width:
                print('overshoot')
                next_cut -= 1
                while text[int(next_cut)] != ' ':
                    next_cut -= 1
                print(f'new cut: {next_cut}')

            last_cut = next_cut
            lines.append(text[int(cut):int(next_cut)].strip())
    else:
        lines.append(text)

    print(lines)

    last_y = -height
    if pos == 'bottom':
        last_y = img.height - height * (line_count + 1) - 10

    for i in range(0, line_count):
        width, height = draw.textsize(lines[i], font)
        x = img.width / 2 - width / 2
        y = last_y + height
        draw_text_with_outline(lines[i], x, y)
        last_y = y


def draw_shape(pos, shape='rectangle'):
    if shape == 'rectangle':
        draw_shape_with_outline()
        # draw_shape_with_outline(x=521, y=298, fill="white")
        # draw_shape_with_outline(x=39, y=236, fill="blue")
        # draw_shape_with_outline(x=385, y=142, fill="red")

#
# draw_text('One does not simply', 'top')
# draw_text('leave activo', 'bottom')
#
# img.save('text.jpg')


draw_shape('top')
img.save('rectangle.jpg')
