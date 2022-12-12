# import module
from tkinter import *
from tkinter import messagebox

# configure 
ws = Tk()
ws.title("Exams and Records")
ws.geometry("700x700")

questions = { "1": "What is the full meaning of HTML?",
              "2": "What is the full meaning of CSS?",
              "3": "What is the full meaning of JS?",
              "4": "What year was python released?",
              "5": "What is the value of 10 x 10?",
}

answers = ["Hypertext Markup Language", "Cascading stylessheet", "Javascript", 1994, 100]
ans = []

def correct_answers():
    correct = 0

    ans.insert(0, ans1_tf.get())
    ans.insert(1, ans2_tf.get())
    ans.insert(2, ans3_tf.get())
    ans.insert(3, ans4_tf.get())
    ans.insert(4, ans5_tf.get())

    if ans[0].lower() == answers[0].lower():
        correct += 1
    if ans[1].lower() == answers[1].lower():
        correct += 1
    if ans[2].lower() == answers[2].lower():
        correct += 1
    if int(ans[3]) == answers[3]:
        correct += 1
    if int(ans[4]) == answers[4]:
        correct += 1

    if correct > 3:
        return messagebox.showinfo("Submit", f"Bravo, your score is {correct}/{len(questions)}")
    else:
       return messagebox.showinfo("Submit", f"Try again, you scored {correct}/{len(questions)}")


    
# write code
que1_lb = Label(ws,text=questions["1"]).pack()
answer_lb = Label(ws,text="Answer:").pack()
ans1_tf = Entry(ws)
ans1_tf.pack()

que2_lb = Label(ws,text=questions["2"]).pack()
answer_lb = Label(ws,text="Answer:").pack()
ans2_tf = Entry(ws)
ans2_tf.pack()

que3_lb = Label(ws,text=questions["3"]).pack()
answer_lb = Label(ws,text="Answer:").pack()
ans3_tf = Entry(ws)
ans3_tf.pack()

que4_lb = Label(ws,text=questions["4"]).pack()
answer_lb = Label(ws,text="Answer:").pack()
ans4_tf = Entry(ws)
ans4_tf.pack()

que5_lb = Label(ws,text=questions["5"]).pack()
answer_lb = Label(ws,text="Answer:").pack()
ans5_tf = Entry(ws)
ans5_tf.pack()




#This would be more efficient but we need better way to store user input individually to an index location
"""for i in questions.items():
    que_lb = Label(ws,text=f'{i[0]}: {i[1]}').pack()
    #print(f'{i[0]}: {i[1]}')
    answer_lb = Label(ws,text="Answer:").pack()
    user_tf = Entry(ws)
    ans.append(user_tf.get())
    user_tf.pack()
"""


submit_btn = Button(ws, text="Submit", command=correct_answers).pack()

# infinite loop
ws.mainloop()

