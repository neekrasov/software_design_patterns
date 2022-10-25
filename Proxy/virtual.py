class Bitmap:
    def __init__(self, filename):
        self.filename = filename
        print('Loading image from {}'.format(filename))

    def draw(self):
        print('Drawing image {}'.format(self.filename))

class LazyBitmap:
    def __init__(self, filename):
        self.filename = filename
        self._bitmap = None

    def draw(self):
        if not self._bitmap:
            self._bitmap = Bitmap(self.filename)
        self._bitmap.draw()

# service
def draw_image(image):
    print('About to draw image')
    image.draw()
    print('Done drawing image')

if __name__ == '__main__':
    bmp = LazyBitmap('facepalm.jpg')
    draw_image(bmp)