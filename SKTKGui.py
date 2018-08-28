'''
Created on Aug 15, 2018

@author: cody.west
'''
from tkinter import *
from SKPkg.ClientSide import ClientSide
from SKPkg.MusicSide import MusicSide
import threading



class SKTKGui(object):
    '''
    classdocs
    '''
 
    def data(self):
        for i in range(50):
            Label(self.frame,text=i).grid(row=i,column=0)
            Label(self.frame,text="my text |"+str(i)).grid(row=i,column=1)
            Label(self.frame,text="..........").grid(row=i,column=2)
            
    #Main play button currently runs this, getting the file list from the running server
    def populateLabels(self):
        self.CS.commSwitch2('ls')
        self.labelArr = self.CS.getDirHolder()
        i = 0
        for x in self.labelArr:
            Label(self.frame,text=str(i)).grid(row=i,column=0)
            Label(self.frame,text=' ' + x).grid(row=i,column=1) 
            Button(self.frame,text='Play',command=lambda num=i: self.musicThreadCall(num)).grid(row=i,column=2)
            #command=lambda num=i: showNumber(num)
            i+=1
            if(i==len(self.labelArr)-1):
                break
        

    def myfunction(self,event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=750,height=450)
        
#         Untested playing music on a thread
    def musicThreadCall(self,pos):
        threading.Thread(target = self.musicDL, args = ([pos])).start()
        #threading.Thread(target = self.clientHandler2, args = (CS, CS_Addr)).start()

  
    def musicDL(self,pos):
        path = self.labelArr[pos]
        caller = self.CS.commSwitch2(path)
        self.MS.playSound("C:\\SoundFiles\\Client\\" + path)
    
    #Method grabs the file from the server and on success will play the music    
    def MusicCall(self,pos):
        print('grabbing id')
        path = self.labelArr[pos]
        print(path)
        caller = self.CS.commSwitch2(path)
        if(caller==1):
            self.MS.playSound("C:\\SoundFiles\\Client\\" + path)
        else:
            print("Error With File")
        
    def __init__(self, master):
        self.CS = ClientSide('127.0.0.1',1445)
        #self.CS.connecter()

        
        self.MS = MusicSide()
        #self.master = master
        master.title("This is only a test")

        self.labelArr = {}
        sizex = 800
        sizey = 600
        posx  = 100
        posy  = 100
        master.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

        myframe=Frame(master,relief=GROOVE,width=50,height=100,bd=1)
        myframe.place(x=10,y=10)
        
        #Buttons and Button Frame
        butFrame = Frame(master,relief=GROOVE,width=750,height=90,bd=1)
        butFrame.place(x=10,y=480)
        
        playBut = Button(butFrame, text = "Play&Pause",fg='blue', height=3,command=self.populateLabels)#,height=3,width=10)
        playBut.place(in_=butFrame,anchor='c', relx=.5, rely=.5)
        nextBut = Button(butFrame, text = "Forward",fg='blue',height=3,width=10)
        nextBut.place(in_=butFrame,anchor='c', relx=.37, rely=.5)
        pastBut = Button(butFrame, text = "Reverse",fg='blue',height=3,width=10)
        pastBut.place(in_=butFrame,anchor='c', relx=.63, rely=.5)
        
#         playBut = Button(butFrame, text = "Play&Pause",fg='blue',height=3,width=10)
#         playBut.place(x=375,y=5)
#         nextBut = Button(butFrame, text = "Forward",fg='blue',height=3,width=10)
#         nextBut.place(x=275,y=5)
#         pastBut = Button(butFrame, text = "Reverse",fg='blue',height=3,width=10)
#         pastBut.place(x=475,y=5)

#         playBut = Button(butFrame, text = "Play&Pause",fg='blue')#,height=3,width=10)
#         playBut.pack(fill=X)
#         nextBut = Button(butFrame, text = "Forward",fg='blue')#,height=3,width=10)
#         nextBut.pack(fill=X)
#         pastBut = Button(butFrame, text = "Reverse",fg='blue')#,height=3,width=10)
#         pastBut.pack(fill=X)

#         playBut = Button(butFrame, text = "Play&Pause",fg='blue', relief=RIDGE)#,height=3,width=10)
#         playBut.grid(row=0,column=0)
#         nextBut = Button(butFrame, text = "Forward",fg='blue', relief=RIDGE)#,height=3,width=10)
#         nextBut.grid(row=0,column=1)
#         pastBut = Button(butFrame, text = "Reverse",fg='blue', relief=RIDGE)#,height=3,width=10)
#         pastBut.grid(row=0,column=2)






        #More Canvas Shit I don't Get
        self.canvas=Canvas(myframe)
        self.frame=Frame(self.canvas)
        myscrollbar=Scrollbar(myframe,orient="vertical",command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=myscrollbar.set)
        self.buttonArr = {}
        
        myscrollbar.pack(side="right",fill="y")
        self.canvas.pack(side="left")
        self.canvas.create_window((0,0),window=self.frame,anchor='nw')
        self.frame.bind("<Configure>",self.myfunction)
        #self.data()

        #self.populateLabel(self)

#         self.total_label_text = IntVar()
#         self.total_label_text.set(self.total)
#         self.total_label = Label(master, textvariable=self.total_label_text)

#         self.label = Label(master, text="Total:")
# 
#         vcmd = master.register(self.validate) # we have to wrap the command
#         self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

#        Using Lambdas to get around tkinters limited paramater abilities.
#         self.add_button = Button(master, text="+", command=lambda: self.update("add"))
#         self.subtract_button = Button(master, text="-", command=lambda: self.update("subtract"))
#         self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))

        # LAYOUT

#         self.label.grid(row=0, column=0, sticky=W)
#         self.total_label.grid(row=0, column=1, columnspan=2, sticky=E)
# 
#         self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)
# 
#         self.add_button.grid(row=2, column=0)
#         self.subtract_button.grid(row=2, column=1)
#         self.reset_button.grid(row=2, column=2, sticky=W+E)

        

    #def populateLabel(self):
            


        
if __name__ == "__main__":
    root = Tk()
    my_gui = SKTKGui(root)
    root.mainloop()
