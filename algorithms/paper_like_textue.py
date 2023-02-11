import cv2
import numpy as np

BG_COLOR = 209
BG_SIGMA = 5
MONOCHROME = 1

class GenerateTexture:

    def blank_image(self, width=1024, height=1024, background=BG_COLOR):
        """
        It creates a blank image of the given background color
        """
        img = np.full((height, width, MONOCHROME), background, np.uint8)
        return img

    def add_noise(self, img, sigma=BG_SIGMA):
        """
        Adds noise to the existing image
        """
        width, height, ch = img.shape
        n = self.noise(width, height, sigma=sigma)
        img = img + n
        return img.clip(0, 255)

    def noise(self, width, height, ratio=1, sigma=BG_SIGMA):
        """
        The function generates an image, filled with gaussian nose. If ratio parameter is specified,
        noise will be generated for a lesser image and then it will be upscaled to the original size.
        In that case noise will generate larger square patterns. To avoid multiple lines, the upscale
        uses interpolation.

        :param ratio: the size of generated noise "pixels"
        :param sigma: defines bounds of noise fluctuations
        """
        mean = 0
        print(width, height, ratio)
        assert width % ratio == 0, "Can't scale image with of size {} and ratio {}".format(width, ratio)
        assert height % ratio == 0, "Can't scale image with of size {} and ratio {}".format(height, ratio)

        h = int(height / ratio)
        w = int(width / ratio)

        result = np.random.normal(mean, sigma, (w, h, MONOCHROME))
        if ratio > 1:
            result = cv2.resize(result, dsize=(width, height), interpolation=cv2.INTER_LINEAR)
        return result.reshape((width, height, MONOCHROME))


    def texture(self, image, sigma=BG_SIGMA, turbulence=2):
        """
        Consequently applies noise patterns to the original image from big to small.

        sigma: defines bounds of noise fluctuations
        turbulence: defines how quickly big patterns will be replaced with the small ones. The lower
        value - the more iterations will be performed during texture generation.
        """
        result = image.astype(float)
        cols, rows, ch = image.shape
        ratio = cols
        while not ratio == 1:
            result += self.noise(cols, rows, ratio, sigma=sigma)
            ratio = (ratio // turbulence) or 1
        cut = np.clip(result, 0, 255)
        return cut.astype(np.uint8)

if __name__ == '__main__':
    __genTexture =  GenerateTexture()
    blank_image = __genTexture.blank_image(background=230)
    texture = __genTexture.texture(blank_image, sigma = 4, turbulence = 4)
    texture_noise = __genTexture.add_noise(texture, sigma = 10)
    noise = __genTexture.add_noise(blank_image, sigma = 10)

    

    print(blank_image.shape)
    print(texture.shape)
    cv2.imwrite('blank_image.png', blank_image)
    cv2.imwrite('texture.png', texture)
    cv2.imwrite('texture_and_noise.png', texture_noise)
    cv2.imwrite('noise.png', noise)
    #cv2.imwrite('noise.jpg', genTexture.add_noise(genTexture.blank_image(1920, 1280), sigma=10))
    print ('done')