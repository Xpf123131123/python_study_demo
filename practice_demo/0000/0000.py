from PIL import Image, ImageDraw, ImageFont


def add_number_with_image(imageUrl, number, number_color, number_font):
    try:
        im = Image.open(imageUrl)
        w = im.width
        h = im.height
        im.show()

        draw = ImageDraw.Draw(im)
        font = ImageFont.truetype(number_font, 35)

        draw.text((w - 20, 10), number, number_color, font)

        im.save('new_avatar.png')
        im.show()

    except Exception as ex:
        print('error', ex)
    pass

if __name__ == '__main__':
    add_number_with_image('kxrr.png', '5', (255, 0, 0), 'Arial')