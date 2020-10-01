from Tkinter import *
from tkMessageBox import *

counter=0
num=0
x=00
y=00
cntr=0

#**********************************************************************************************************************************************************************
#ajsncsvnfdkbndfnbdfnb
def result():
    root=Tk()
    root.attributes('-fullscreen',True)
    shortcutbar = Frame(root, height=30, bg='light blue')
    toolbar = Label(shortcutbar, text='Quiz Test',bg='black',fg='white',height=2,font='CalibriLight 12 bold')
    toolbar.pack(side=TOP,fill=X,expand=YES)
    shortcutbar.pack(expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root, text='\n\n\n\n\n\n\nYour score is',fg='black',font='Times 22').pack(side=TOP,anchor=CENTER)
    Label(root, text='\n'+str(num),fg='black',font='Times 24 bold').pack(side=TOP,anchor=CENTER)
    def counter_label(label):
        def count():
            global cntr
            cntr= cntr+1
            label.after(1000,count)

            if cntr==5:
                root.destroy()
            
        count()
    label=Label(root,fg='red',font='Arial 18 bold')
    label.pack(side=TOP,anchor=NE)
    counter_label(label)

    
#**********************************************************************************************************************************************************************
#**********************************************************************************************************************************************************************
def ques5odd():
    global count
    root=Tk()
    root.attributes('-fullscreen',True)
    v=IntVar()
    def m():
        if(v.get()==2):
            global num
            num=num+2
            
        else:
            num
    shortcutbar = Frame(root, height=30, bg='light blue')
    toolbar = Label(shortcutbar, text='Quiz Test',bg='black',fg='white',height=2,font='CalibriLight 12 bold')
    toolbar.pack(side=TOP,fill=X,expand=YES)
    shortcutbar.pack(expand=NO, fill=X)
        
    def counter_label(label):
        def count():
            global counter
            counter= counter+1
            if counter>59:
                global x
                x=x+counter/60
                counter=counter/60
                if x>59:
                    global y
                    y=y+x/60
                    x=x/60
            global t
            t=str(y)+':'+str(x)+':'+str(counter)
            label.config(text=str(t))
            label.after(1000,count)

            if x==5:
                root.destroy()
                result()
        count()
    label=Label(root,fg='red',font='Arial 18 bold')
    label.pack(side=TOP,anchor=NE)
    counter_label(label)
    
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root, text = 'Q5. Which of the following results in a SyntaxError(Multiple answers possible) ?',fg='black',font='Times 19').pack(side=TOP,expand=NO,anchor=NW)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' "Once upon a time...",she said.',padx=20,variable=v,value=1,font='Times 16',command=m).pack(anchor=W)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' "He said,"Yes!""',padx=20,variable=v,value=2,font='Times 16',command=m).pack(anchor=W)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' "3\"',padx=20,variable=v,value=3,font='Times 16',command=m).pack(anchor=W)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' '"That's okey"'',padx=20,variable=v,value=4,font='Times 16',command=m).pack(anchor=W)
    
        
    def Quit(event=None):
        
        if askokcancel("Quit", "Do you really want to Quit?"):
            root.destroy()
            result()
    def r():
        
        root.destroy()
        result()
    
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    s = Frame(root, height=30, bg='black')
    Button(s, text = 'EXIT',width=16,height=1,bg='light blue',fg='black',font='Times 10 bold', command = Quit).pack(side=LEFT,expand=NO, anchor=SW)
    Button(s, text = 'RESULT',width=16,height=1,bg='light blue',fg='black',font='Times 10 bold', command = r).pack(side=RIGHT,expand=NO, anchor=SE)
    s.pack(side=BOTTOM,expand=NO, fill=X)
#**********************************************************************************************************************************************************************
#**********************************************************************************************************************************************************************
def ques5even():
    global count
    root=Tk()
    root.attributes('-fullscreen',True)
    v=IntVar()
    def m():
        if(v.get()==4):
            global num
            num=num+2
            
        else:
            num
    shortcutbar = Frame(root, height=30, bg='light blue')
    toolbar = Label(shortcutbar, text='Quiz Test',bg='black',fg='white',height=2,font='CalibriLight 12 bold')
    toolbar.pack(side=TOP,fill=X,expand=YES)
    shortcutbar.pack(expand=NO, fill=X)
    social_bar = 0
    social_bar = 1
    
    def counter_label(label):
        def count():
            global counter
            counter= counter+1
            if counter>59:
                global x
                x=x+counter/60
                counter=counter/60
                if x>59:
                    global y
                    y=y+x/60
                    x=x/60
            global t
            t=str(y)+':'+str(x)+':'+str(counter)
            label.config(text=str(t))
            label.after(1000,count)

            if x==5:
                root.destroy()
                result()
        count()
    label=Label(root,fg='red',font='Arial 18 bold')
    label.pack(side=TOP,anchor=NE)
    counter_label(label)
    
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root, text = 'Q5. Given a function that does not return any value, What value is thrown by itby default when executed in shell.',fg='black',font='Times 19').pack(side=TOP,expand=NO,anchor=NW)
    #Label(root, text = '       gorblflur means fan belt.',fg='black',font='Times 19').pack(side=TOP,expand=NO,anchor=NW)
    #Label(root, text = '       pixngorbl means ceiling fan.',fg='black',font='Times 19').pack(side=TOP,expand=NO,anchor=NW)
    #Label(root, text = '       arthtusl means tile roof.',fg='black',font='Times 19').pack(side=TOP,expand=NO,anchor=NW)
    #Label(root, text = '       Which word could mean "ceiling tile"?',fg='black',font='Times 19').pack(side=TOP,expand=NO,anchor=NW)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' int',padx=20,variable=v,value=1,font='Times 16',command=m).pack(anchor=W)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' bool',padx=20,variable=v,value=2,font='Times 16',command=m).pack(anchor=W)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' void',padx=20,variable=v,value=3,font='Times 16',command=m).pack(anchor=W)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' None ',padx=20,variable=v,value=4,font='Times 16',command=m).pack(anchor=W)
        
    def Quit(event=None):
        
        if askokcancel("Quit", "Do you really want to Quit?"):
            root.destroy()
            result()
    def r():
        
        root.destroy()
        result()
    
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    s = Frame(root, height=30, bg='light green')
    Button(s, text = 'EXIT',width=16,height=1,bg='light blue',fg='black',font='Times 10 bold', command = Quit).pack(side=LEFT,expand=NO, anchor=SW)
    Button(s, text = 'RESULT',width=16,height=1,bg='light blue',fg='black',font='Times 10 bold', command = r).pack(side=RIGHT,expand=NO, anchor=SE)
    s.pack(side=BOTTOM,expand=NO, fill=X)

#**********************************************************************************************************************************************************************
#**********************************************************************************************************************************************************************
def ques4odd():
    global count
    root=Tk()
    root.attributes('-fullscreen',True)
    v=IntVar()
    def m():
        if(v.get()==2):
            global num
            num=num+2
        
        else:
            num
    shortcutbar = Frame(root, height=30, bg='light blue')
    toolbar = Label(shortcutbar, text='Quiz Test',bg='black',fg='white',height=2,font='CalibriLight 12 bold')
    toolbar.pack(side=TOP,fill=X,expand=YES)
    shortcutbar.pack(expand=NO, fill=X)

    def q2():
        root.destroy()
        ques5odd()
    def counter_label(label):
        def count():
            global counter
            counter= counter+1
            if counter>59:
                global x
                x=x+counter/60
                counter=counter/60
                if x>59:
                    global y
                    y=y+x/60
                    x=x/60
            global t
            t=str(y)+':'+str(x)+':'+str(counter)
            label.config(text=str(t))
            label.after(1000,count)

            if x==5 :
                root.destroy()
                result()
        count()
    label=Label(root,fg='red',font='Arial 18 bold')
    label.pack(side=TOP,anchor=NE)
    counter_label(label)
    
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root, text = 'Q4. What is the average value of the code that is executed below ?What is the average value of the code that is executed below ? ',fg='black',font='Times 19').pack(side=TOP,expand=NO,anchor=NW)
    Label(root, text = '       1. >>>grade1 = 80',fg='black',font='Times 19').pack(side=TOP,expand=NO,anchor=NW)
    Label(root, text = '       2. >>>grade2 = 90',fg='black',font='Times 19').pack(side=TOP,expand=NO,anchor=NW)
    Label(root, text = '       3. >>>average = (grade1 + grade2) / 2',fg='black',font='Times 19').pack(side=TOP,expand=NO,anchor=NW)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' 85',padx=20,variable=v,value=1,font='Times 16',command=m).pack(anchor=W)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' 85.0',padx=20,variable=v,value=2,font='Times 16',command=m).pack(anchor=W)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' 95',padx=20,variable=v,value=3,font='Times 16',command=m).pack(anchor=W)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' 95.0',padx=20,variable=v,value=4,font='Times 16',command=m).pack(anchor=W)
    
       
    def Quit(event=None):
       
        if askokcancel("Quit", "Do you really want to Quit?"):
            root.destroy()
            result()
    
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    s = Frame(root, height=30, bg='light green')
    Button(s, text = 'EXIT',width=16,height=1,bg='light blue',fg='black',font='Times 10 bold', command = Quit).pack(side=LEFT,expand=NO, anchor=SW)
    Button(s, text = 'NEXT',width=16,height=1,bg='light blue',fg='black',font='Times 10 bold', command = q2).pack(side=RIGHT,expand=NO, anchor=SE)
    s.pack(side=BOTTOM,expand=NO, fill=X)
#**********************************************************************************************************************************************************************
#**********************************************************************************************************************************************************************
def ques4even():
    global count
    root=Tk()
    root.attributes('-fullscreen',True)
    v=IntVar()
    def m():
        if(v.get()==1):
            global num
            num=num+2
            
        else:
            num
    shortcutbar = Frame(root, height=30, bg='light blue')
    toolbar = Label(shortcutbar, text='Quiz Test',bg='black',fg='white',height=2,font='CalibriLight 12 bold')
    toolbar.pack(side=TOP,fill=X,expand=YES)
    shortcutbar.pack(expand=NO, fill=X)

    def q2():
       
        root.destroy()
        ques5even()

    def counter_label(label):
        def count():
            global counter
            counter= counter+1
            if counter>59:
                global x
                x=x+counter/60
                counter=counter/60
                if x>59:
                    global y
                    y=y+x/60
                    x=x/60
            global t
            t=str(y)+':'+str(x)+':'+str(counter)
            label.config(text=str(t))
            label.after(1000,count)

            if x==5:
                root.destroy()
                result()
        count()
    label=Label(root,fg='red',font='Arial 18 bold')
    label.pack(side=TOP,anchor=NE)
    counter_label(label)
    
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root, text = 'Q4. FAG, GAF, HAI, IAH, ____ ',fg='black',font='Times 19').pack(side=TOP,expand=NO,anchor=NW)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' JAK',padx=20,variable=v,value=1,font='Times 16',command=m).pack(anchor=W)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' HAL',padx=20,variable=v,value=2,font='Times 16',command=m).pack(anchor=W)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' HAK',padx=20,variable=v,value=3,font='Times 16',command=m).pack(anchor=W)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' JAL',padx=20,variable=v,value=4,font='Times 16',command=m).pack(anchor=W)
    
        
    def Quit(event=None):
        
        if askokcancel("Quit", "Do you really want to Quit?"):
            root.destroy()
            result()
   
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    s = Frame(root, height=30, bg='light green')
    Button(s, text = 'EXIT',width=16,height=1,bg='light blue',fg='black',font='Times 10 bold', command = Quit).pack(side=LEFT,expand=NO, anchor=SW)
    Button(s, text = 'NEXT',width=16,height=1,bg='light blue',fg='black',font='Times 10 bold', command = q2).pack(side=RIGHT,expand=NO, anchor=SE)
    s.pack(side=BOTTOM,expand=NO, fill=X)
#*********************************************************************************************************************************************************************
#*********************************************************************************************************************************************************************
def ques3odd():
    global count
    root=Tk()
    root.attributes('-fullscreen',True)
    v=IntVar()
    def m():
        if(v.get()==3):
            global num
            num=num+2
            
        else:
            num
    shortcutbar = Frame(root, height=30, bg='light blue')
    toolbar = Label(shortcutbar, text='Quiz Test',bg='black',fg='white',height=2,font='CalibriLight 12 bold')
    toolbar.pack(side=TOP,fill=X,expand=YES)
    shortcutbar.pack(expand=NO, fill=X)

    def q2():
        
        root.destroy()
        ques4odd()
    def counter_label(label):
        def count():
            global counter
            counter= counter+1
            if counter>59:
                global x
                x=x+counter/60
                counter=counter/60
                if x>59:
                    global y
                    y=y+x/60
                    x=x/60
            global t
            t=str(y)+':'+str(x)+':'+str(counter)
            label.config(text=str(t))
            label.after(1000,count)

            if x==5 :
                root.destroy()
                result()
        count()
    label=Label(root,fg='red',font='Arial 18 bold')
    label.pack(side=TOP,anchor=NE)
    counter_label(label)
    
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root, text = 'Q3. Look at this series: 22, 21, 23, 22, 24, 23, ... What number should come next?  ',fg='black',font='Times 19').pack(side=TOP,expand=NO,anchor=NW)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' 22',padx=20,variable=v,value=1,font='Times 16',command=m).pack(anchor=W)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' 24',padx=20,variable=v,value=2,font='Times 16',command=m).pack(anchor=W)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' 25',padx=20,variable=v,value=3,font='Times 16',command=m).pack(anchor=W)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' 26',padx=20,variable=v,value=4,font='Times 16',command=m).pack(anchor=W)
    
       
    def Quit(event=None):
     
        if askokcancel("Quit", "Do you really want to Quit?"):
            root.destroy()
            result()
    
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    s = Frame(root, height=30, bg='light green')
    Button(s, text = 'EXIT',width=16,height=1,bg='light blue',fg='black',font='Times 10 bold', command = Quit).pack(side=LEFT,expand=NO, anchor=SW)
    Button(s, text = 'NEXT',width=16,height=1,bg='light blue',fg='black',font='Times 10 bold', command = q2).pack(side=RIGHT,expand=NO, anchor=SE)
    s.pack(side=BOTTOM,expand=NO, fill=X)
#**********************************************************************************************************************************************************************
#**********************************************************************************************************************************************************************
def ques3even():
    global count
    root=Tk()
    root.attributes('-fullscreen',True)
    v=IntVar()
    def m():
        if(v.get()==2):
            global num
            num=num+2
           
        else:
            num
    shortcutbar = Frame(root, height=30, bg='light blue')
    toolbar = Label(shortcutbar, text='Quiz Test',bg='black',fg='white',height=2,font='CalibriLight 12 bold')
    toolbar.pack(side=TOP,fill=X,expand=YES)
    shortcutbar.pack(expand=NO, fill=X)

    def q2():
        
        root.destroy()
        ques4even()

    def counter_label(label):
        def count():
            global counter
            counter= counter+1
            if counter>59:
                global x
                x=x+counter/60
                counter=counter/60
                if x>59:
                    global y
                    y=y+x/60
                    x=x/60
            global t
            t=str(y)+':'+str(x)+':'+str(counter)
            label.config(text=str(t))
            label.after(1000,count)

            if x==5:
                root.destroy()
                result()
        count()
    label=Label(root,fg='red',font='Arial 18 bold')
    label.pack(side=TOP,anchor=NE)
    counter_label(label)
    
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root, text = 'Q3. Look at this series: 7, 10, 8, 11, 9, 12, ... What number should come next? ',fg='black',font='Times 19').pack(side=TOP,expand=NO,anchor=NW)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' 7',padx=20,variable=v,value=1,font='Times 16',command=m).pack(anchor=W)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' 10',padx=20,variable=v,value=2,font='Times 16',command=m).pack(anchor=W)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' 12',padx=20,variable=v,value=3,font='Times 16',command=m).pack(anchor=W)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' 13',padx=20,variable=v,value=4,font='Times 16',command=m).pack(anchor=W)
    
        
    def Quit(event=None):
        
        if askokcancel("Quit", "Do you really want to Quit?"):
            root.destroy()
            result()
    
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    s = Frame(root, height=30, bg='light green')
    Button(s, text = 'EXIT',width=16,height=1,bg='light blue',fg='black',font='Times 10 bold', command = Quit).pack(side=LEFT,expand=NO, anchor=SW)
    Button(s, text = 'NEXT',width=16,height=1,bg='light blue',fg='black',font='Times 10 bold', command = q2).pack(side=RIGHT,expand=NO, anchor=SE)
    s.pack(side=BOTTOM,expand=NO, fill=X)
#*********************************************************************************************************************************************************************
#*********************************************************************************************************************************************************************
def ques2even():
    global count
    root=Tk()
    root.attributes('-fullscreen',True)
    v=IntVar()
    def m():
        if(v.get()==2):
            global num
            num=num+2
            
        else:
            num
    shortcutbar = Frame(root, height=30, bg='light blue')
    toolbar = Label(shortcutbar, text='Quiz Test',bg='black',fg='white',height=2,font='CalibriLight 12 bold')
    toolbar.pack(side=TOP,fill=X,expand=YES)
    shortcutbar.pack(expand=NO, fill=X)

    def q2():
        
        root.destroy()
        ques3even()
    def counter_label(label):
        def count():
            global counter
            counter= counter+1
            if counter>59:
                global x
                x=x+counter/60
                counter=counter/60
                if x>59:
                    global y
                    y=y+x/60
                    x=x/60
            global t
            t=str(y)+':'+str(x)+':'+str(counter)
            label.config(text=str(t))
            label.after(1000,count)

            if x==5:
                root.destroy()
                result()
        count()
    label=Label(root,fg='red',font='Arial 18 bold')
    label.pack(side=TOP,anchor=NE)
    counter_label(label)
    
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root, text = 'Q2. In a family of two generations ,there are two couples. A has only two sons and a brother C. E is the only daughter of D. B is a  ',fg='black',font='Times 19').pack(side=TOP,expand=NO,anchor=NW)
    Label(root, text = '       female married into the family and has no daughters. How is B related to E.',font='Times 19').pack(side=TOP,expand=NO,anchor=NW)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' Uncle',padx=20,variable=v,value=1,font='Times 16',command=m).pack(anchor=W)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' Aunt',padx=20,variable=v,value=2,font='Times 16',command=m).pack(anchor=W)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' Sister',padx=20,variable=v,value=3,font='Times 16',command=m).pack(anchor=W)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' Data Insufficient',padx=20,variable=v,value=4,font='Times 16',command=m).pack(anchor=W)
    
       
    def Quit(event=None):
        
        if askokcancel("Quit", "Do you really want to Quit?"):
            root.destroy()
            result()
    
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    s = Frame(root, height=30, bg='light green')
    Button(s, text = 'EXIT',width=16,height=1,bg='light blue',fg='black',font='Times 10 bold', command = Quit).pack(side=LEFT,expand=NO, anchor=SW)
    Button(s, text = 'NEXT',width=16,height=1,bg='light blue',fg='black',font='Times 10 bold', command = q2).pack(side=RIGHT,expand=NO, anchor=SE)
    s.pack(side=BOTTOM,expand=NO, fill=X)
#**********************************************************************************************************************************************************************
#**********************************************************************************************************************************************************************
def ques2odd():
    global count
    root=Tk()
    root.attributes('-fullscreen',True)
    v=IntVar()
    def m():
        if(v.get()==4):
            global num
            num=num+2
            
        else:
            num
    shortcutbar = Frame(root, height=30, bg='light blue')
    toolbar = Label(shortcutbar, text='Quiz Test',bg='black',fg='white',height=2,font='CalibriLight 12 bold')
    toolbar.pack(side=TOP,fill=X,expand=YES)
    shortcutbar.pack(expand=NO, fill=X)

    def q2():
       
        root.destroy()
        ques3odd()

    def counter_label(label):
        def count():
            global counter
            counter= counter+1
            if counter>59:
                global x
                x=x+counter/60
                counter=counter/60
                if x>59:
                    global y
                    y=y+x/60
                    x=x/60
            global t
            t=str(y)+':'+str(x)+':'+str(counter)
            label.config(text=str(t))
            label.after(1000,count)

            if x==5:
                root.destroy()
                result()
        count()
    label=Label(root,fg='red',font='Arial 18 bold')
    label.pack(side=TOP,anchor=NE)
    counter_label(label)
    
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root, text = 'Q2. Nayeem walks 4km towards west,he walks 9 km to the north and then turns to his left and walks 5 km and finally walks 3 km ',fg='black',font='Times 19').pack(side=TOP,expand=NO,anchor=NW)
    Label(root, text = '       towards north. How far he is from starting position.',fg='black',font='Times 19').pack(side=TOP,expand=NO,anchor=NW)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' 12 km',padx=20,variable=v,value=1,font='Times 16',command=m).pack(anchor=W)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' 21 km',padx=20,variable=v,value=2,font='Times 16',command=m).pack(anchor=W)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' 18 km',padx=20,variable=v,value=3,font='Times 16',command=m).pack(anchor=W)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' 15 km',padx=20,variable=v,value=4,font='Times 16',command=m).pack(anchor=W)
    
        
    def Quit(event=None):
       
        if askokcancel("Quit", "Do you really want to Quit?"):
            root.destroy()
            result()
    
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    s = Frame(root, height=30, bg='light green')
    Button(s, text = 'EXIT',width=16,height=1,bg='light blue',fg='black',font='Times 10 bold', command = Quit).pack(side=LEFT,expand=NO, anchor=SW)
    Button(s, text = 'NEXT',width=16,height=1,bg='light blue',fg='black',font='Times 10 bold', command = q2).pack(side=RIGHT,expand=NO, anchor=SE)
    s.pack(side=BOTTOM,expand=NO, fill=X)
#*********************************************************************************************************************************************************************
#*********************************************************************************************************************************************************************

def ques1even():
    global count
    root=Tk()
    root.attributes('-fullscreen',True)
    v=IntVar()
    def m():
        if(v.get()==3):
            global num
            num=num+2
            
        else:
            num
    shortcutbar = Frame(root, height=30, bg='light blue')
    toolbar = Label(shortcutbar, text='Quiz Test',bg='black',fg='white',height=2,font='CalibriLight 12 bold')
    toolbar.pack(side=TOP,fill=X,expand=YES)
    shortcutbar.pack(expand=NO, fill=X)

    def q1():
        
        root.destroy()
        ques2even()

    def counter_label(label):
        def count():
            global counter
            counter= counter+1
            if counter>59:
                global x
                x=x+counter/60
                counter=counter/60
                if x>59:
                    global y
                    y=y+x/60
                    x=x/60
            global t
            t=str(y)+':'+str(x)+':'+str(counter)
            label.config(text=str(t))
            label.after(1000,count)

            if x==5:
                root.destroy()
                result()
        count()
    label=Label(root,fg='red',font='Arial 18 bold')
    label.pack(side=TOP,anchor=NE)
    counter_label(label)
    
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root, text = 'Q1. Champu elephant walked 10 km to the east. He then turned right and walked 9 km,turned right and walked 7 km,and again turned',fg='black',font='Times 19').pack(side=TOP,expand=NO,anchor=NW)
    Label(root, text = '       right and walked 5 km. How far he is now from original position.',fg='black',font='Times 19').pack(side=TOP,expand=NO,anchor=NW)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' 31 km',padx=20,variable=v,value=1,font='Times 16',command=m).pack(anchor=W)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' 4 km',padx=20,variable=v,value=2,font='Times 16',command=m).pack(anchor=W)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' 5 km',padx=20,variable=v,value=3,font='Times 16',command=m).pack(anchor=W)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' 0 km',padx=20,variable=v,value=4,font='Times 16',command=m).pack(anchor=W)
    
        
    def Quit(event=None):
        
        if askokcancel("Quit", "Do you really want to Quit?"):
            root.destroy()
            result()
    
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    s = Frame(root, height=30, bg='light green')
    Button(s, text = 'EXIT',width=16,height=1,bg='light blue',fg='black',font='Times 10 bold', command = Quit).pack(side=LEFT,expand=NO, anchor=SW)
    Button(s, text = 'NEXT',width=16,height=1,bg='light blue',fg='black',font='Times 10 bold', command = q1).pack(side=RIGHT,expand=NO, anchor=SE)
    s.pack(side=BOTTOM,expand=NO, fill=X)

#*********************************************************************************************************************************************************************
#*********************************************************************************************************************************************************************
def ques1odd():
    global count
    root=Tk()
    root.attributes('-fullscreen',True)
    v=IntVar()
    def m():
        if(v.get()==2):
            global num
            num=num+2
            
        else:
            num
    shortcutbar = Frame(root, height=30, bg='light blue')
    toolbar = Label(shortcutbar, text='Quiz Test',bg='black',fg='white',height=2,font='CalibriLight 12 bold')
    toolbar.pack(side=TOP,fill=X,expand=YES)
    shortcutbar.pack(expand=NO, fill=X)

    
    def counter_label(label):
        def count():
            global counter
            counter= counter+1
            if counter>59:
                global x
                x=x+counter/60
                counter=counter/60
                if x>59:
                    global y
                    y=y+x/60
                    x=x/60
            global t
            t=str(y)+':'+str(x)+':'+str(counter)
            label.config(text=str(t))
            label.after(1000,count)

            if x==5:
                root.destroy()
                result()
        count()
    label=Label(root,fg='red',font='Arial 18 bold')
    label.pack(side=TOP,anchor=NE)
    counter_label(label)
    def q1():
        
        root.destroy()
        ques2odd()
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root, text = 'Q1. A woman while looking at the photograph of a man said, "He is the maternal grandfather of children of my husband'"'s"' sister."',fg='black',font='Times 19').pack(side=TOP,expand=NO,anchor=NW)
    Label(root, text = '       How is he related to woman.',fg='black',font='Times 19').pack(side=TOP,expand=NO,anchor=NW)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' Father',padx=20,variable=v,value=1,font='Times 16',command=m).pack(anchor=W)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' Father-in-law',padx=20,variable=v,value=2,font='Times 16',command=m).pack(anchor=W)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' Grandfather',padx=20,variable=v,value=3,font='Times 16',command=m).pack(anchor=W)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Radiobutton(root,text=' Brother-in-law ',padx=20,variable=v,value=4,font='Times 16',command=m).pack(anchor=W)

        
    def Quit(event=None):
        
        if askokcancel("Quit", "Do you really want to Quit?"):
            root.destroy()
            result()
    
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)

    s = Frame(root, height=24, bg='light green')
    Button(s, text = 'EXIT',width=16,height=1,bg='light blue',fg='black',font='Times 10 bold', command = Quit).pack(side=LEFT,expand=NO, anchor=SW)
    Button(s, text = 'NEXT',width=16,height=1,bg='light blue',fg='black',font='Times 10 bold', command = q1).pack(side=RIGHT,expand=NO, anchor=SE)
    s.pack(side=BOTTOM,expand=NO, fill=X)
    
#*********************************************************************************************************************************************************************
#*********************************************************************************************************************************************************************
def page3odd():
    root=Tk()
    root.attributes('-fullscreen',True)

    shortcutbar = Frame(root, height=30, bg='light blue')
    toolbar = Label(shortcutbar, text='Quiz Test',bg='black',fg='white',height=2,font='CalibriLight 12 bold')
    toolbar.pack(side=TOP,fill=X,expand=YES)
    shortcutbar.pack(expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    
    shortcutbar1 = Frame(root)
    toolbar1 = Label(shortcutbar1,text="Please read the instructions carefully",font='Times 14 bold')
    toolbar1.pack(side=LEFT,fill=X,anchor=W)
    shortcutbar1.pack(expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    
    shortcutbar1 = Frame(root)
    toolbar1 = Label(shortcutbar1,text="1. This test contains 5 questions.",font='Calibri 12 ')
    toolbar1.pack(side=LEFT,fill=X,anchor=W)
    shortcutbar1.pack(expand=NO, fill=X)

    shortcutbar1 = Frame(root)
    toolbar1 = Label(shortcutbar1,text="2. The test is of 10 marks.",font='Calibri 12 ')
    toolbar1.pack(side=LEFT,fill=X,anchor=W)
    shortcutbar1.pack(expand=NO, fill=X)

    shortcutbar1 = Frame(root)
    toolbar1 = Label(shortcutbar1,text="3. All questions are multiple choice and are compulsory. ",font='Calibri 12 ')
    toolbar1.pack(side=LEFT,fill=X,anchor=W)
    shortcutbar1.pack(expand=NO, fill=X)

    shortcutbar1 = Frame(root)
    toolbar1 = Label(shortcutbar1,text="4. You can only attempt in sequential order.  ",font='Calibri 12 ')
    toolbar1.pack(side=LEFT,fill=X,anchor=W)
    shortcutbar1.pack(expand=NO, fill=X)

    shortcutbar1 = Frame(root)
    toolbar1 = Label(shortcutbar1,text="5. Test is time bound. You have 5 mins for completing the test. ",font='Calibri 12 ')
    toolbar1.pack(side=LEFT,fill=X,anchor=W)
    shortcutbar1.pack(expand=NO, fill=X)

    shortcutbar1 = Frame(root)
    toolbar1 = Label(shortcutbar1,text="6. The marks alloted per question will be 2. ",font='Calibri 12 ')
    toolbar1.pack(side=LEFT,fill=X,anchor=W)
    shortcutbar1.pack(expand=NO, fill=X)

    shortcutbar1 = Frame(root)
    toolbar1 = Label(shortcutbar1,text="7. Once you opt for a question you can go to another question without completing or submitting the current one but then you cannot return to the previous one. ",font='Calibri 12 ')
    toolbar1.pack(side=LEFT,fill=X,anchor=W)
    shortcutbar1.pack(expand=NO, fill=X)

    shortcutbar1 = Frame(root)
    toolbar1 = Label(shortcutbar1,text="8. Your score will be displayed once you complete all the questions or when you quit the test. ",font='Calibri 12 ')
    toolbar1.pack(side=LEFT,fill=X,anchor=W)
    shortcutbar1.pack(expand=NO, fill=X)

    shortcutbar1 = Frame(root)
    toolbar1 = Label(shortcutbar1,text="9. There is no scope of cheating. So concentrate on ur screen. ",font='Calibri 12 ') 
    toolbar1.pack(side=LEFT,fill=X,anchor=W)
    shortcutbar1.pack(expand=NO, fill=X)

    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    
    Label(root,text='\nClick START to Continue' ,fg='red',font='AdobeHeitiStdR 13').pack(side=TOP,pady=70)
    def next3():
        root.destroy()
        ques1odd()
    def Quit(event=None):
        if askokcancel("Quit", "Do you really want to Quit?"):
            root.destroy()

    s = Frame(root, height=24, bg='light green')
    Button(root, text = 'EXIT',width=16,height=1,bg='light blue',fg='black',font='Times 10 bold', command = Quit).pack(side=LEFT,expand=NO, anchor=SW)
    Button(root, text = 'START',width=16,height=1,bg='light blue',fg='black',font='Times 10 bold', command = next3 ).pack(side=RIGHT,expand=NO,anchor=SE )
    s.pack(side=BOTTOM,expand=NO, fill=X)
#********************************************************************************************************************************************************************
#********************************************************************************************************************************************************************
def page3even():
    root=Tk()
    root.attributes('-fullscreen',True)

    shortcutbar = Frame(root, height=30, bg='light blue')
    toolbar = Label(shortcutbar, text='Quiz Test',bg='black',fg='white',height=2,font='CalibriLight 12 bold')
    toolbar.pack(side=TOP,fill=X,expand=YES)
    shortcutbar.pack(expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    
    shortcutbar1 = Frame(root)
    toolbar1 = Label(shortcutbar1,text="Please read the instructions carefully",font='Times 14 bold')
    toolbar1.pack(side=LEFT,fill=X,anchor=W)
    shortcutbar1.pack(expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    
    shortcutbar1 = Frame(root)
    toolbar1 = Label(shortcutbar1,text="1. This test contains 5 questions.",font='Calibri 14 ')
    toolbar1.pack(side=LEFT,fill=X,anchor=W)
    shortcutbar1.pack(expand=NO, fill=X)

    shortcutbar1 = Frame(root)
    toolbar1 = Label(shortcutbar1,text="2. The test is of 10 marks.",font='Calibri 14 ')
    toolbar1.pack(side=LEFT,fill=X,anchor=W)
    shortcutbar1.pack(expand=NO, fill=X)

    shortcutbar1 = Frame(root)
    toolbar1 = Label(shortcutbar1,text="3. All questions are multiple choice and are compulsory. ",font='Calibri 14 ')
    toolbar1.pack(side=LEFT,fill=X,anchor=W)
    shortcutbar1.pack(expand=NO, fill=X)

    shortcutbar1 = Frame(root)
    toolbar1 = Label(shortcutbar1,text="4. You can only attempt in sequential order.  ",font='Calibri 14 ')
    toolbar1.pack(side=LEFT,fill=X,anchor=W)
    shortcutbar1.pack(expand=NO, fill=X)

    shortcutbar1 = Frame(root)
    toolbar1 = Label(shortcutbar1,text="5. Test is time bound. You have 5 mins for completing the test. ",font='Calibri 14 ')
    toolbar1.pack(side=LEFT,fill=X,anchor=W)
    shortcutbar1.pack(expand=NO, fill=X)

    shortcutbar1 = Frame(root)
    toolbar1 = Label(shortcutbar1,text="6. The marks alloted per question will be 2. ",font='Calibri 14 ')
    toolbar1.pack(side=LEFT,fill=X,anchor=W)
    shortcutbar1.pack(expand=NO, fill=X)

    shortcutbar1 = Frame(root)
    toolbar1 = Label(shortcutbar1,text="7. Once you opt for a question you can go to another question without completing or submitting the current one but then you cannot return to the previous one. ",font='Calibri 14')
    toolbar1.pack(side=LEFT,fill=X,anchor=W)
    shortcutbar1.pack(expand=NO, fill=X)

    shortcutbar1 = Frame(root)
    toolbar1 = Label(shortcutbar1,text="8. Your score will be displayed once you complete all the questions or when you quit the test. ",font='Calibri 14 ')
    toolbar1.pack(side=LEFT,fill=X,anchor=W)
    shortcutbar1.pack(expand=NO, fill=X)

    shortcutbar1 = Frame(root)
    toolbar1 = Label(shortcutbar1,text="9. There is no scope of cheating. So concentrate on ur screen. ",font='Calibri 12 ') 
    toolbar1.pack(side=LEFT,fill=X,anchor=W)
    shortcutbar1.pack(expand=NO, fill=X)
    

    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)

    
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    
    Label(root,text='\nClick START to Continue' ,fg='red',font='AdobeHeitiStdR 13').pack(side=TOP,pady=70)
    def next3():
        root.destroy()
        ques1even()
    def Quit(event=None):
        if askokcancel("Quit", "Do you really want to Quit?"):
            root.destroy()

    s = Frame(root, height=30, bg='light green')
    Button(s, text = 'EXIT',width=16,height=1,bg='light blue',fg='black',font='Times 10 bold', command = Quit).pack(side=LEFT,expand=NO, anchor=SW)
    Button(s, text = 'START',width=16,height=1,bg='light blue',fg='black',font='Times 10 bold', command = next3 ).pack(side=RIGHT,expand=NO,anchor=SE )
    s.pack(side=BOTTOM,expand=NO, fill=X)
#**********************************************************************************************************************************************************************
#**********************************************************************************************************************************************************************
def page2():
    root=Tk()
    root.attributes('-fullscreen',True)
    def Quit1(event=None):
        if askokcancel("Quit", "Do you really want to Quit?"):
            root.destroy()
            page1()
    shortcutbar = Frame(root, height=30, bg='light blue')
    Button(shortcutbar,justify=CENTER,text='CLOSE',activeforeground='khaki',overrelief=SOLID,relief=GROOVE,command=Quit1,bg='red',activebackground='blue',cursor="hand2").pack(side=RIGHT,anchor=NE,fill=Y)
    toolbar = Label(shortcutbar, text='Quiz Test',bg='black',fg='white',height=2,font='CalibriLight 12 bold')
    toolbar.pack(side=TOP,fill=X,expand=YES)
    shortcutbar.pack(expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)

    shortcutbar1 = Frame(root)
    toolbar1 = Label(shortcutbar1,text="Welcome to our Quiz.\nPlease fill in the below given registration form to continue.",fg='blue',height=2,font='Calibri 12 bold')
    toolbar1.pack(side=TOP,fill=X,expand=YES)
    shortcutbar1.pack(expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)

    shortcutbar2 = Frame(root)
    e1 = Entry(shortcutbar2)
    toolbar2 = Label(shortcutbar2, text="Enrollment No.  ",font='Arial 10 bold')
    toolbar2.pack(side=LEFT,fill=X,expand=NO)
    e1.pack(side=LEFT,expand=YES)
    shortcutbar2.pack(expand=NO)
    Label(root,text=" ").pack(side=TOP,expand=NO)

    shortcutbar3 = Frame(root)
    e2 = Entry(shortcutbar3)
    toolbar2 = Label(shortcutbar3, text="First Name        ",font='Arial 10 bold')
    toolbar2.pack(side=LEFT,fill=X,expand=NO)
    e2.pack(side=LEFT,expand=YES, fill=X)
    shortcutbar3.pack(expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)

    shortcutbar4 = Frame(root)
    e3 = Entry(shortcutbar4)
    toolbar2 = Label(shortcutbar4, text="Last Name        ",font='Arial 10 bold')
    toolbar2.pack(side=LEFT,fill=X,expand=NO)
    e3.pack(side=LEFT,expand=YES, fill=X)
    shortcutbar4.pack(expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)


    shortcutbar4 = Frame(root)
    e4 = Entry(shortcutbar4)
    toolbar2 = Label(shortcutbar4, text="Branch              ",font='Arial 10 bold')
    toolbar2.pack(side=LEFT,fill=X,expand=NO)
    e4.pack(side=LEFT,expand=YES, fill=X)
    shortcutbar4.pack(expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    
    shortcutbar4 = Frame(root)
    e5 = Entry(shortcutbar4)
    toolbar2 = Label(shortcutbar4, text="Batch                ",font='Arial 10 bold')
    toolbar2.pack(side=LEFT,fill=X,expand=NO)
    e5.pack(side=LEFT,expand=YES, fill=X)
    shortcutbar4.pack(expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)

    def next2():
        if (int(str(e1.get()))%2==0):
            root.destroy()
            page3even()
        else:
            root.destroy()
            page3odd()
    def Quit(event=None):
        if askokcancel("Quit", "Do you really want to Quit?"):
            root.destroy()
    def info():
            if(str(e1.get())=='' or str(e2.get())=='' or str(e3.get())=='' or str(e4.get())=='' or str(e5.get())==''):
                s=showerror(title="Error",message='Fill the entries.')
            else:
                Label(root,text='Thanks '+(str(e2.get()).title())+' '+(str(e3.get()).title())+' '+'('+e1.get()+')'+' '+'for enrolling with us.',fg='Dark Blue',font='Times 14').pack(side=TOP)
                Label(root,text='\n\n\nClick NEXT to Continue' ,fg='red',font='AdobeHeitiStdR 14').pack(side=TOP,pady=100)
                s = Frame(root, height=30, bg='light green')
                Button(s, text = 'NEXT',width=16,height=1,bg='light blue',fg='black',font='Times 10 bold', command = next2 ).pack(side=RIGHT,expand=NO,anchor=SE )
                s.pack(side=BOTTOM,expand=NO, fill=X)
    def submit(event=None):
        if askokcancel("SUBMIT", "Are you sure you want to Submit?"):
            info()
            
            
    
           
    Button(root, text = 'SUBMIT',width=10,height=1,bg='light blue',fg='black',font='Times 10 bold', command = submit ).pack(side=TOP,expand=NO, anchor=SW)
    
#*************************************************************************************************************************************************************
#*************************************************************************************************************************************************************
def aboutus():
    root=Tk()
    root.attributes('-fullscreen',True)

    shortcutbar = Frame(root, height=30, bg='light green')
    toolbar = Label(shortcutbar, text='Quiz Test',bg='black',fg='white',height=2,font='CalibriLight 12 bold')
    toolbar.pack(side=TOP,fill=X,expand=YES)
    shortcutbar.pack(expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root,text=" ").pack(side=TOP,expand=NO, fill=X)
    Label(root, text='\n\n\n\n\nThe project is designed by',fg='black',font='Times 18').pack(side=TOP,anchor=CENTER)
    Label(root, text='YUVRAJ SINGH PARMAR(151453)',fg='red',font='Times 20 bold').pack(side=TOP,anchor=CENTER)
    Label(root, text='Branch - CSE(B7)',fg='purple',font='Times 16 bold').pack(side=TOP,anchor=CENTER)
    Label(root, text='Email: yuvrajparmar1997@gmail.com',fg='black',font='Times 16 bold').pack(side=TOP,anchor=CENTER)
    Label(root, text='\nUnder the guiadence of',fg='black',font='Times 18').pack(side=TOP,anchor=CENTER)
    Label(root, text='Dr. Mahesh Kumar',fg='green',font='Times 20 bold').pack(side=TOP,anchor=CENTER)
    Label(root, text='\n\n\n\n\n\n\n\n\nSign up to Enroll & Continue',fg='blue',font='Times 12').pack(side=TOP,anchor=CENTER)
    def sbmt():
        root.destroy()
        page2()
    s = Frame(root, height=30, bg='light green')
    Button(s, text='EXIT',width=16,height=1,bg='light blue',fg='black',font='Times 12 bold',command=root.destroy).pack(side=LEFT, anchor=SW)
    Button(s, text='SIGN UP',width=16,height=1,bg='light blue',fg='black',font='Times 12 bold',command=sbmt).pack(side=RIGHT, anchor=SE)
    s.pack(side=BOTTOM,expand=NO, fill=X)
#*******************************************************************************************************************************************************
#*******************************************************************************************************************************************************

global page1
def page1():
    root = Tk()
    root.attributes('-fullscreen',True)
    shortcutbar = Frame(root, height=30, bg='light green')
    toolbar = Label(shortcutbar, text='Quiz Test',bg='black',fg='black',height=2,font='CalibriLight 14 bold')
    toolbar.pack(side=LEFT,fill=X,expand=YES)
    shortcutbar.pack(expand=NO, fill=X)
    shortcutbar1 = Frame(root, height=1000, bg='black')
  
    
    Label(shortcutbar1, text='\n\n\n\n\n\n\nWelcome to Quiz Test\n\n',bg='black',fg='white',font='Times 25').pack(side=TOP,anchor=CENTER)
    Label(shortcutbar1, text='TEST THE IQ\n\n\n\n',bg='black',fg='white',font='Times 25').pack(side=TOP,anchor=CENTER)
    Label(shortcutbar1, text='Sign up to Continue',bg='black',fg='white',font='Times 12').pack(side=TOP,anchor=CENTER)
    
    def abt():
        root.destroy()
        aboutus()
    def sbmt():
        root.destroy()
        page2()
    def Quit(event=None):
        if askokcancel("Quit", "Do you really want to Quit?"):
            root.destroy()
    Button(shortcutbar1, text='SIGN UP',width=16,height=1,bg='grey',fg='black',font='Times 12 bold',command=sbmt,relief=RAISED).pack()
    shortcutbar1.pack(expand=NO, fill=X)
    shortcutbar3 = Frame(root, height=60, bg='black')
    shortcutbar3.pack(expand=NO, fill=X)
    shortcutbar2 = Frame(root, height=768, bg='light blue')
    Button(shortcutbar2, text='ABOUT US',width=16,height=1,bg='grey',fg='black',font='Times 12 bold',command=abt).pack(side=RIGHT, anchor=SE)
    Button(shortcutbar2, text='EXIT',width=16,height=1,bg='grey',fg='black',font='Times 12 bold',command=Quit).pack(side=LEFT, anchor=SW)
    shortcutbar2.pack(side=BOTTOM,expand=NO, fill=BOTH)
    root.mainloop()
page1()
