 #!/opt/local/bin/python

import tkinter as tk
import tkinter.ttk as ttk
import time
import sys
from random import randint

import threading

globstop = 0

class MyTimer:
    global globstop

    def __init__(self, tempo, target, args= [], kwargs={}):
        self._target = target
        self._args = args
        self._kwargs = kwargs
        self._tempo = tempo

    def _run(self):
        if globstop :
            self.exit()
        self._timer = threading.Timer(self._tempo, self._run)
        self._timer.start()
        self._target(*self._args, **self._kwargs)

    def start(self):
        
        self._timer = threading.Timer(self._tempo, self._run)
        self._timer.start()
    
    def stop(self):
        self._timer.cancel()


class Lift:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.master.title('ascenseur')


        self.CreerEtage()
        self.CreerElevator()

        self.buttonA = tk.Button(self.frame, text = 'Alarm')
        self.buttonA.pack()

        self.button5 = tk.Button(self.frame, text = '5',command=self.Aller5)
        self.button5.pack()
        self.button4 = tk.Button(self.frame, text = '4',command=self.Aller4)
        self.button4.pack()
        self.button3 = tk.Button(self.frame, text = '3',command=self.Aller3)
        self.button3.pack()
        self.button2 = tk.Button(self.frame, text = '2',command=self.Aller2)
        self.button2.pack()
        self.button1 = tk.Button(self.frame, text = '1',command=self.Aller1)
        self.button1.pack()

        self.frame.pack()

        self.CurEtage=1
        self.curMouvement='0'
        self.target=[0,0,0,0,0]
        self.CurPos=0
        self.CurServed=0
        self.CurTempo=0

    def Aller5(self):
        if self.CurPos < 5 :
            self.target[self.CurPos]=5
            self.CurPos = self.CurPos+1
            if self.CurPos==5:
                self.CurPos=0

    def Aller4(self):
        if self.CurPos < 5 :
            self.target[self.CurPos]=4
            self.CurPos = self.CurPos+1
            if self.CurPos==5:
                self.CurPos=0

    def Aller3(self):
        if self.CurPos < 5 :
            self.target[self.CurPos]=3
            self.CurPos = self.CurPos+1
            if self.CurPos==5:
                self.CurPos=0

    def Aller2(self):
        if self.CurPos < 5 :
            self.target[self.CurPos]=2
            self.CurPos = self.CurPos+1
            if self.CurPos==5:
                self.CurPos=0

    def Aller1(self):
        if self.CurPos < 5 :
            self.target[self.CurPos]=1
            self.CurPos = self.CurPos+1
            if self.CurPos==5:
                self.CurPos=0



    def CreerEtage(self):
        self.newWindow = tk.Toplevel(self.master)
        self.Etages = Etages(self.newWindow,self)

    def CreerElevator(self):

        self.newWindow = tk.Toplevel(self.master)
        self.Elevator = Elevator(self.newWindow)

    def move(self):
        if self.CurEtage > 5:
            self.CurEtage=5
            self.curMouvement='0'
        if self.CurEtage < 1:
            self.CurEtage=1
            self.curMouvement='0'

        if self.curMouvement == '+' or self.curMouvement=='-' or self.curMouvement== 'p':
            self.CurTempo=self.CurTempo+1
        if self.CurTempo == 50 or self.CurTempo==0:
            
            if self.curMouvement=='p':
                self.curMouvement='0'
            

            if self.curMouvement=='+':
                self.CurEtage=self.CurEtage+1
                if self.CurEtage==self.target[self.CurServed]:
                    self.curMouvement='p'
                    self.target[self.CurServed]=0
                    self.CurServed=self.CurServed+1
                    if self.CurServed==5:
                        self.CurServed=0
                        self.target[self.CurPos]=randint(0,5)
            if self.curMouvement=='-':
                self.CurEtage=self.CurEtage-1
                if self.CurEtage==self.target[self.CurServed]:
                    self.curMouvement='p'
                    self.target[self.CurServed]=0
                    self.CurServed=self.CurServed+1
                    if self.CurServed==5:
                        self.CurServed=0
                        self.target[self.CurServed]=randint(0,5)

            self.UpdateColor()
            self.CurTempo=0


        if self.curMouvement=='0':
            if self.target[self.CurServed]>0:
                if self.CurEtage < self.target[self.CurServed]:
                    self.curMouvement='+'
                    self.UpdateColor()
                if self.CurEtage >self.target[self.CurServed]:
                    self.curMouvement='-'
                    self.UpdateColor()
                if self.target[self.CurServed]==self.CurEtage:
                    if self.CurServed==4:
                        self.CurServed=0
                    else:
                        self.CurServed=self.CurServed+1
    
                        
    def UpdateColor(self):
#        print "UpdateColor", self.curMouvement, self.CurEtage
        if self.curMouvement=='0':
            if self.CurEtage == 1:
                self.Elevator.Rouge1()
                self.Elevator.Noir2()
                self.Elevator.Noir3()
                self.Elevator.Noir4()
                self.Elevator.Noir5()
            if self.CurEtage == 2:
                self.Elevator.Noir1()
                self.Elevator.Rouge2()
                self.Elevator.Noir3()
                self.Elevator.Noir4()
                self.Elevator.Noir5()
            if self.CurEtage == 3:
                self.Elevator.Noir1()
                self.Elevator.Noir2()
                self.Elevator.Rouge3()
                self.Elevator.Noir4()
                self.Elevator.Noir5()
            if self.CurEtage == 4:
                self.Elevator.Noir1()
                self.Elevator.Noir2()
                self.Elevator.Noir3()
                self.Elevator.Rouge4()
                self.Elevator.Noir5()
            if self.CurEtage == 5:
                self.Elevator.Noir1()
                self.Elevator.Noir2()
                self.Elevator.Noir3()
                self.Elevator.Noir4()
                self.Elevator.Rouge5()

        if self.curMouvement=='p':
            if self.CurEtage == 1:
                self.Elevator.Vert1()
                self.Elevator.Noir2()
                self.Elevator.Noir3()
                self.Elevator.Noir4()
                self.Elevator.Noir5()
            if self.CurEtage == 2:
                self.Elevator.Noir1()
                self.Elevator.Vert2()
                self.Elevator.Noir3()
                self.Elevator.Noir4()
                self.Elevator.Noir5()
            if self.CurEtage == 3:
                self.Elevator.Noir1()
                self.Elevator.Noir2()
                self.Elevator.Vert3()
                self.Elevator.Noir4()
                self.Elevator.Noir5()
            if self.CurEtage == 4:
                self.Elevator.Noir1()
                self.Elevator.Noir2()
                self.Elevator.Noir3()
                self.Elevator.Vert4()
                self.Elevator.Noir5()
            if self.CurEtage == 5:
                self.Elevator.Noir1()
                self.Elevator.Noir2()
                self.Elevator.Noir3()
                self.Elevator.Noir4()
                self.Elevator.Vert5()


        if self.curMouvement=='+':
            if self.CurEtage == 1:
                self.Elevator.Orange1()
                self.Elevator.Bleu2()
                self.Elevator.Noir3()
                self.Elevator.Noir4()
                self.Elevator.Noir5()
            if self.CurEtage == 2:
                self.Elevator.Noir1()
                self.Elevator.Orange2()
                self.Elevator.Bleu3()
                self.Elevator.Noir4()
                self.Elevator.Noir5()
            if self.CurEtage == 3:
                self.Elevator.Noir1()
                self.Elevator.Noir2()
                self.Elevator.Orange3()
                self.Elevator.Bleu4()
                self.Elevator.Noir5()
            if self.CurEtage == 4:
                self.Elevator.Noir1()
                self.Elevator.Noir2()
                self.Elevator.Noir3()
                self.Elevator.Orange4()
                self.Elevator.Bleu5()


        if self.curMouvement=='-':
            if self.CurEtage == 2:
                self.Elevator.Bleu1()
                self.Elevator.Orange2()
                self.Elevator.Noir3()
                self.Elevator.Noir4()
                self.Elevator.Noir5()
            if self.CurEtage == 3:
                self.Elevator.Noir1()
                self.Elevator.Bleu2()
                self.Elevator.Orange3()
                self.Elevator.Noir4()
                self.Elevator.Noir5()
            if self.CurEtage == 4:
                self.Elevator.Noir1()
                self.Elevator.Noir2()
                self.Elevator.Bleu3()
                self.Elevator.Orange4()
                self.Elevator.Noir5()
            if self.CurEtage == 5:
                self.Elevator.Noir1()
                self.Elevator.Noir2()
                self.Elevator.Noir3()
                self.Elevator.Bleu4()
                self.Elevator.Orange5()

    def sortir(self):
        global globstop
        globstop = 1
        sys.exit(1)


class Etages(Lift):
    def __init__(self, master,Lift):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.master.title('Etages')

        self.button5u=tk.Button(self.frame,text='5 ^',command=Lift.Aller5)
        self.button5u.pack()
        self.button5d=tk.Button(self.frame,text='5 v',command=Lift.Aller5)
        self.button5d.pack()

        self.button4u=tk.Button(self.frame,text='4 ^',command=Lift.Aller4)
        self.button4u.pack()
        self.button4d=tk.Button(self.frame,text='4 v',command=Lift.Aller4)
        self.button4d.pack()

        self.button3u=tk.Button(self.frame,text='3 ^',command=Lift.Aller3)
        self.button3u.pack()
        self.button3d=tk.Button(self.frame,text='3 v',command=Lift.Aller3)
        self.button3d.pack()

        self.button2u=tk.Button(self.frame,text='2 ^',command=Lift.Aller2)
        self.button2u.pack()
        self.button2d=tk.Button(self.frame,text='2 v',command=Lift.Aller2)
        self.button2d.pack()

        self.button1u=tk.Button(self.frame,text='1 ^',command=Lift.Aller1)
        self.button1u.pack()
        self.button1d=tk.Button(self.frame,text='1 v',command=Lift.Aller1)
        self.button1d.pack()


        self.master.geometry("+200+200")

        self.frame.pack()

    def close_windows(self):
        self.master.destroy()

class Elevator:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)

        self.master.title('Position')

        style=ttk.Style()
        style.configure("TButton",padding=(0,5,0,5)) 

        style.configure("Red.TButton",foreground='red')
        style.configure("Blue.TButton",foreground='blue')
        style.configure("Green.TButton",foreground='green')
        style.configure("Orange.TButton",foreground='orange')
        style.configure("Black.Tbutton",foreground='black')


        self.button5 = ttk.Button(self.frame, text = '#_5_#')
        self.button5.configure(style="Red.TButton")
        self.button5.pack()

        self.button4 = ttk.Button(self.frame, text = '#_4_#')
        self.button4.configure(style="Blue.TButton")
        self.button4.pack()
 
        self.button3 = ttk.Button(self.frame, text = '#_3_#')
        self.button3.configure(style="Green.TButton") 
        self.button3.pack()

        self.button2 = ttk.Button(self.frame, text = '#_2_#')
        self.button2.pack()
        self.button2.configure(style="Orange.TButton")

        self.button1 = ttk.Button(self.frame, text = '#_1_#')
        self.button1.configure(style="Black.TButton")
        self.button1.pack()

        self.master.geometry("+400+200")

        self.frame.pack()

    def Rouge5(self):

        self.button5.configure(style="Red.TButton")
        self.button5.pack()

    def Bleu5(self):
    
        self.button5.configure(style="Blue.TButton")
        self.button5.pack()
    
    def Vert5(self):
        
        self.button5.configure(style="Green.TButton")
        self.button5.pack()

    def Orange5(self):
        
        self.button5.configure(style="Orange.TButton")
        self.button5.pack()
    
    def Noir5(self):
        
        self.button5.configure(style="Black.TButton")
        self.button5.pack()


    def Rouge4(self):
    
        self.button4.configure(style="Red.TButton")
        self.button4.pack()

    def Bleu4(self):
    
        self.button4.configure(style="Blue.TButton")
        self.button4.pack()

    def Vert4(self):
    
        self.button4.configure(style="Green.TButton")
        self.button4.pack()

    def Orange4(self):
    
        self.button4.configure(style="Orange.TButton")
        self.button4.pack()

    def Noir4(self):
    
        self.button4.configure(style="Black.TButton")
        self.button4.pack()


    def Rouge3(self):
    
        self.button3.configure(style="Red.TButton")
        self.button3.pack()

    def Bleu3(self):
    
        self.button3.configure(style="Blue.TButton")
        self.button3.pack()

    def Vert3(self):
    
        self.button3.configure(style="Green.TButton")
        self.button3.pack()

    def Orange3(self):
    
        self.button3.configure(style="Orange.TButton")
        self.button3.pack()

    def Noir3(self):
    
        self.button3.configure(style="Black.TButton")
        self.button3.pack()


    def Rouge2(self):
    
        self.button2.configure(style="Red.TButton")
        self.button2.pack()

    def Bleu2(self):
    
        self.button2.configure(style="Blue.TButton")
        self.button2.pack()

    def Vert2(self):
    
        self.button2.configure(style="Green.TButton")
        self.button2.pack()

    def Orange2(self):
    
        self.button2.configure(style="Orange.TButton")
        self.button2.pack()

    def Noir2(self):
    
        self.button2.configure(style="Black.TButton")
        self.button2.pack()

    def Rouge1(self):
        
    
        self.button1.configure(style="Red.TButton")
        self.button1.pack()

    def Bleu1(self):
    
        self.button1.configure(style="Blue.TButton")
        self.button1.pack()

    def Vert1(self):
    
        self.button1.configure(style="Green.TButton")
        self.button1.pack()

    def Orange1(self):
    
        self.button1.configure(style="Orange.TButton")
        self.button1.pack()

    def Noir1(self):
    
        self.button1.configure(style="Black.TButton")
        self.button1.pack()

class Portes_défaillantes(Lift,Etages):
    



def main(): 
    root = tk.Tk()
    app = Lift(root)
    root.protocol("WM_DELETE_WINDOW", app.sortir)
    Cron=MyTimer(0.02,app.move)
    Cron.start()
    root.mainloop()

if __name__ == '__main__':
    main()
