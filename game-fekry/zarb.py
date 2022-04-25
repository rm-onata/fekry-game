import tkinter as t
from awesometkinter.bidirender import add_bidi_support
import arabic_reshaper as ar
from bidi.algorithm import get_display
import random






root = t.Tk()
root.geometry('270x200')
root.resizable(False, False)
root.title('math')
root.configure(bg='#0079fb')

ye = random.randrange(10)
do = random.randrange(10)
answ = t.StringVar()



x = ye * do
vr = t.Label(root, bg='#f9ff71', fg='black')

add_bidi_support(vr)
def ok():
    vr.set('جواب :{}'.format(x))
    vr.pack()
    answ.set("")



def aftr():
    add_bidi_support(vr)
    bb = root.after(9000, lambda: vr.set('جواب :{}'.format(xx)))

    for z in range(1000):
        rx = random.randrange(10)
        ry = random.randrange(10)
        xx = rx * ry
        root.after(1000, lambda: lb.config(text='{} x {} =  '.format(rx, ry)))
        root.after(1000, lambda: btn.config(command=bb))
        answ.set("")






fram = t.Frame(root, bd= 5, relief= 'sunken', bg='#00f0fb')
fram.pack()


lb = t.Label(fram, text= "{} x {} =  ".format(ye, do), bg='#707070', fg='black')
lb.pack(side='left')

ent = t.Entry(fram, textvariable=answ ,width=5, bg='#707070', fg='black')
ent.pack(side='left')

text1 = 'شروع'
tex1 = get_display(ar.reshape(text1))

btn = t.Button(fram, text=tex1, bg='#ece900',command=ok)
btn.pack(side='bottom')

text2 = 'تعویض'
tex2 = get_display(ar.reshape(text2))
t.Button(fram, text=tex2, bg='#ece900',command=aftr).pack(side='bottom')





fram.pack(fill= 'x',padx= 15, pady= 15)
fram.config(padx= 20,pady= 20)

root.mainloop()