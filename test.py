import tkinter as tk
from PIL import Image
from PIL import ImageTk
import numpy as np
from tkinter import filedialog
from tkinter.colorchooser import *
from IntensitySlicing import IntensitySlicing
from ColorTransformations import ColorTransf
from Filtering import Smoothing
class DIP(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Color Image Processing")
        self.pack(fill = tk.BOTH, expand = 1)


        self.browseButton = tk.Button(self,text = "Browse",command = self.onOpen)
        self.browseButton.grid(row =0,column=0)
        self.var = tk.IntVar()
        self.buttonradio1 = tk.Radiobutton(self, text="ColorTransformations", variable=self.var, value=1,
                                   command=self.ColorTransfer)
        self.buttonradio2 = tk.Radiobutton(self, text="PseudoColoring", variable=self.var, value=2,
                                   command=self.PseudoColor)
        self.buttonradio3 = tk.Radiobutton(self, text="Smoothing & Sharpening", variable=self.var, value=3,
                                           command=self.Filtering)
        self.buttonradio1.grid(row=1, column=0)
        self.buttonradio2.grid(row=1, column=1)
        self.buttonradio3.grid(row=1, column=2)
        self.label1 = tk.Label(self, border = 5)
        self.label2 = tk.Label(self, border = 25)
        self.label1.grid(row = 8, column = 0)
        self.label2.grid(row = 8, column = 2)
        # filename = "C:/Users/Roopa/Documents/GitHub/assignment-2-roopa-rajala/Lenna.png"
        # self.fn = filename
        # self.img = Image.open(self.fn)
        # self.I = np.asarray(self.img)
        # l, h = self.img.size
        # text = str(2 * l + 100) + "x" + str(h + 50) + "+0+0"
        # self.parent.geometry(text)
        # photo = ImageTk.PhotoImage(self.img)
        # self.label1.configure(image=photo)
        # self.label2.configure(image=photo)
        # self.label1.image = photo  # keep a reference!
        # self.label2.image = photo
        self.convertButton = tk.Button(self, text="Convert", bg="green", command=self.setImage)
        self.convertButton.grid(row=5, column=1)


    def ColorTransfer(self):
        self.colorvar = tk.StringVar()
        self.colorvar2 = tk.StringVar()
        self.colorvar.set('RGB')
        self.colorvar2.set('CMYK')
        dropdownFrom = tk.OptionMenu(self,self.colorvar,"RGB","CMYK")
        dropdownTo = tk.OptionMenu(self,self.colorvar2,"RGB","CMYK","HSI")
        labelTo = tk.Label(self,text="to")
        labelTo.grid(row=3,column=0)
        dropdownFrom.grid(row =2,column=0)
        dropdownTo.grid(row = 4,column=0)
    def PseudoColor(self):
        self.pseudovar = tk.IntVar()
        button3 = tk.Radiobutton(self, text="Intensity Slicing", variable=self.pseudovar, value=1)
        button4 = tk.Radiobutton(self, text="Color Transformation", variable=self.pseudovar, value=2)
        self.slicesNo = tk.StringVar()

        self.slicesNo.set(1)

        dropdownSlices = tk.OptionMenu(self, self.slicesNo, 1, 2, 3, 4, 5, 6, 7, 8, command=self.func)

        dropdownSlices.grid(row=3, column=1)
        button3.grid(row=2, column=1)
        button4.grid(row=4, column=1)
        # colorPick.grid(row=2, column=2)

    def func(self, value):
        self.slider1=[]
        self.sliceNumber = value
        print(value)
        self.labelslider = tk.Label(self,text = "Intensity sliders")
        self.labelslider.grid(row=0,column=4)
        for i in range(value-1):
            self.slider1.append(tk.Scale(self,from_=0,to=255,orient= tk.HORIZONTAL))
            self.slider1[i].set(0)
            self.slider1[i].grid(row=i+1,column=4)


    def Filtering(self):
        self.filtervar = tk.IntVar()
        button3 = tk.Radiobutton(self, text="Smothing", variable=self.filtervar,command=self.filter1, value=1)
        button4 = tk.Radiobutton(self, text="Sharpening", variable=self.filtervar,command=self.filter2, value=2)
        button3.grid(row=2, column=2)
        button4.grid(row=4, column=2)
    def filter1(self):
        self.filtervar1 = tk.IntVar()
        button5 = tk.Radiobutton(self, text="HSI", variable=self.filtervar1, value=1)
        button6 = tk.Radiobutton(self, text="RGB", variable=self.filtervar1, value=2)
        button5.grid(row=3, column=2)
        button6.grid(row=3, column=3)

    def filter2(self):
        self.filtervar2 = tk.IntVar()
        button7 = tk.Radiobutton(self, text="HSI", variable=self.filtervar2, value=1)
        button8 = tk.Radiobutton(self, text="RGB", variable=self.filtervar2, value=2)
        button7.grid(row=5, column=2)
        button8.grid(row=5, column=3)
    def setImage(self):
        ct = ColorTransf()
        i = IntensitySlicing
        f = Smoothing
        if self.var.get()== 1:
            if self.colorvar.get()=='RGB' and self.colorvar2.get()=='CMYK':
                self.setImage1()
                self.output = ct.RGBtoCMYK(self.fn)
                filename = "test.png"
                self.fnout = filename
                self.img = Image.open(self.fnout)
                self.temp = self.img.save("test.ppm","ppm")
                photo = ImageTk.PhotoImage(file = "test.ppm")
                self.label2.configure(image=photo)
                self.label2.image = photo

            elif self.colorvar.get()=='CMYK' and self.colorvar2.get()=='RGB':
                self.output = ct.RGBtoCMYK(self.fn)
                filename = "test.png"
                self.fnout = filename
                self.img = Image.open(self.fnout)
                self.temp = self.img.save("test.ppm", "ppm")
                photo = ImageTk.PhotoImage(file="test.ppm")
                self.label1.configure(image=photo)
                self.label1.image = photo
                self.output = ct.CMYKtoRGB(self.output)
                filename = "test.png"
                self.fnout = filename
                self.img = Image.open(self.fnout)
                self.temp = self.img.save("test.ppm","ppm")
                photo = ImageTk.PhotoImage(file = "test.ppm")
                self.label2.configure(image=photo)
                self.label2.image = photo
            elif self.colorvar.get()=='CMYK' and self.colorvar2.get()=='HSI':
                # self.output = ct.CMYKtoRGB(self.fn)
                # filename = "test.png"
                # self.fnout = filename
                # self.img = Image.open(self.fnout)
                # self.temp = self.img.save("test.ppm", "ppm")
                # photo = ImageTk.PhotoImage(file="test.ppm")
                # self.label1.configure(image=photo)
                # self.label1.image = photo
                self.output = ct.CMYKtoHSV(self.fn)
                filename = "test.png"
                self.fnout = filename
                self.img = Image.open(self.fnout)
                self.temp = self.img.save("test.ppm","ppm")
                photo = ImageTk.PhotoImage(file = "test.ppm")
                self.label2.configure(image=photo)
                self.label2.image = photo
            elif self.colorvar.get()=='RGB' and self.colorvar2.get()=='HSI':
                self.setImage1()
                self.output = ct.RGBtoHSV(self.fn)
                filename = "test.png"
                self.fnout = filename
                self.img = Image.open(self.fnout)
                self.temp = self.img.save("test.ppm","ppm")
                # self.I = np.asarray(self.img)
                # l, h = self.img.size
                # text = str(2 * l + 100) + "x" + str(h + 50) + "+0+0"
                # self.parent.geometry(text)
                photo = ImageTk.PhotoImage(file = "test.ppm")
                self.label2.configure(image=photo)
                self.label2.image = photo
        elif self.var.get() == 2:
            if self.pseudovar.get() == 1:
                max = list()
                maxVal = list()
                max.append(0)
                for j in range(self.sliceNumber-1):
                    max.append(self.slider1[j].get())
                    maxVal.append(max)
                    max=[]
                    max.append(self.slider1[j].get())
                max.append(255)
                maxVal.append(max)
                self.output = i.scale(i,self.fn, maxVal)
                filename = "test.png"
                self.fnout = filename
                self.img = Image.open(self.fnout)
                self.temp = self.img.save("test.ppm", "ppm")
                photo = ImageTk.PhotoImage(file="test.ppm")
                self.label2.configure(image=photo)
                self.label2.image = photo
            elif self.pseudovar.get() == 2:

                self.output = i.transform(i,self.fn)
                filename = "test.png"
                self.fnout = filename
                self.img = Image.open(self.fnout)
                self.temp = self.img.save("test.ppm", "ppm")
                photo = ImageTk.PhotoImage(file="test.ppm")
                self.label2.configure(image=photo)
                self.label2.image = photo
        elif self.var.get() == 3:
            if self.filtervar.get() == 1:
                if self.filtervar1.get() ==1:

                    self.output = f.blurringHSI(f, self.fn)
                    filename = "test.png"
                    self.fnout = filename
                    self.img = Image.open(self.fnout)
                    self.temp = self.img.save("test.ppm", "ppm")
                    # self.I = np.asarray(self.img)
                    # l, h = self.img.size
                    # text = str(2 * l + 100) + "x" + str(h + 50) + "+0+0"
                    # self.parent.geometry(text)
                    photo = ImageTk.PhotoImage(file="test.ppm")
                    self.label2.configure(image=photo)
                    self.label2.image = photo
                else:
                        self.output = f.blurring(f, self.fn)
                        filename = "test.png"
                        self.fnout = filename
                        self.img = Image.open(self.fnout)
                        self.temp = self.img.save("test.ppm", "ppm")
                        # self.I = np.asarray(self.img)
                        # l, h = self.img.size
                        # text = str(2 * l + 100) + "x" + str(h + 50) + "+0+0"
                        # self.parent.geometry(text)
                        photo = ImageTk.PhotoImage(file="test.ppm")
                        self.label2.configure(image=photo)
                        self.label2.image = photo

            elif self.filtervar.get() == 2:
                if self.filtervar2.get() == 1:

                    self.output = f.sharpenHSI(f, self.fn)
                    filename = "test.png"
                    self.fnout = filename
                    self.img = Image.open(self.fnout)
                    self.temp = self.img.save("test.ppm", "ppm")
                    # self.I = np.asarray(self.img)
                    # l, h = self.img.size
                    # text = str(2 * l + 100) + "x" + str(h + 50) + "+0+0"
                    # self.parent.geometry(text)
                    photo = ImageTk.PhotoImage(file="test.ppm")
                    self.label2.configure(image=photo)
                    self.label2.image = photo
                else:
                    self.output = f.sharpening(f, self.fn)
                    filename = "test.png"
                    self.fnout = filename
                    self.img = Image.open(self.fnout)
                    self.temp = self.img.save("test.ppm", "ppm")
                    # self.I = np.asarray(self.img)
                    # l, h = self.img.size
                    # text = str(2 * l + 100) + "x" + str(h + 50) + "+0+0"
                    # self.parent.geometry(text)
                    photo = ImageTk.PhotoImage(file="test.ppm")
                    self.label2.configure(image=photo)
                    self.label2.image = photo


    def onOpen(self):
        #Open Callback
        filename = filedialog.askopenfilename(
            filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")])
        self.fn = filename
        print()
        #print self.fn #prints filename with path here
        self.img = Image.open(self.fn)
        photo = ImageTk.PhotoImage(self.img)
        self.label1.configure(image=photo)
        self.label1.image = photo
    def setImage1(self):
        self.img = Image.open(self.fn)
        photo = ImageTk.PhotoImage(self.img)
        self.label1.configure(image=photo)
        self.label1.image = photo
    #def onError(self):
        #box.showerror("Error", "Could not open file")

def main():

    root = tk.Tk()
    root.configure(background='red')
    tk.Scrollbar(root)
    DIP(root)

    root.geometry("800x600")
    root.mainloop()


if __name__ == '__main__':
    main()