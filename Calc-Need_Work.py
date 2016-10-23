import sys 
from tkinter import * 


class Gui:   
    def __init__(self, root):
        
        self.num = 0
        self.holdNum = 0
        self.op = 0
        self.add = 0
        self.dec = 0
        self.count = 1
        self.oper = 0
        self.second = False
        self.clear = False
        
        self.root = root 

        self.label = Label(self.root, text = 0)
        self.label.pack(fill=BOTH, expand=True)

        self.frame = Frame(self.root, borderwidth = 10, relief = GROOVE)
        self.frame.pack(fill = BOTH, expand = True)

        self.button1 = Button(self.frame, text='1', command = lambda a = 1 : self.button_press(a)) 
        self.button2 = Button(self.frame, text='2', command = lambda a = 2 : self.button_press(a)) 
        self.button3 = Button(self.frame, text='3', command = lambda a = 3 : self.button_press(a)) 

        self.button1.pack(side = LEFT, fill= BOTH, expand = True)
        self.button2.pack(side = LEFT, fill= BOTH, expand = True) 
        self.button3.pack(side = LEFT, expand = True, fill= BOTH) 

        self.frame2 = Frame(self.root, borderwidth = 10, relief = GROOVE)
        self.frame2.pack(fill = BOTH, expand = True)

        self.button4 = Button(self.frame2, text='4', command = lambda a = 4 : self.button_press(a))
        self.button5 = Button(self.frame2, text='5', command = lambda a = 5 : self.button_press(a)) 
        self.button6 = Button(self.frame2, text='6', command = lambda a = 6 : self.button_press(a))
        
        self.button4.pack(side = LEFT, fill= BOTH, expand = True)
        self.button5.pack(side = LEFT, fill= BOTH, expand = True)
        self.button6.pack(side = LEFT, fill= BOTH, expand = True)

        self.frame3 = Frame(self.root, borderwidth = 10, relief = GROOVE)
        self.frame3.pack(fill = BOTH, expand = True)

        self.button7 = Button(self.frame3, text='7', command = lambda a = 7 : self.button_press(a))
        self.button8 = Button(self.frame3, text='8', command = lambda a = 8 : self.button_press(a)) 
        self.button9 = Button(self.frame3, text='9', command = lambda a = 9 : self.button_press(a))
        
        self.button7.pack(side = LEFT, fill= BOTH, expand = True)
        self.button8.pack(side = LEFT, fill= BOTH, expand = True)
        self.button9.pack(side = LEFT, fill= BOTH, expand = True)

        self.frame4 = Frame(self.root, borderwidth = 10, relief = GROOVE)
        self.frame4.pack(fill = BOTH, expand = True)
        
        self.button0 = Button(self.frame4, text='0', command = lambda a = 0 : self.button_press(a))
        self.button10 = Button(self.frame4, text='+', command = lambda a = '+' : self.button_press(a)) 
        self.button11 = Button(self.frame4, text='-', command = lambda a = '-' : self.button_press(a))
        
        self.button0.pack(side = LEFT, fill= BOTH, expand = True)
        self.button10.pack(side = LEFT, fill= BOTH, expand = True)
        self.button11.pack(side = LEFT, fill= BOTH, expand = True)

        self.frame5 = Frame(self.root, borderwidth = 10, relief = GROOVE)
        self.frame5.pack(fill = BOTH, expand = True)
        
        self.button12 = Button(self.frame5, text='x', command = lambda a = 'X' : self.button_press(a))
        self.button13 = Button(self.frame5, text='/', command = lambda a = '/' : self.button_press(a)) 
        self.button14 = Button(self.frame5, text='=', command = lambda a = '=' : self.button_press(a))
        
        self.button12.pack(side = LEFT, fill= BOTH, expand = True)
        self.button13.pack(side = LEFT, fill= BOTH, expand = True)
        self.button14.pack(side = LEFT, fill= BOTH, expand = True)

        self.frame6 = Frame(self.root, borderwidth = 10, relief = GROOVE)
        self.frame6.pack(fill = BOTH, expand = True)
        
        self.button15 = Button(self.frame6, text='.', command = lambda a = '.' : self.button_press(a))
        self.button16 = Button(self.frame6, text='CL', command = lambda a = 'CL' : self.button_press(a)) 
        self.button17 = Button(self.frame6, text='', command = lambda a = '' : self.button_press(a))
        
        self.button15.pack(side = LEFT, fill= BOTH, expand = True)
        self.button16.pack(side = LEFT, fill= BOTH, expand = True)
        self.button17.pack(side = LEFT, fill= BOTH, expand = True)

    def reseting(self, clear):
        print ("Reseting")
        self.label.config(text = str(self.add))
        self.num = 0
        self.holdNum = 0
        if clear == True:
            self.add = 0
            self.oper = 0
            print("Reset oper" + str(self.oper))
            self.count = 1
        self.op = 0
        self.dec = 0
        self.second = False
        
    def makeDecimal(self, num1, num2):
        num3 = num2/10
        return(num1 + num3)

    def getNumber(self, val):
        print("Step 1 I have: " + str(val))
        self.num = val
##        print("Value is: " + str(val))
##        print ("Getting Number")
        print ("Count is set at: " + str(self.count))

        if self.count == 1:
            self.oper = val
            print ("Operator is set at: " + str(self.oper))
            self.count += 1
        elif self.count > 1:
            self.oper = self.holdNum * 10 + self.num
            print ("Operator is set at: " + str(self.oper))
            self.count += 1
                    
                
        print("Getting First Number: " + str(self.oper))
        

    def button_press(self, val):
        self.label.config(text = str(val))

        string = "Test"        
        #print(self.holdNum)

        if val == "CL":
            print("Clearing")
            clear = True
            self.reseting(clear)

        #teller = val != '+' and val != '-' and val != '=' and val != 'X' and val != '/' and val != '.' and self.second == False and val != "CL"
        #print(teller)

        #operander = val == '+' or val == '-' or val == 'X' or val == '/' or val == '.'

        if val != '+' and val != '-' and val != '=' and val != 'X' and val != '/' and val != '.' and self.second == False and val != "CL":
            self.getNumber(val)

        if self.op == '.':
                print ("Decimalisation")
                self.holdNum = self.num
                print ("Holding is set at: " + str(self.holdNum))
                self.dec = val
                print ("Decimal is set at: " + str(self.dec))
                self.num = self.makeDecimal(self.holdNum, self.dec)
                print(str(self.num))
                self.add = self.num
                self.label.config(text = self.add)
                if self.op != '=':
                    self.holdNum = self.add
                    print ("Holding is set at: " + str(self.holdNum))
                    self.op = 0
                    
                    
        if self.op == '+':
            print("Adding")
            self.num = val
            if type(val) != type(string):
                self.getNumber(val)
            elif val == '=' :
                print("Adding this number: " + str(self.oper))
                self.add = self.oper + self.holdNum
                print("Combined they make " + str(self.add))
                self.label.config(text = str(self.add))
                self.holdNum = self.add
                print ("Holding is set at: " + str(self.holdNum))
                self.op = 0
                clear = False
                self.reseting(clear)
                    
        elif self.op == '-':
            print("Subtracting")
            self.num = val
            print("Subtracting this number: " + str(self.num))
            self.add = self.holdNum - self.num
            print("Combined they make " + str(self.add))
            self.label.config(text = str(self.add))
            if self.op != '=':
                self.holdNum = self.add
                print ("Holding is set at: " + str(self.holdNum))
                self.op = 0
                
        elif self.op == 'X':
            print("Multiplyng")
            self.num = val
            print("Multing this number: " + str(self.num))
            self.add = self.num * self.holdNum
            print("Combined they make " + str(self.add))
            self.label.config(text = str(self.add))
            if self.op != '=':
                self.holdNum = self.add
                print ("Holding is set at: " + str(self.holdNum))
                self.op = 0

        elif self.op == '/':
            print("Dividing")
            self.num = val
            print("Dividing this number: " + str(self.num))
            self.add = self.holdNum / self.num
            print("Combined they make " + str(self.add))
            self.label.config(text = str(self.add))
            if self.op != '=':
                self.holdNum = self.add
                print ("Holding is set at: " + str(self.holdNum))
                self.op = 0

        else:   
            if val == '+' or val == '-' or val == 'X' or val == '/' or val == '.':
                print('I have operand: ' + val)
                if self.add == 0:
                    print("We do not have a previous answer")
                    self.holdNum = self.oper
                else:
                    print("Previous answer is: " + str(self.add))
                    self.holdNum = self.add
                    print ("Holder is set at: " + str(self.oper))
                #self.oper = self.holdNum
                self.count = 1
                self.op = val
                self.second = True
                print ("Holder is set at: " + str(self.holdNum))

        

def main(): 
    root = Tk() 
    # set the starting size of the window 
    root.geometry('%dx%d' % (290,350))
    gui = Gui(root) 
    root.mainloop() 


if __name__ == '__main__': 
    sys.exit(main()) 
