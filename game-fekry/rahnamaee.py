import tkinter as t
from tkinter import messagebox as mb
import arabic_reshaper as ar
from bidi.algorithm import get_display
from PIL import Image, ImageTk




root = t.Tk()
root.title("rahnamaee")
root.geometry("650x350")
root.resizable(False, False)
root.configure(bg='#99cceb')


###############################
image1 = Image.open("cherag-rahnama.png")
test1 = ImageTk.PhotoImage(image1)

image2 = Image.open("dander.png")
test2 = ImageTk.PhotoImage(image2)

image3 = Image.open("dast-andaz.png")
test3 = ImageTk.PhotoImage(image3)

image5 = Image.open("dor-zadan-mamno.png")
test5 = ImageTk.PhotoImage(image5)

image4 = Image.open("rizesh-sang.png")
test4 = ImageTk.PhotoImage(image4)

image6 = Image.open("tavaghof-mamno.png")
test6 = ImageTk.PhotoImage(image6)

image7 = Image.open("media/vorod-mamno.png")
test7 = ImageTk.PhotoImage(image7)


test = [test1, test2, test3, test4, test5, test6, test7]


class Quiz:
    def __init__(self):
        self.q_no=0
        self.display_question()
        self.opt_selected = t.IntVar()
        self.opts = self.radio_buttons()
        self.display_options()
        self.data_size = len(question)
        self.correct = 0

    def display_result(self):
      wrong_count = self.data_size - self.correct

      correct = f"صحیح: {self.correct}"
      cor = get_display(ar.reshape(correct))

      wrong = f"غلط: {wrong_count}"
      wr = get_display(ar.reshape(wrong))
         
      score = int(self.correct / self.data_size * 100)
      result = f"امتیاز: {score}%"
      re = get_display(ar.reshape(result))
         
      mb.showinfo("Result", f"{re}\n{cor}\n{wr}")
 
 
    def check_ans(self, q_no):
        if self.opt_selected.get() == answer[q_no]:
            return True
 

    def next_btn(self):
        if self.check_ans(self.q_no):
            self.correct += 1
        self.q_no += 1
         
        if self.q_no == self.data_size:
            self.display_result()
            root.destroy()
        else:
            self.display_question()
            self.display_options()


    def display_options(self):
        val = 0
        self.opt_selected.set(0)

        for option in options[self.q_no]:
            self.opts[val]['text'] = option
            val+=1
 
 
    def display_question(self):
         
        q_no = t.Label(root, image=test[self.q_no], bg='#99cceb')
        q_no.photo = test1
        q_no.place(x=300, y=30)


    def radio_buttons(self):
        q_list = []
        y_pos = 100
         
        while len(q_list) < 4:
            radio_btn = t.Radiobutton(root, text=" ",variable=self.opt_selected, value = len(q_list)+1,font = ("ariel",14), bg='#99cceb', fg='#202020')
            q_list.append(radio_btn)
            radio_btn.place(x = 70, y = y_pos)
            y_pos += 30

        return q_list




#####1#####
g1 = get_display(ar.reshape('چراق راهنمایی'))
g2 = get_display(ar.reshape('چراق قوخ'))
g3 = get_display(ar.reshape('چهار راه'))
g4 = get_display(ar.reshape('همه موارد'))
##########

#####2#####
g5 = get_display(ar.reshape('سبقت ممنوع'))
g6 = get_display(ar.reshape('علامت خطر'))
g7 = get_display(ar.reshape('سبقت ازاد'))
g8 = get_display(ar.reshape('هیچکدام'))
###########

#####3######
g9 = get_display(ar.reshape('چاله'))
g10 = get_display(ar.reshape('ایست'))
g11 = get_display(ar.reshape('دست انداز'))
g12 = get_display(ar.reshape('همه موارد'))
############

######4######
g13 = get_display(ar.reshape('سبقت ممنوع'))
g14 = get_display(ar.reshape('دور زدن ممنوع'))
g15 = get_display(ar.reshape('میدان'))
g16 = get_display(ar.reshape('هیچکدام'))
#############

######5########
g17 = get_display(ar.reshape('ریزش سنگ'))
g18 = get_display(ar.reshape('ریزش کوه'))
g19 = get_display(ar.reshape('طبیعت'))
g20 = get_display(ar.reshape('همه موارد'))
#############

######6#######
g21 = get_display(ar.reshape('ورود ممنوع'))
g22 = get_display(ar.reshape('ایست'))
g23 = get_display(ar.reshape('توقف'))
g24 = get_display(ar.reshape('توقف ممنوع'))
###############

######7#######
g25 = get_display(ar.reshape('ایست'))
g26 = get_display(ar.reshape('ورود ممنوع'))
g27 = get_display(ar.reshape('توقف ممنوع'))
g28 = get_display(ar.reshape('همه موارد'))
##############


data = {
    "question": [
      test1,
      test2,
      test3,
      test4,
      test5,
      test6,
      test7
    ],
    "answer": [
      1,
      2,
      3,
      1,
      2,
      4,
      2
    ],
    "options": [
  
      [g1,
        g2,
        g3,
        g4
      ],
      [g5,
        g6,
        g7,
        g8
      ],
      [g9,
        g10,
        g11,
        g12
      ],
      [g17,
        g18,
        g19,
        g20
      ],
      [
          g13,
          g14,
          g15,
          g16
      ],
      [
        g21,
        g22,
        g23,
        g24
      ],
      [
        g25,
        g26,
        g27,
        g28
      ]
    ]
  }


question = (data['question'])
options = (data['options'])
answer = (data[ 'answer'])  
quiz = Quiz()


lb = get_display(ar.reshape('گزینه های درست انتخاب کنید'))
lb1 = t.Label(root, text=lb, fg='black', bg='#8be3d3')
lb1.place(x=35, y=35)

tex1 = get_display(ar.reshape('بعدی'))
next_button = t.Button(root, text=tex1,command = quiz.next_btn, width=10,bg="#fbf9f0", fg="#101010",font=("ariel",16,"bold"))
next_button.place(x=230,y=280)

tex2 = get_display(ar.reshape('خروج'))
quit_button = t.Button(root, text=tex2, command = root.destroy, width=5,bg="black", fg="white",font=("ariel",16," bold"), relief='ridge')         
quit_button.place(x=560,y=10)


root.mainloop()
