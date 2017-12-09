import cv2
import numpy as np
import math


class ColorTransf():

    def RGBtoCMYK(self, filename):
        img = cv2.imread(filename)
        h, w, c = np.shape(img)
        cmyk_img = np.zeros((h, w, 4), dtype="uint8")
        print(h, w, c)
        for i in range(h):
            for j in range(w):
                r = img[i][j][2]
                g = img[i][j][1]
                b = img[i][j][0]
                c = 1 - r / 255
                m = 1 - g / 255
                y = 1 - b / 255
                min_cmy = min(c, m, y)
                if min_cmy==1:
                    cmyk_img[i][j][0]=0
                    cmyk_img[i][j][1] = 0
                    cmyk_img[i][j][2] = 0
                    cmyk_img[i][j][3] = 0
                else:
                    cmyk_img[i][j][0] = 100 * (c - min_cmy) / (1 - min_cmy)
                    cmyk_img[i][j][1] = 100 * (m - min_cmy) / (1 - min_cmy)
                    cmyk_img[i][j][2] = 100 * (y - min_cmy) / (1 - min_cmy)
                    cmyk_img[i][j][3] = 100 * min_cmy

        cv2.imwrite("test.png", cmyk_img)
        return cmyk_img

    def CMYKtoRGB(self, cmyk_img):
        #cmyk_img = self.RGBtoCMYK(filename)
        # img = cv2.imread(filename)
        h, w, c = np.shape(cmyk_img)
        print(c)
        rgb_img = np.zeros((h, w, 3), dtype="uint8")
        print(h, w, c)
        for i in range(h):
            for j in range(w):
                c = cmyk_img[i][j][0] / 100.0
                m = cmyk_img[i][j][1] / 100.0
                y = cmyk_img[i][j][2] / 100.0
                k = cmyk_img[i][j][3] / 100.0
                rgb_img[i][j][2] = round(255.0 - ((min(1.0, c * (1.0 - k) + k)) * 255.0))
                rgb_img[i][j][1] = round(255.0 - ((min(1.0, m * (1.0 - k) + k)) * 255.0))
                rgb_img[i][j][0] = round(255.0 - ((min(1.0, y * (1.0 - k) + k)) * 255.0))
        cv2.imwrite("test.png", rgb_img)
        return rgb_img

    def RGBtoHSV(self, filename):
        img = cv2.imread(filename)
        row, col, c = np.shape(img)
        hsv_img = np.zeros((row, col, 3), dtype="uint8")
        print(row, col, c)
        for i in range(row):
            for j in range(col):
                r = img[i][j][2] / 255.0
                g = img[i][j][1] / 255.0
                b = img[i][j][0] / 255.0

                maxi = max(r, g, b)
                mini = min(r, g, b)

                # RGB to HSV implemetation
                v = maxi
                delta = maxi - mini;
                if maxi == 0:
                    r = 0
                    g = 0
                    b = 0
                    s = 0
                    h = -1

                else:
                    s = delta / maxi
                    if r == maxi:
                        h = ((g - b) / delta) % 6
                    elif g == maxi:
                        h = 2 + ((b - r) / delta)
                    elif b == maxi:
                        h = 4 + (r - g) / delta
                    if h < 0:
                        h = h + 360
                    h = h / 6
                hsv_img[i][j][0] = h * 255
                hsv_img[i][j][1] = s * 255
                hsv_img[i][j][2] = v * 255
        cv2.imwrite("test.png", hsv_img)
        return hsv_img

    def HSVtoRGB(self, filename):
        hsv_img = cv2.imread(filename)
        row, col, c = np.shape(hsv_img)
        rgb_img = np.zeros((row, col, 3), dtype="uint8")
        print(row, col, c)
        for i in range(row):
            for j in range(col):
                fH = hsv_img[i][j][0] / 255.0
                fS = hsv_img[i][j][1] / 255.0
                fV = hsv_img[i][j][2] / 255.0
                fC = fV * fS;
                fHPrime = (fH / 60.0) % 6
                fX = fC * (1 - abs((fHPrime % 2) - 1));
                fM = fV - fC;
                if 0 <= fHPrime and fHPrime < 1:
                    fR = fC;
                    fG = fX;
                    fB = 0;
                elif 1 <= fHPrime and fHPrime < 2:
                    fR = fX;
                    fG = fC;
                    fB = 0;
                elif 2 <= fHPrime and fHPrime < 3:
                    fR = 0;
                    fG = fC;
                    fB = fX;
                elif 3 <= fHPrime and fHPrime < 4:
                    fR = 0;
                    fG = fX;
                    fB = fC;
                elif 4 <= fHPrime and fHPrime < 5:
                    fR = fX;
                    fG = 0;
                    fB = fC;
                elif 5 <= fHPrime and fHPrime < 6:
                    fR = fC;
                    fG = 0;
                    fB = fX;
                else:
                    fR = 0;
                    fG = 0;
                    fB = 0;

                fR += fM;
                fG += fM;
                fB += fM;

                r = fR
                g = fG
                b = fB

                rgb_img[i][j][2] = int(r * 255)
                rgb_img[i][j][1] = int(g * 255)
                rgb_img[i][j][0] = int(b * 255)
        cv2.imwrite("test.png", rgb_img)
        return rgb_img

    def CMYKtoHSV(self, filename):
        img = cv2.imread(filename)
        temp_img = self.CMYKtoRGB(img)
        hsv_img = self.RGBtoHSV("test.png")
        cv2.imwrite("test.png", hsv_img)
        return hsv_img

    def HSVtoCMYK(self, filename):
        temp_img = self.HSVtoRGB(filename)
        cmyk_img = self.RGBtoCMYK(filename)
        cv2.imwrite("test.png", cmyk_img)
        return cmyk_img