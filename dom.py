import Tkinter as tk
from PIL import Image, ImageTk
from Libraries import *
import random as rd
import sys


if sys.platform == "win32":
    # Windows...
    from win32api import GetSystemMetrics


# Maybe a better design philosophy is that _init_ doesnt create all the buttonss and things, but 
# instead just calls functions that create these things. That way it should be a bit cleaner and easier to 
# look at.

# Choose this to be either true or false, only working for Linux
HIDPI = True

class Dominion (object):
    def __init__(self):
        self.root=tk.Tk()
        
        if sys.platform == "linux" or sys.platform == "linux2":
            # linux
            print "linux"
            if HIDPI:
                self.scale = 1.5
                self.fontSize = 8
                self.winWidth = 1920
                self.winHeight = 1000
            else:
                self.scale = 1
                self.fontSize = 8
                self.winWidth = 1920
                self.winHeight = 1000
        elif sys.platform == "darwin":
            # OS X
            print "os X"
        elif sys.platform == "win32":
            # Windows...
            self.scale = 1
            self.fontSize = 14
            self.winWidth = GetSystemMetrics(0)
            self.winHeight = GetSystemMetrics(1)

        self.root.tk.call('tk', 'scaling', self.scale)
        self.root.bind("<Escape>", self._close)
        self.root.minsize(width=int(self.scale*self.winWidth), height=int(self.scale*self.winHeight))
        self.labels = []
        self.root.grid_rowconfigure(0,weight=1)
        self.root.grid_columnconfigure(0,weight=1)
        self.cnv = tk.Canvas(self.root)
        self.cnv.grid(row=0,column=0,sticky='nswe')

        self.hScroll = tk.Scrollbar(self.root, orient=tk.HORIZONTAL,\
                command = self.cnv.xview, width = int(self.scale*16))
        self.hScroll.grid(row=1, column=0, sticky='we')
        
        self.vScroll = tk.Scrollbar(self.root, orient=tk.VERTICAL,\
                command = self.cnv.yview, width = int(self.scale*16))
        self.vScroll.grid(row=0, column=1, sticky='ns')
        self.cnv.configure(xscrollcommand=self.hScroll.set,\
                yscrollcommand=self.vScroll.set)
        self.frm = tk.Frame(self.cnv, bg='white')
        self.cnv.create_window(0,0,window=self.frm,anchor='nw')
        self.imageScale = 0.8
        
        if sys.platform == "linux" or sys.platform == "linux2":
            self.cnv.bind_all("<Button-4>", self._on_mousewheel_up)
            self.cnv.bind_all("<Button-5>", self._on_mousewheel_down)
        elif sys.platform == "win32":
            self.cnv.bind_all("<MouseWheel>", self._on_mousewheel)
        
        # Drag Scrolling
        self.cnv.bind_all("<Button-1>", self._scroll_start)
        self.cnv.bind_all("<B1-Motion>", self._scroll_move)
        self.cnv.bind_all("<ButtonRelease-1>", self._reset_cursor)
        # Initializing Basic Window 

        # Make menubar, toolbar and statusbar
        self.__createMenuBar__()
        self.__createToolBar__()
        self.__createStatusBar__()

        # Make dropdown Menu with all Cardnames.
        self.__createCardViewerMenu__()

        # Generate some Title text
        self.__createTitle__()
                
        # Generate Checkboxes for expansions
        self.__createExpansionCheckboxes__()
         # Generate Checkboxes for options
        self.__createOptionsCheckboxes__()

        # Define Variable for which expansions have been selected.
        self.ExpansionsSelected = []
        
        # Define card pool
        self.CardPool = []

        # Define card selection
        self.CardSelection = []

        # Make some Buttons inside frame 1
        self.__createCardViewerButton__()
        self.__createDrawSampleButton__()
        self.MAXROW+=1
    
        # Display previe pic
        self.drawOnePic(self.OM_var.get(), scale = self.imageScale*self.scale)
        
        # A geometry update
        self.frm.update_idletasks()

        # make second frame to display the selection.
        self.displayfrm = tk.Frame(self.cnv, bg='blue')
        self.cnv.create_window(self.frm.winfo_reqwidth(),0,\
                window=self.displayfrm,anchor='nw')
        
    def doNothing(self):
        pass

    def __createMenuBar__(self):
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        self.subMenu1 = tk.Menu(self.menu)
        self.menu.add_cascade(label="Menu 1", menu=self.subMenu1,\
                font=('Helvetica',int(self.fontSize*self.scale)))
        self.subMenu1.add_command(label="Command 1", command=self.doNothing,\
                font=('Helvetica',int(self.fontSize*self.scale)))
        self.subMenu1.add_command(label="Command 2", command=self.doNothing,\
                font=('Helvetica',int(self.fontSize*self.scale)))
        self.subMenu1.add_command(label="Command 3", command=self.doNothing,\
                font=('Helvetica',int(self.fontSize*self.scale)))
        self.subMenu1.add_separator()
        self.subMenu1.add_command(label="Command 4", command=self.doNothing,\
                font=('Helvetica',int(self.fontSize*self.scale)))
        
        self.subMenu2 = tk.Menu(self.menu)
        self.menu.add_cascade(label="Menu 2", menu=self.subMenu2,\
                font=('Helvetica',int(self.fontSize*self.scale)))
        self.subMenu2.add_command(label="Command 1", command=self.doNothing,\
                font=('Helvetica',int(self.fontSize*self.scale)))
        self.subMenu2.add_command(label="Command 2", command=self.doNothing,\
                font=('Helvetica',int(self.fontSize*self.scale)))
        self.subMenu2.add_command(label="Command 3", command=self.doNothing,\
                font=('Helvetica',int(self.fontSize*self.scale)))
        self.subMenu2.add_separator()
        self.subMenu2.add_command(label="Command 4", command=self.doNothing,\
                font=('Helvetica',int(self.fontSize*self.scale)))

    def __createToolBar__(self):
        pass

    def __createStatusBar__(self):
        self.status = tk.Label(self.root, text = " ... Go nuts with the randomizer! ... ",\
                bd = 1, relief=tk.SUNKEN, anchor = tk.W, width = int(self.scale*1920),\
                font=('Helvetica',int(self.fontSize*self.scale)))
        self.status.grid(columnspan=10)

    def __createCardViewerMenu__(self):
        self.OM_var = tk.StringVar(self.root)
        self.OM_var.set(CARDNAMES[0])
        self.OM = apply(tk.OptionMenu, (self.frm, self.OM_var) +\
                tuple(CARDNAMES))
        self.OM.config(bg='white', width=10, font=('Helvetica',\
                int(self.fontSize*self.scale)))
        self.men = self.OM.nametowidget(self.OM.menuname)
        self.men.configure(font=('Helvetica',int(self.fontSize*self.scale)))
        self.OM.grid(row = 1, column = 0)

    def __createTitle__(self):
        self.titleLabel = tk.Label(self.frm, text="DOMINION - Card Randomizer",\
                bg='blue', fg='white', font=('Helvetica',\
                int(self.fontSize*self.scale)))
        self.titleLabel.grid(row=0, columnspan=2, pady = int(self.scale*10))

    def __createExpansionCheckboxes__(self):
        self.Descr = tk.Label(self.frm,\
                text="Check Expansions from which cards will be picked.",\
                bg='blue', fg='white', font=('Helvetica',int(self.fontSize*\
                self.scale)))
        self.Descr.grid(row=3, columnspan=2, pady = int(self.scale*10))
        self.labOpt = tk.Label(self.frm, text="Expansions:", bg='pink',\
                font=('Helvetica',int(self.fontSize*self.scale))).grid(row = 4,\
                column=0, sticky="W")
        self.lab = tk.Label(self.frm, text="Options:", bg='pink',\
                font=('Helvetica',int(self.fontSize*self.scale))).grid(row = 4,\
                column=1, sticky="W")

        self.toggles = []
        nBox = 0
        self.CheckBoxVars = []
        self.MAXROW = 5

        self.image_on = Image.open('./Resources/toggle_on.gif')
        self.image_off = Image.open('./Resources/toggle_off.gif')
        self.toggleWidth = self.image_on.size[0]
        self.toggleHeight = self.image_on.size[1]
        A = 0.25 * self.scale
        self.image_on = self.image_on.resize((int(A*self.toggleWidth),\
                int(A*self.toggleHeight)), Image.ANTIALIAS)
        self.image_off = self.image_off.resize((int(A*self.toggleWidth),\
                int(A*self.toggleHeight)), Image.ANTIALIAS)
        self.photo_on = ImageTk.PhotoImage(self.image_on)
        self.photo_off = ImageTk.PhotoImage(self.image_off)

        self.togglefrm = tk.Frame(self.frm, height=100,width=300,bg="white")
        self.togglefrm.grid(row=5,column =0, sticky="W", pady=int(5*self.scale))

        self.N = 0
        self.toggleLabels = []
        for name in EXPANSION_NAMES_CHR:
            var = tk.IntVar(value=0)
            toggle = tk.Label(self.togglefrm,image=self.photo_off, bg="white",\
                    textvariable=var)
            toggle.image=self.photo_off
            toggle.grid(row = self.N, column=0, sticky="W",\
                    padx=int(5*self.scale))
            toggle.bind("<Button-1>", self.updateToggle) 
            lab = tk.Label(self.togglefrm, text=EXPANSIONS[name].Name,\
                    bg='white', font=('Helvetica',int(self.fontSize*self.scale)),\
                    textvariable=name)
            lab.grid(row = self.N, column=1, sticky="W")
            self.N+=1
            self.toggles.append(toggle)
            self.toggleLabels.append(lab)
            self.CheckBoxVars.append(var)
            self.MAXROW +=1
    
    def __createOptionsCheckboxes__(self):
        self.togglesOptions = []
        nBox = 0
        self.CheckBoxVarsOptions = []

        self.image_on = Image.open('./Resources/toggle_on.gif')
        self.image_off = Image.open('./Resources/toggle_off.gif')
        self.toggleWidth = self.image_on.size[0]
        self.toggleHeight = self.image_on.size[1]
        A = 0.25 * self.scale
        self.image_on = self.image_on.resize((int(A*self.toggleWidth),\
                int(A*self.toggleHeight)), Image.ANTIALIAS)
        self.image_off = self.image_off.resize((int(A*self.toggleWidth),\
                int(A*self.toggleHeight)), Image.ANTIALIAS)
        self.photo_on = ImageTk.PhotoImage(self.image_on)
        self.photo_off = ImageTk.PhotoImage(self.image_off)

        self.togglefrmOptions = tk.Frame(self.frm, height=100,width=300,bg="white")
        self.togglefrmOptions.grid(row=5,column = 1, sticky="NW", pady=int(5*self.scale))

        self.N = 0
        self.toggleLabelsOptions = []
        self.Options = ['Curve', 'High Interaction', 'Suggested Sets']
        for name in self.Options:
            var = tk.IntVar(value=0)
            toggle = tk.Label(self.togglefrmOptions,image=self.photo_off, bg="white",\
                    textvariable=var)
            toggle.image=self.photo_off
            toggle.grid(row = self.N, column=0, sticky="W",\
                    padx=int(5*self.scale))
            toggle.bind("<Button-1>", self.updateToggle) 
            lab = tk.Label(self.togglefrmOptions, text=name,\
                    bg='white', font=('Helvetica',int(self.fontSize*self.scale)),\
                    textvariable=name)
            lab.grid(row = self.N, column=1, sticky="W")
            self.N+=1
            self.togglesOptions.append(toggle)
            self.toggleLabelsOptions.append(lab)
            self.CheckBoxVarsOptions.append(var)

    def __createCardViewerButton__(self):
        self.button = tk.Button(self.frm, text='Update Preview',\
                command=self.updateCardPreview, font=('Helvetica',\
                int(self.fontSize*self.scale)))
        self.button.grid(row=1, column = 1)

    def __createDrawSampleButton__(self):
        self.button2 = tk.Button(self.frm, text='Draw Sample',\
                command=self.drawSample, font=('Helvetica',\
                int(self.fontSize*self.scale)))
        self.button2.grid(row=self.MAXROW+1, columnspan = 2)

    def _close(self,event):
        self.root.withdraw()
        sys.exit()
        
    def _on_mousewheel_up(self, event):
        self.cnv.yview_scroll(-2,"units")
         
    def _on_mousewheel_down(self, event):
        self.cnv.yview_scroll(2,"units")

    def _on_mousewheel(self, event):
        self.cnv.yview_scroll(-1*(event.delta/120),"units")

    def _scroll_start(self, event):
        self.cnv.scan_mark(event.x, event.y)
        
    def _scroll_move(self, event):
        self.cnv.config(cursor="fleur")
        self.cnv.scan_dragto(event.x, event.y, gain=1)

    def _reset_cursor(self, event):
        self.cnv.config(cursor="arrow")

    def drawSample(self):
        counter = 0
        self.ExpansionsSelected = []
        self.CardPool = []
        self.CardSelection = []
        for label in self.toggles:
            if label.cget("textvariable") == 1:
                self.ExpansionsSelected.append(counter)
            counter +=1
        for i in self.ExpansionsSelected:
            name = self.toggleLabels[i].cget("text")
            for c in CARDS:
                if CARDS[c].expansion == name:
                    self.CardPool.append(c)

        # Use options information 
        counter = 0
        self.OptionsSelected = []
        for label in self.togglesOptions:
            if label.cget("textvariable") == 1:
                self.OptionsSelected.append(self.Options[counter])
            counter +=1
        # Apply options to the CardPool
        self.applyOptions()



        # CardPool now contains the dictionary names of the selected cards. 
        # To get more information about the cards you need to use CARDS[name]._attribute_.
        #for i in range(0,10):
        #    self.CardSelection.append(self.CardPool[i])
        # Now that a card pool has been selected, I need to make a selection of 10 cards.
        # ... 
        chosenIndecies = []
        # While less than 10 cards have been found select a random one from the card
        # pool and make sure it hasn't been selected before.
        while len(self.CardSelection) < 10:
            Rnum = rd.randint(0,len(self.CardPool)-1)
            indexFound = False
            if len(chosenIndecies) == 0:
                indexFound = True
            else:
                indexFound = True
                for i in chosenIndecies:
                    if Rnum == i:
                        indexFound = False
            if indexFound:
                chosenIndecies.append(Rnum)
                self.CardSelection.append(self.CardPool[Rnum])

        # Now let's sort the selection according to cost and name
        CARDS_selected = []
        for name in self.CardSelection:
            CARDS_selected.append((CARDS[name], name))
        CARDS_selected = sorted(sorted(CARDS_selected, key=lambda c: c[0].name),\
                key = lambda c: c[0].cost)
        newSelec = []
        for c in CARDS_selected:
            newSelec.append(c[1])
        self.CardSelection = newSelec

        # Once this selection has been made I should show the picture of the selected cards.
        self.displaySelection()

    def applyOptions(self):
        for option in self.OptionsSelected:
            if option == 'Curve':
                costsAvailable = []
                for name in self.CardPool:
                    if len(costsAvailable) == 0:
                        costsAvailable.append(CARDS[name].cost)
                    else:
                        add = True
                        for cost in costsAvailable:
                            if CARDS[name].cost == cost:
                                add = False
                        if add:
                            costsAvailable.append(CARDS[name].cost)
                costsAvailable.sort()
                # numpy.random.choice(numpy.arange(1,7), p=[0.1,0.05,0.05,0.2,0.4,0.2])
                
                #determine probabilites
                #p = []
                #for i in costsAvailable:
                #    p.append(self.gauss(i,mu,sigma))
            if option == 'High Interaction':
                print(option)
            if option == 'Suggested Sets':
                print(option)

    def gauss(self,i,mu,sigma):
        pass
    
    def displaySelection(self):
        imageList = []
        scale = self.imageScale*self.scale
        # This should display cards in ascending order of cost and in alphabetical order.

        for name in self.CardSelection:
            image = Image.open(CARDS[name].imagePath)
            imageWidth = image.size[0]
            imageHeight = image.size[1]
            image = image.resize((int(scale*imageWidth),int(scale*imageHeight)),\
                Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            lab = tk.Label(self.displayfrm, image = photo)
            lab.image = photo
            imageList.append(lab)
        
        for i in range(0,5):
            imageList[i].grid(row = 2, column = i, columnspan = 1,\
                    padx=int(self.scale*15),pady=int(self.scale*5))
            imageList[i+5].grid(row = 3, column = i, columnspan = 1,\
                    padx=int(self.scale*15),pady=int(self.scale*5))
        
    def drawOnePic(self, name, nlabel = 0, scale = 1):
        picName = ''
        for n in CARDS:
            if CARDS[n].name == name:
                picName = n
        image = Image.open(CARDS[picName].imagePath)
        imageWidth = image.size[0]
        imageHeight = image.size[1]
        image = image.resize((int(scale*imageWidth),int(scale*imageHeight)),\
                Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(self.frm, image=photo)
        label.image = photo
        if len(self.labels) == 0:
            label.grid(row = 2, column = 0, columnspan = 2,\
                    padx=int(self.scale*15),pady=int(self.scale*5))
            self.labels.append(label)
        else:
            self.labels[nlabel].configure(image = photo)

    def updateCardPreview(self):
        self.drawOnePic(self.OM_var.get(), 0, self.scale*self.imageScale)
        self.frm.update_idletasks()
        self.cnv.configure(scrollregion=(0,0,self.frm.winfo_width(),\
                self.frm.winfo_height()))
    
    def updateToggle(self, event):
        l = event.widget
        if l.cget("textvariable") == 1:
            l.configure(image=self.photo_off)
            l.configure(textvariable = 0) 
        else:
            l.configure(image=self.photo_on)
            l.configure(textvariable = 1) 

    def run(self):
        #----- Resize window ----- #-
        self.frm.update_idletasks()
        self.displayfrm.update_idletasks()
        self.cnv.configure(scrollregion=(0,0,self.frm.winfo_width(),\
                self.frm.winfo_height()))
        self.root.mainloop()

if __name__=='__main__':
    Dominion().run()
