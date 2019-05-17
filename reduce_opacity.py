from PIL import ImageEnhance


def reduce_opacity(button, opacity):
    assert 0 <= opacity <= 1
    button = button.copy() if button.mode == 'RGBA' else button.convert('RGBA')
    alpha = button.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    button.putalpha(alpha)
    return button
