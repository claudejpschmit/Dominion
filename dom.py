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
        
        # Initializing Basic Window 
        # Make dropdown Menu with all Cardnames.
        self.OM_var = tk.StringVar(self.root)
        self.OM_var.set(CARDNAMES[0])
        self.OM = apply(tk.OptionMenu, (self.frm, self.OM_var) + tuple(CARDNAMES))
        self.OM.pack()


    def drawOnePic(self, name, nlabel = 0):
        image = Image.open(CARDS[name].imagePath)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self.frm, image=photo)
        label.image = photo
        if len(self.labels) == 0:
            print "a"
            label.pack()
            self.labels.append(label)
        else:
            print "b"
            self.labels[nlabel].configure(image = photo)
    def drawAllPics(self):
        for name in CARDNAMES:
            image = Image.open(CARDS[name].imagePath)
            photo = ImageTk.PhotoImage(image)
            label = tk.Label(self.frm, image=photo)
            label.image = photo
            label.pack(side="left")
            self.labels.append(label)

    def updateCardPreview(self):
        self.drawOnePic(self.OM_var.get(), 0)
        self.frm.update_idletasks()
        self.cnv.configure(scrollregion=(0,0,self.frm.winfo_width(), self.frm.winfo_height()))

    def run(self):
        self.button = tk.Button(self.frm, text='Update Preview', command=self.updateCardPreview)
        self.button.pack()

        self.drawOnePic(self.OM_var.get())
        
        #----- Resize window ------#
        self.frm.update_idletasks()
        self.cnv.configure(scrollregion=(0,0,self.frm.winfo_width(), self.frm.winfo_height()))
        self.root.mainloop()

if __name__=='__main__':
    Dominion().run()

