from tkinter import *
from tkinter import messagebox as mb
from PIL import ImageTk,Image
root=Tk()


def new_window1():

    def add():
        
        addwind=Toplevel(root)

        def save():
                    c=x.get()
                    b=y.get()
                    d=z.get()
                    e=z11.get()
                    k=0

                    if c=='':
                        la='si'
                    else:

                        f1=open('contacts2.txt','r')

                        for line in f1:
                            if c in line:
                                k+=1
                                l9=Label(addwind,text='name exists').pack()
                                break
                            elif b in line:
                                k+=1
                                l8=Label(addwind,text='number exists').pack()
                                break
                            elif c in line:
                                k+=1
                                l7=Label(addwind,text='mail exists').pack()
                                break
                            elif e in line:
                                        k+=1
                                        l6=Label(addwind,text='address exists')
                                        break
                            elif len(b)!=10:
                                        k+=1
                                        l5=Label(addwind,text='invalid contact')
                                        break
                                
                        f1.close

                        if k==0:
                            f1=open('contacts2.txt','a')
                            f1.write('Name: ')
                            f1.write(c)
                            f1.write('\n')
                            f1.write('Number: ')
                            f1.write(b)
                            f1.write('\n')
                            f1.write('E-mail ID: ')
                            f1.write(d)
                            f1.write('\n')
                            f1.write('Adress:')
                            f1.write(e)
                            f1.write('\n')
                            f1.write('\n')
                            f1.close
                            l88=Label(addwind,text='Added succesfully').pack()

                        else:
                            l99=Label(addwind,text='nothing was added').pack()

        l1=Label(addwind,text='Contact name').pack()
        global x 
        x=Entry(addwind,width=68)
        x.pack()
        l2=Label(addwind,text='Cell number').pack()
        global y
        y=Entry(addwind,width=68)
        y.pack()
        l3=Label(addwind,text='E-mail ID').pack()
        global z
        z=Entry(addwind,width=68)
        z.pack()
        l4=Label(addwind,text='Address').pack()
        global z11
        z11=Entry(addwind,width=68)
        z11.pack()
        b3=Button(addwind,text='+',bg='green',fg='white',command=save).pack()
        save()




    def contact():
            newwind=Toplevel(root)
        
            def phone():
                if cn=='':
                    qq='qq'
                else:
                    message=cn.get()
                    string1= message
                    f1=open('contacts2.txt','r')
                    index=0
                    flag=0

                    for line in f1:
                        index += 1
                        if string1 in line:
                            flag=1
                            break
                
                    if flag == 0:
                        lbl1=Label(newwind,text=string1+' not found').pack()
                    else:
                        f1.close
                        f1 = open('contacts2.txt')
                        content=f1.readlines()
                        var=content[index-1:index+3]
                        for i in var:
                            lab2=Label(newwind,text=i)
                            lab2.pack()
                        
    

            

            l1=Label(newwind,text='Contact name').pack()
            global cn
            cn=Entry(newwind,width=69)
            cn.pack()


            
            
            b3=Button(newwind,text='+',bg='green',fg='white',command=phone).pack()

    def delete():
            newwind2=Toplevel(root)

            def dell():
                    if dl=='':
                        kk='kk'
                    else:
                        delet1 = dl.get()
                        f1 = open('contacts2.txt','r')
                        lin=0
                        hoist=0

                        for line in f1:
                            lin+=1
                            if delet1 in line:
                                hoist = 1
                                break

                        if hoist == 0:
                            labb=Label(newwind2,text='Contact doesnt exist').pack()

                        else:
                            f1 = open('contacts2.txt','r')
                            rem = f1.readlines()
                            f1.close

                            del rem[lin-1:lin+3]
                            new_file = open('contacts2.txt','w+')

                            for line in rem:
                                new_file.write(line)

                            new_file.close
                            labb2=Label(newwind2,text='was succesfully deleted').pack()
                        

            l1=Label(newwind2,text='Contact name').pack()
            global dl
            dl=Entry(newwind2,width=69)
            dl.pack()

            b3=Button(newwind2,text='-',bg='red',fg='white',command=dell).pack()


    def pt():
        newwind4=Toplevel(root)
        sb=Scrollbar(newwind4)
        sb.pack(side=RIGHT,fill=Y)
        mylist = Listbox(newwind4, yscrollcommand = sb.set )
        f1 = open('contacts2.txt','r')
        direc=f1.readlines()
        for i in direc:
            mylist.insert(END,i)
        mylist.pack( side=LEFT,fill = BOTH )
        sb.config( command = mylist.yview )


        

    def ptt():
        newwind3=Toplevel(root)
        sb=Scrollbar(newwind3)
        sb.pack(side=RIGHT,fill=Y)
        mylist = Listbox(newwind3, yscrollcommand = sb.set )
        f1 = open('pass.txt','r')
        direc=f1.readlines()
        for i in direc:
            mylist.insert(END,i)
        mylist.pack( side=LEFT,fill = BOTH )
        sb.config( command = mylist.yview )
                
    newWind=Toplevel(root)

    


    newWind.title('Personal Directory')
    newWind.geometry('400x400')
    
    #Image background with some patches to work on 

    #Define Canvas
    canvas=Canvas(root,height=1620,width=1620)
    canvas.pack(fill='both',expand=True)
    #Add image into canvas

    b11=Button(newWind,text='enter a new contact',command=add).place(x=140,y=30)
    b22=Button(newWind,text='search a conntact',command=contact).place(x=140,y=80)
    b33=Button(newWind,text='Delete contact',command = delete).place(x=140,y=130)
    b44=Button(newWind,text='Complete PT',command = pt).place(x=140,y=180)
    b22=Button(newWind,text='Complete Public PT',command=ptt).place(x=140,y=230)
 
def PubDir():
    Pubdir=Toplevel(root)

    Pubdir.title('Confidential Directory')
    Pubdir.geometry('400x400')
    
    #Image background with some patches to work on 

    #Define Canvas
    canvas=Canvas(root,height=1620,width=1620)
    canvas.pack(fill='both',expand=True)
    #Add image into canvas
    def ent():
        
        
        file=open('password.txt','r')
        passkey=file.read()
        file.close
        passkk=passk.get()
        
        
        if passkk=='':
            lll='lll'
        
        if passkk== passkey:
            pub2=Toplevel(root)
            pub2.geometry('250x250')
                
                
                
            def addon():

                    
                    pubm2=Toplevel(root)

                    def save1():
                                
                                c=x1.get()
                                b=y1.get()
                                d=z1.get()
                                e=zz1.get()
                                k=0

                                if c=='':
                                    lq='sq'
                                else:

                                    f1=open('pass.txt','r')

                                    for line in f1:
                                        if c in line:
                                            k+=1
                                            l9=Label(pubm2,text='name exists').pack()
                                            break
                                        elif b in line:
                                            k+=1
                                            l8=Label(pubm2,text='number exists').pack()
                                            break
                                        elif c in line:
                                            k+=1
                                            l7=Label(pubm2,text='mail exists').pack()
                                            break
                                        elif e in line:
                                            k+=1
                                            l6=Label(pubm2,text='address exists')
                                            break
                                        elif len(b)!=10:
                                            k+=1
                                            l5=Label(pubm2,text='invalid contact')
                                            break
                                    f1.close

                                    if k==0:
                                        f1=open('pass.txt','a')
                                        f1.write('Name: ')
                                        f1.write(c)
                                        f1.write('\n')
                                        f1.write('Number: ')
                                        f1.write(b)
                                        f1.write('\n')
                                        f1.write('E-mail ID: ')
                                        f1.write(d)
                                        f1.write('\n')
                                        f1.write(e)
                                        f1.write('\n')
                                        f1.write('\n')
                                        f1.close
                                        l88=Label(pubm2,text='Added succesfully').pack()

                                    else:
                                        l99=Label(pubm2,text='nothing was added').pack()

                    l11=Label(pubm2,text='Contact name').pack()
                    global x1 
                    x1=Entry(pubm2,width=68)
                    x1.pack()
                    l21=Label(pubm2,text='Cell number').pack()
                    global y1
                    y1=Entry(pubm2,width=68)
                    y1.pack()
                    l3=Label(pubm2,text='E-mail ID').pack()
                    global z1
                    z1=Entry(pubm2,width=68)
                    z1.pack()
                    l4=Label(pubm2,text='Address').pack()
                    zz1=Entry(pubm2,width=68)
                    zz1.pack()
                    b31=Button(pubm2,text='+',bg='green',fg='white',command=save1).pack()
                    save1()

            
            def deltt():

                    pub3=Toplevel(root)

                    def dell():
                            if dl=='':
                                kk='kk'
                            else:
                                delet1 = dl.get()
                                f1 = open('pass.txt','r')
                                lin=0
                                hoist=0

                                for line in f1:
                                    lin+=1
                                    if delet1 in line:
                                        hoist = 1
                                        break

                                if hoist == 0:
                                    labb=Label(pub3,text='Contact doesnt exist').pack()

                                else:
                                    f1 = open('pass.txt','r')
                                    rem = f1.readlines()
                                    f1.close

                                    del rem[lin-1:lin+3]
                                    new_file = open('pass.txt','w+')

                                    for line in rem:
                                        new_file.write(line)

                                    new_file.close
                                    labb2=Label(pub3,text='was succesfully deleted').pack()
                                

                    l1=Label(pub3,text='Contact name').pack()
                    global dl
                    dl=Entry(pub3,width=69)
                    dl.pack()

                    b3=Button(pub3,text='-',bg='red',fg='white',command=dell).pack()
            
            def direcc():
                
                    newwind3=Toplevel(root)
                    sb=Scrollbar(newwind3)
                    sb.pack(side=RIGHT,fill=Y)
                    mylist = Listbox(newwind3, yscrollcommand = sb.set )
                    f1 = open('pass.txt','r')
                    direc=f1.readlines()
                    for i in direc:
                        mylist.insert(END,i)
                    mylist.pack( side=LEFT,fill = BOTH )
                    sb.config( command = mylist.yview )
                                                    

            bp1=Button(pub2,text='enter new contact',command=addon).pack()
            bp2=Button(pub2,text='delete a contact',command=deltt).pack()
            bp3=Button(pub2,text='Get the directory',command=direcc).pack()

        else:
            lab33=Label(Pubdir,text='wrong password').pack()
           


    def cpd():
        entr=Entry(Pubdir,show='*',width=25)
        entr.place(x=120,y=100)
        

        def cpd1():
            if passk=='':
                jj='jj'
            else:

                key=entr.get()
                file=open('password.txt','r')
                passkey=file.read()
                file.close()

                if key == passkey:
                    f1 = open('password.txt','r')
                    rem = f1.readlines()
                    f1.close

                    del rem[0:1]
                    new_file = open('password.txt','w+')

                    for line in rem:
                        new_file.write(line)
                        new_file.close()

                    newkey1=Entry(Pubdir,text='enter the new password: ')
                    newkey1.place(x=120,y=145)
                    newkey=newkey1.get()
                    
                    def inner():
                            if newkey=='':
                                ll='ll'
                            else:
                                new_passkey=open('password.txt','w')
                                new_passkey.write(newkey)
                                new_passkey.close()    
                    buttoon=Button(Pubdir,text='enter',command=inner).place(x=140,y=160)
                else:
                    l100=Label(Pubdir,text='Wrong password').place(x=140,y=180)
        butto=Button(Pubdir,text='enter previous password',command=cpd1).place(x=140,y=120)




    b11=Button(Pubdir,text='Enter password',command=ent).place(x=140,y=30)
    global passk
    passk = Entry(Pubdir,show='*', width=25)
    passk.place(x=120,y=50)
    
    b22=Button(Pubdir,text='Change Password',command=cpd).place(x=140,y=80)
    

root.title('Python Directory')

root.geometry('800x1620')

bg=PhotoImage(file='pngwing.com.png')
#Image background with some patches to work on 

#Define Canvas
canvas=Canvas(root,height=1620,width=1620)
canvas.pack(fill='both',expand=True)
#Add image into canvas
canvas.create_image(0,0 ,image=bg,anchor='nw') #anchor puts the image at top lest and allowws it to expand through out
#Add a label
canvas.create_text(400,250,text='Telephone Directory!!',font=('Comic Sans MS',30),fill='Black')   #fill used in place of fg
#Add Buttons
b1=Button(root,text='Personal Directory',command=new_window1)
b2=Button(root,text='Confidential Directory',command=PubDir)
b3=Button(root,text='exit',command=exit)
#buttons are added as windows here
b1_window=canvas.create_window(410,300,anchor='nw',window=b1)
b2_window=canvas.create_window(410,340,anchor='nw',window=b2)
b3_window=canvas.create_window(410,380,anchor='nw',window=b3)

root.mainloop()
