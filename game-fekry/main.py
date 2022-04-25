import tkinter as t
from PIL import Image, ImageTk
from awesometkinter.bidirender import add_bidi_support
from bidi.algorithm import get_display
import arabic_reshaper as ar
import os






root = t.Tk()
root.title("Menu")
root.geometry("1080x650+100+20")
root.resizable(False, False)

xx = 0



def math():
    global xx
    os.system('python3 math.py')
    xx += 1
    add_bidi_support(score)
    root.after(1000, lambda: score.set('امتیاز :{}'.format(xx)))


def car_rah():
    global xx
    os.system('python3 rahnamaee.py')
    xx += 1
    add_bidi_support(score)
    root.after(1000, lambda: score.set('امتیاز :{}'.format(xx)))


def zarb():
    global xx
    os.system('python3 zarb.py')
    xx += 1
    add_bidi_support(score)
    root.after(1000, lambda: score.set('امتیاز :{}'.format(xx)))


def abot():
    win = t.Tk()
    win.title('about')
    win.geometry('440x200')
    win.resizable(False, False)
    win.configure(bg='#a1def8')

    url1 = 'https://github.com/r4myh/game-fekry'
    t.Label(win, text='my github : {0}'.format(url1), bg='#0173f8',fg='#a1def8').pack()

    url2 = 'https://www.instagram.com/0day_online'
    t.Label(win, text='my page on instagram : {0}'.format(url2), bg='#0173f8',fg='#a1def8').pack()


    
    win.mainloop()



def draw_visitor():
    for widget in dashboard.winfo_children():
        widget.destroy()
    
    image1 = Image.open("gdg.jpg")
    test = ImageTk.PhotoImage(image1)
    label1 = t.Label(dashboard,image=test)
    label1.photo = test

    text1='جمع و تفریق'
    text2=' راهنمایی رانندگی'
    text3='درباره'
    text4='جدول ضرب'

    tex1 = get_display(ar.reshape(text1))
    tex2 = get_display(ar.reshape(text2))
    tex3 = get_display(ar.reshape(text3))
    tex4 = get_display(ar.reshape(text4))

    label1.place(x=0, y=0, height = 500, width = 1080)
    op1= t.Button(dashboard, command = math, text=tex1 ,bd =0, font=("any 20",16), bg = "#010189",fg="#eae2b7", justify='right')
    op1.place(x=855, y=75, width = 200, height = 50)
    op2= t.Button(dashboard, command = car_rah, text=tex2,bd =0, font=("any 20",16), bg = "#010189",fg="#eae2b7", justify='right')
    op2.place(x=855, y=200, width = 200, height = 50)
    op3= t.Button(dashboard, command = abot, text=tex3,bd =0, font=("any 20",16), bg = "#010189",fg="#eae2b7", justify='right')
    op3.place(x=855, y=425, width = 200, height = 50)
    op4= t.Button(dashboard, command = zarb,bd =0, text=tex4,font=("any 20",16), bg = "#010189",fg="#eae2b7", justify='right')
    op4.place(x=855, y=315, width = 200, height = 50)











#Header
header = t.Frame(root, bg="#0191d8", bd=0)
header.place(x=0,y=0,width=1080,height=100)

nsec = t.Label(header, font=("Helvetica",36,"bold"), bg = "#0191d8",fg="#101010")
nsec.place(x=105, y=20, width=950)

add_bidi_support(nsec)
nsec.set('پنل بازی های فکری')


#Profile frame
frame = t.Frame(root, bg="#01e8d8")
frame.place(x=0,y=100 ,width=1080,height=50)

welcome_text = t.Label(frame, font=("Minion Pro Regular", 16), bg="#01e8d8", fg='#303030')
welcome_text.place(x=890, y=10)

add_bidi_support(welcome_text)
welcome_text.set('منو بازیها')


#score
score = t.Label(frame, font=("Minion Pro Regular", 16), bg="#909090", fg="orange")
score.place(x=20, y=10)

add_bidi_support(score)
score.set('امتیاز :{0}'.format(xx))


dashboard = t.Frame(root, bg="#bbb", bd=0)
dashboard.place(x=0,y=150 ,width=1080,height=500)
draw_visitor()

root.mainloop()
