import math
import numpy as np
import cv2
from scipy import ndimage
class Smoothing:
    def get_gaussian_low_pass_filter(self):
        #k = (1 / 16) * np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])
        # k=(1/273)*np.array([[1,4,7,4,1],[4,16,26,16,4],[7,26,41,26,7],[4,16,26,16,4],[1,4,7,4,1]])
        k = (1 / 256) * np.array(
            [[1, 4, 6, 4, 1], [4, 16, 24, 16, 4], [6, 24, 36, 24, 6], [4, 16, 24, 16, 4], [1, 4, 6, 4, 1]])
        return k

    def get_gaussian_high_pass_filter(self):
        # k = (1 / 273) * np.array(
        #     [[1, 4, 7, 4, 1], [4, 16, 26, 16, 4], [7, 26, 41, 26, 7], [4, 16, 26, 16, 4], [1, 4, 7, 4, 1]])
        k = (-1 / 256) * np.array([[1, 4, 6, 4, 1], [4, 16, 24, 16, 4], [6, 24, -476, 24, 6], [4, 16, 24, 16, 4], [1, 4, 6, 4, 1]])
        print(k)
        return k

    #FinaL smoothing function using opencv2 convolution filter
    def blurring(self, image):
        image = cv2.imread(image)
        b, g, r = cv2.split(image)
        k = self.get_gaussian_low_pass_filter(self)
        blurr = cv2.filter2D(r, -1, k)
        blurg = cv2.filter2D(g, -1, k)
        blurb = cv2.filter2D(b, -1, k)
        blur = cv2.merge((blurb, blurg, blurr))
        cv2.imwrite("test.png", blur)
        return blur
    #smoothing function using scipy convolution filter
    def blurringScipy(self, image):
        b, g, r = cv2.split(image)
        k = self.get_gaussian_low_pass_filter(self)
        blur_red = ndimage.convolve(r, k, mode='constant', cval=0.0)
        blur_blue = ndimage.convolve(b, k, mode='constant', cval=0.0)
        blur_green = ndimage.convolve(g, k, mode='constant', cval=0.0)
        # blurred_face = ndimage.gaussian_filter(image, sigma=3)
        blur = cv2.merge((blur_blue, blur_green, blur_red))
        cv2.imwrite("test.png", blur)
        return blur
    def blurringHSI(self, image):
        image = cv2.imread(image)
        image=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
        h, s, i  = cv2.split(image)
        k = self.get_gaussian_low_pass_filter(self)
        bluri = cv2.filter2D(i, -1, k)
        blur = cv2.merge((h, s, bluri))
        blur = cv2.cvtColor(blur,cv2.COLOR_HSV2BGR)
        # cv2.imshow("image", blur)
        # cv2.waitKey(0)
        cv2.imwrite("test.png", blur)
        return blur
    def sharpenHSI(self, image):
        image = cv2.imread(image)
        h, s, i  = cv2.split(image)
        k = self.get_gaussian_high_pass_filter(self)
        sharpi = cv2.filter2D(i, -1, k)
        sharp = cv2.merge((h, s, sharpi))
        # cv2.imshow("image", sharp)
        # cv2.waitKey(0)
        cv2.imwrite("test.png", sharp)
        return sharp
#sharpening using opencv2 convolution filter
    def sharpening(self, image):
        image = cv2.imread(image)
        b, g, r = cv2.split(image)
        k = self.get_gaussian_high_pass_filter(self)
        sharpr = cv2.filter2D(r, -1, k)
        sharpg = cv2.filter2D(g, -1, k)
        sharpb = cv2.filter2D(b, -1, k)
        sharp = cv2.merge((sharpb, sharpg, sharpr))
        cv2.imwrite("test.png", sharp)
        return
    def sharpeningedge(self, image):
        blur=self.blurring(self,image)
        edge =  image + image - blur
        # cv2.imshow("image", edge)
        # cv2.waitKey(0)
        return
