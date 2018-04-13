import Tkinter as tk
from PIL import Image, ImageTk
from Libraries import *

class Dominion (object):
    def __init__(self):
        self.root=tk.Tk()
        self.root.minsize(width=1920, height=1080)
        self.labels = []
        self.root.grid_rowconfigure(0,weight=1)
        self.root.grid_columnconfigure(0,weight=1)
        self.cnv = tk.Canvas(self.root)
        self.cnv.grid(row=0,column=0,sticky='nswe')
        self.hScroll = tk.Scrollbar(self.root, orient=tk.HORIZONTAL, command = self.cnv.xview)
        self.hScroll.grid(row=1, column=0, sticky='we')
        self.vScroll = tk.Scrollbar(self.root, orient=tk.VERTICAL, command = self.cnv.yview)
        self.vScroll.grid(row=0, column=1, sticky='ns')
        self.cnv.configure(xscrollcommand=self.hScroll.set,yscrollcommand=self.vScroll.set)
        self.frm = tk.Frame(self.cnv)
        self.cnv.create_window(0,0,window=self.frm,anchor='nw')
        self.imageScale = 0.7 
        # Initializing Basic Window 
        # Make dropdown Menu with all Cardnames.
        self.OM_var = tk.StringVar(self.root)
        self.OM_var.set(CARDNAMES[0])
        self.OM = apply(tk.OptionMenu, (self.frm, self.OM_var) + tuple(CARDNAMES))
        self.OM.grid(row = 1, column = 0)


    def drawOnePic(self, name, nlabel = 0, scale = 1):
        image = Image.open(CARDS[name].imagePath)
        imageWidth = image.size[0]
        imageHeight = image.size[1]
        image = image.resize((int(scale*imageWidth),int(scale*imageHeight)), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self.frm, image=photo)
        label.image = photo
        if len(self.labels) == 0:
            label.grid(row = 2, column = 0, columnspan = 2, padx=15)
            self.labels.append(label)
        else:
            self.labels[nlabel].configure(image = photo)
    def drawAllPics(self):
        for name in CARDNAMES:
            image = Image.open(CARDS[name].imagePath)
            photo = ImageTk.PhotoImage(image)
            label = tk.Label(self.frm, image=photo)
            label.image = photo
            #label.pack(side=tk.BOTTOM)
            self.labels.append(label)

    def updateCardPreview(self):
        self.drawOnePic(self.OM_var.get(), 0, self.imageScale)
        self.frm.update_idletasks()
        self.cnv.configure(scrollregion=(0,0,self.frm.winfo_width(), self.frm.winfo_height()))

    def run(self):
        self.button = tk.Button(self.frm, text='Update Preview', command=self.updateCardPreview)
        self.button.grid(row=1, column = 1)

        self.drawOnePic(self.OM_var.get(), scale = self.imageScale)
        
        #----- Resize window ------#
        self.frm.update_idletasks()
        self.cnv.configure(scrollregion=(0,0,self.frm.winfo_width(), self.frm.winfo_height()))
        self.root.mainloop()

if __name__=='__main__':
    Dominion().run()

