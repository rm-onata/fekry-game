import tkinter as t
from tkinter import messagebox as mb
from PIL import Image, ImageTk
from bidi.algorithm import get_display
import arabic_reshaper as ar
import json





gui = t.Tk()
gui.geometry("650x350")
gui.resizable(False, False)
gui.title("Math")
gui.configure(bg='#0079fb')

image1 = Image.open("zoz.jpg")
test = ImageTk.PhotoImage(image1)

label1 = t.Label(gui, image=test)
label1.photo = test
label1.place(x=0, y=0, height = 350, width = 650)



class Quiz:
    def __init__(self):
         
        self.q_no=0
         
        self.display_question()
         

        self.opt_selected=t.IntVar()
         

        self.opts=self.radio_buttons()
         
        self.display_options()
         
        self.data_size=len(question)
         
        self.correct=0



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
         
        if self.q_no==self.data_size:
             
            self.display_result()
             
            gui.destroy()
        else:
            self.display_question()
            self.display_options()



    def display_options(self):
        val=0
      
        self.opt_selected.set(0)
         

        for option in options[self.q_no]:
            self.opts[val]['text']=option
            val+=1
 
 
    def display_question(self):
         
        q_no = t.Label(gui, text=question[self.q_no], font=('ariel' , 16, 'bold' ))
         
        q_no.place(x=40, y=50)


    def radio_buttons(self):
         
        q_list = []
         
        y_pos = 100
         
        while len(q_list) < 4:
             
            radio_btn = t.Radiobutton(gui,text=" ",variable=self.opt_selected, value = len(q_list)+1,font = ("ariel",14))
             
            q_list.append(radio_btn)
             
            radio_btn.place(x = 70, y = y_pos)
             
            y_pos += 30

        return q_list



    



with open('media/data.json') as f:
    data = json.load(f)


question = (data['question'])
options = (data['options'])
answer = (data[ 'answer'])      
quiz = Quiz()
 
text1 = 'بعدی'
text2 = 'خروج'
tex1 = get_display(ar.reshape(text1))
tex2 = get_display(ar.reshape(text2))


next_button = t.Button(gui, text=tex1,command = quiz.next_btn, width=10,bg="#fbf9f0", fg="#101010",font=("ariel",16,"bold"))
next_button.place(x=230,y=280)
quit_button = t.Button(gui, text=tex2, command = gui.destroy, width=5,bg="black", fg="white",font=("ariel",16," bold"), relief='ridge')         
quit_button.place(x=560,y=10)



gui.mainloop()
