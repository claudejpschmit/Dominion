import Tkinter as tk
from PIL import Image, ImageTk
from Libraries import *

class Dominion (object):
    def __init__(self):
        self.root=tk.Tk()
        self.scale = 3
        self.root.tk.call('tk', 'scaling', self.scale)
        self.fontSize = 6
        self.root.minsize(width=int(self.scale*1920), height=int(self.scale*1080))
        self.labels = []
        self.root.grid_rowconfigure(0,weight=1)
        self.root.grid_columnconfigure(0,weight=1)
        self.cnv = tk.Canvas(self.root)
        self.cnv.grid(row=0,column=0,sticky='nswe')
        self.hScroll = tk.Scrollbar(self.root, orient=tk.HORIZONTAL, command = self.cnv.xview, width = int(self.scale*16))
        self.hScroll.grid(row=1, column=0, sticky='we')
        self.vScroll = tk.Scrollbar(self.root, orient=tk.VERTICAL, command = self.cnv.yview, width = int(self.scale*16))
        self.vScroll.grid(row=0, column=1, sticky='ns')
        self.cnv.configure(xscrollcommand=self.hScroll.set,yscrollcommand=self.vScroll.set)
        self.frm = tk.Frame(self.cnv, bg='white')
        self.cnv.create_window(0,0,window=self.frm,anchor='nw')
        self.imageScale = 0.7 
        # Initializing Basic Window 
        # Make dropdown Menu with all Cardnames.
        self.OM_var = tk.StringVar(self.root)
        self.OM_var.set(CARDNAMES[0])
        self.OM = apply(tk.OptionMenu, (self.frm, self.OM_var) + tuple(CARDNAMES))
        self.OM.config(bg='white', width=10, font=('Helvetica',int(self.fontSize*self.scale)))
        self.OM.grid(row = 1, column = 0)

        # Generate some Title text
        self.titleLabel = tk.Label(self.frm, text="DOMINION - Card Randomizer",\
                bg='blue', fg='white', font=('Helvetica',int(self.fontSize*self.scale)))
        self.titleLabel.grid(row=0, columnspan=2, pady = 10)
        
        # Generate Checkboxes for expansions
        self.Descr = tk.Label(self.frm, text="Check Expansions from which cards will be picked.",\
                bg='blue', fg='white', font=('Helvetica',int(self.fontSize*self.scale)))
        self.Descr.grid(row=3, columnspan=2, pady = 10)
        self.labOpt = tk.Label(self.frm, text="Options:", bg='pink',\
                font=('Helvetica',int(self.fontSize*self.scale))).grid(row = 4, column=0, sticky="W")
        self.lab = tk.Label(self.frm, text="Selection:", bg='pink',\
                font=('Helvetica',int(self.fontSize*self.scale))).grid(row = 4, column=1, sticky="W")

        ###################
        self.toggles = []
        nBox = 0
        self.CheckBoxVars = []
        self.MAXROW = 5

        self.image_on = Image.open('./Resources/toggle_on.gif')
        self.image_off = Image.open('./Resources/toggle_off.gif')
        self.toggleWidth = self.image_on.size[0]
        self.toggleHeight = self.image_on.size[1]
        A = 0.25 * self.scale
        self.image_on = self.image_on.resize((int(A*self.toggleWidth),int(A*self.toggleHeight)), Image.ANTIALIAS)
        self.image_off = self.image_off.resize((int(A*self.toggleWidth),int(A*self.toggleHeight)), Image.ANTIALIAS)
        self.photo_on = ImageTk.PhotoImage(self.image_on)
        self.photo_off = ImageTk.PhotoImage(self.image_off)
        #self.toggleLabel = tk.Label(self.frm,image=self.image_off)
        #self.toggleLabel.image=self.image_off

        self.frm2 = tk.Frame(self.frm, height=100,width=300,bg="white")
        self.frm2.grid(row=5,column =0, sticky="W", pady=5*self.scale)

        self.N = 0
        for name in EXPANSION_NAMES_CHR:
            var = tk.IntVar(value=0)
            toggle = tk.Label(self.frm2,image=self.photo_off, bg="white", textvariable=var)
            toggle.image=self.photo_off
            toggle.grid(row = self.N, column=0, sticky="W", padx=5*self.scale)
            toggle.bind("<Button-1>", self.updateToggle) 
            lab = tk.Label(self.frm2, text=EXPANSIONS[name].Name, bg='white', font=('Helvetica',int(self.fontSize*self.scale)))
            lab.grid(row = self.N, column=1, sticky="W")
            self.N+=1
            self.toggles.append(toggle)
            self.CheckBoxVars.append(var)
            self.MAXROW +=1

        ##################################
        #self.CheckBoxes = []
        #nBox = 0
        #self.CheckBoxVars = []
        #self.MAXROW = 4
        #self.image_off = Image.open('./Resources/toggle_off.jpg')
        #imageWidth = self.image_off.size[0]
        #imageHeight = self.image_off.size[1]
        #scale = 0.7
        #self.image_off = self.image_off.resize((int(scale*imageWidth),int(scale*imageHeight)), Image.ANTIALIAS)
        #self.photoA = ImageTk.PhotoImage(self.image_off)
        #self.l = tk.Label(self.frm, image=self.photoA).grid()
        #for name in EXPANSION_NAMES_CHR:
        #    var = tk.IntVar()
        #    box = tk.Checkbutton(self.frm, text= EXPANSIONS[name].Name,\
        #            variable=var, bg='white', font=('Helvetica',int(self.fontSize*self.scale)),\
        #            indicatoron=True, selectimage=self.photoA)
        #    box.grid(row = 5+nBox, columnspan=1, sticky="W")
        #    nBox+=1
        #    self.CheckBoxes.append(box)
        #    self.CheckBoxVars.append(var)
        #    self.MAXROW +=1
        #self.ExpansionsSelected = []
        #self.lab = tk.Label(self.frm, text="Selection:", bg='pink',\
        #        font=('Helvetica',int(self.fontSize*self.scale))).grid(row = 4, column=1, sticky="W")
        #self.selectionPrintLabels = []
#
    def registerCheckBoxes(self):
        counter = 0
        self.ExpansionsSelected = []
        for var in self.CheckBoxVars:
            counter +=1
            if var.get():
                self.ExpansionsSelected.append(EXPANSION_NAMES_CHR[counter-1])
        self.printCheckBoxSelection()

    def printCheckBoxSelection(self):
        counter = 1
        for name in self.ExpansionsSelected:
            if len(self.selectionPrintLabels) < counter:
                label = tk.Label(self.frm, text = "> " + EXPANSIONS[name].Name,\
                        font=('Helvetica',int(self.fontSize*self.scale)))
                label.grid(row = 4+counter, column = 1, sticky='W')
                self.selectionPrintLabels.append(label)
            else:
                self.selectionPrintLabels[counter-1].config(text = "> " + EXPANSIONS[name].Name,\
                        font=('Helvetica',int(self.fontSize*self.scale)))
    
            counter +=1
        if len(self.selectionPrintLabels)>(counter-1):
            for i in range(counter-1,len(self.selectionPrintLabels)):
                self.selectionPrintLabels[i].destroy()
        newSelection = []
        for i in range(0, counter-1):
            newSelection.append(self.selectionPrintLabels[i])
        self.selectionPrintLabels = newSelection

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
        self.drawOnePic(self.OM_var.get(), 0, self.scale*self.imageScale)
        self.frm.update_idletasks()
        self.cnv.configure(scrollregion=(0,0,self.frm.winfo_width(), self.frm.winfo_height()))
    def updateToggle(self, event):
        l = event.widget
        if l.cget("textvariable") == 1:
            l.configure(image=self.photo_off)
            l.configure(textvariable = 0) 
                #imagel.configure(image=image_on)
                #imagel.image=image_on
        else:
            l.configure(image=self.photo_on)
            l.configure(textvariable = 1) 
            #imagel.configure(image=image_off)
            #imagel.image=image_off

    def run(self):
        self.button = tk.Button(self.frm, text='Update Preview',\
                command=self.updateCardPreview, font=('Helvetica',int(self.fontSize*self.scale)))
        self.button.grid(row=1, column = 1)
        self.drawOnePic(self.OM_var.get(), scale = self.imageScale*self.scale)
        
        self.button2 = tk.Button(self.frm, text='Apply Selection',\
                command=self.registerCheckBoxes, font=('Helvetica',int(self.fontSize*self.scale)))
        self.button2.grid(row=self.MAXROW+1, columnspan = 2)
        self.MAXROW+=1
        #----- Resize window ------#
        self.frm.update_idletasks()
        self.cnv.configure(scrollregion=(0,0,self.frm.winfo_width(), self.frm.winfo_height()))
        self.root.mainloop()

if __name__=='__main__':
    Dominion().run()

